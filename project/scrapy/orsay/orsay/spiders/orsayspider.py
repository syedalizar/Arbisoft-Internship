# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from orsay.items import OrsayItem
#dependenciees

class OrsayspiderSpider(CrawlSpider): #main class
    name = 'orsayspider'
    api_url_template = 'http://www.orsay.com/de-de/produkte/?prefn1=availableMarkets&sz=72&start={}&format=page-element&prefv1=de_DE'
    start_urls = [api_url_template.format(0)] #initial start parameter = 0

    def parse(self, response):
        product_list = response.css('.name-link::attr(href)').extract()
        product_urls = [response.urljoin(product_url) for product_url in product_list]
        #extracting urls for all products on the current page

        for product_url in product_urls:
            yield scrapy.Request(url=product_url, callback=self.parse_product)
        #requesting every product url to be parsed individually

        if response.css('div.load-next-placeholder').extract():
            next_page_param_i = int(response.css('div.load-next-placeholder::attr(data-grid-url)')
            next_page_param = next_page_param_i.extract_first().split('start=')[1].split('&')[0])
            yield scrapy.Request(url=self.api_url_template.format(next_page_param), callback=self.parse)
        #checking if the load more button is still there
        #if it is, we perform pagination by extracting the next_page_param parameter
        #then generating new request with it

    def parse_product(self, response):
        #final parse function which extracts details from the product page
        #using css selectors

        item = OrsayItem() #our item defined in items.py

        item["name"] = (response.css('html body div.pt_product-details div#main div.primary-content div.pdp-main.js-pdpMain div.container div.product-top-wrapper.row div.col-xs-12.col-sm-6.col-md-4.product-description-col div.product-col-2.product-detail div#product-content h1.product-name::text').extract())
        item["price"] = (response.css('html body div.pt_product-details div#main div.primary-content div.pdp-main.js-pdpMain div.container div.product-top-wrapper.row div.col-xs-12.col-sm-6.col-md-4.product-description-col div.product-col-2.product-detail div#product-content div.product-price-wrapper div.product-price span.price-sales::text').extract_first().split('\n')[2])
        item["currency"] = (response.css('html body.is-locale-de_DE div#wrapper.pt_product-details header.header.js-header div.header-in div.header-top-navigation div.header-left-side div.top-naigation-menu-item.header-localization div.js-locale-selector.locale-selector.locale-selector-desktop.visually-hidden div.locale-item a.js-locale.locale-link span.locale-text span.country-currency::text').extract_first())
        item["colors"] = ' '.join(response.css('html body div.pt_product-details div#main div.primary-content div.pdp-main.js-pdpMain div.container div.product-top-wrapper.row div.col-xs-12.col-sm-6.col-md-4.product-description-col div.product-col-2.product-detail div#product-content div.product-variations ul li div.value ul.swatches.color li.selectable a::attr(title)').extract())
        item["sizes"] =  ' '.join(response.css('html body div.pt_product-details div#main div.primary-content div.pdp-main.js-pdpMain div.container div.product-top-wrapper.row div.col-xs-12.col-sm-6.col-md-4.product-description-col div.product-col-2.product-detail div#product-content div.product-variations ul li div.value ul.swatches.size li.selectable a::text').extract())
        item["availability_status"] = (response.css('html body div.pt_product-details div#main div.primary-content div.pdp-main.js-pdpMain div.container div.product-top-wrapper.row div.col-xs-12.col-sm-6.col-md-4.product-description-col div.product-col-2.product-detail div#product-content form.pdpForm div.product-add-to-cart div.availability-web div.label span.value div.availability-msg p::text').extract())
        item["category"] = (response.css('html body.is-locale-de_DE div#wrapper.pt_product-details div#main.full-width.clearfix div.container div.pdp-breadcrumbs.breadcrumb-element-back div.breadcrumb a.breadcrumb-element-link span::text').extract()[1:])

        yield item
