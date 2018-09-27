# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from orsay.items import OrsayItem

class OrsayspiderSpider(CrawlSpider):
    name = 'orsayspider'
    api_url = 'http://www.orsay.com/de-de/produkte/?prefn1=availableMarkets&sz=72&start={}&format=page-element&prefv1=de_DE'
    start_urls = [api_url.format(0)]

    # rules = {
    #         Rule(LinkExtractor(allow=(), deny=()))
    # }
    #

    def parse(self, response):
        product_list = response.css('.name-link::attr(href)').extract()
        product_urls = [response.urljoin(product_url) for product_url in product_list]
        # for product in products:
        #     yield {"url" : product}

        for product_url in product_urls:
            yield scrapy.Request(url=product_url, callback=self.parse_product)

        if response.xpath('//div[@class="load-next-placeholder"]').extract():
            next_page_param = int(response.xpath('/html/body/div/div[@class="load-next-placeholder"]/@data-grid-url').extract_first().split('start=')[1].split('&')[0])
            yield scrapy.Request(url=self.api_url.format(next_page_param), callback=self.parse)


    def parse_product(self, response):
        # available = response.xpath('/html/body/div[1]/div[3]/div[3]/div[1]/div/div[1]/div[2]/div[1]/div/form/div/div/div/span/div/p').extract()
        # if !available:
        # skus ={}  {"skus" :
        #         {"name" : response.css('html body div.pt_product-details div#main div.primary-content div.pdp-main.js-pdpMain div.container div.product-top-wrapper.row div.col-xs-12.col-sm-6.col-md-4.product-description-col div.product-col-2.product-detail div#product-content h1.product-name::text').extract(),
        #          "price" : response.css('html body div.pt_product-details div#main div.primary-content div.pdp-main.js-pdpMain div.container div.product-top-wrapper.row div.col-xs-12.col-sm-6.col-md-4.product-description-col div.product-col-2.product-detail div#product-content div.product-price-wrapper div.product-price .price-sales::text').extract_first().split('\n')[2],
        #          "currency": response.css('html body.is-locale-de_DE div#wrapper.pt_product-details header.header.js-header div.header-in div.header-top-navigation div.header-left-side div.top-naigation-menu-item.header-localization div.js-locale-selector.locale-selector.locale-selector-desktop.visually-hidden div.locale-item a.js-locale.locale-link span.locale-text span.country-currency::text').extract_first(),
        #          "colors" : response.css('html body div.pt_product-details div#main div.primary-content div.pdp-main.js-pdpMain div.container div.product-top-wrapper.row div.col-xs-12.col-sm-6.col-md-4.product-description-col div.product-col-2.product-detail div#product-content div.product-variations ul li div.value ul.swatches.color li.selectable a::attr(title)').extract(),
        #          "sizes":  response.css('html body div.pt_product-details div#main div.primary-content div.pdp-main.js-pdpMain div.container div.product-top-wrapper.row div.col-xs-12.col-sm-6.col-md-4.product-description-col div.product-col-2.product-detail div#product-content div.product-variations ul li div.value ul.swatches.size li.selectable a::text').extract(),
        #          "availability_status" : response.css('html body div.pt_product-details div#main div.primary-content div.pdp-main.js-pdpMain div.container div.product-top-wrapper.row div.col-xs-12.col-sm-6.col-md-4.product-description-col div.product-col-2.product-detail div#product-content form.pdpForm div.product-add-to-cart div.availability-web div.label span.value div.availability-msg p::text').extract(),
        #          "category" : response.css('html body.is-locale-de_DE div#wrapper.pt_product-detailsdiv#main.full-width.clearfix div.container div.pdp-breadcrumbs.breadcrumb-element-back div.breadcrumb a.breadcrumb-element-link span::text').extract()[1:], }
        #          }

#
#         I = ItemLoader(item=OrsayItem(), response=response)
#         I.add_value("name", response.css('html body div.pt_product-details div#main div.primary-content div.pdp-main.js-pdpMain div.container div.product-top-wrapper.row div.col-xs-12.col-sm-6.col-md-4.product-description-col div.product-col-2.product-detail div#product-content h1.product-name::text').extract())
#         I.add_value("price", response.css('html body div.pt_product-details div#main div.primary-content div.pdp-main.js-pdpMain div.container div.product-top-wrapper.row div.col-xs-12.col-sm-6.col-md-4.product-description-col div.product-col-2.product-detail div#product-content div.product-price-wrapper div.product-price span.price-sales::text').extract_first().split('\n')[2])
#         I.add_value("currency", response.css('html body.is-locale-de_DE div#wrapper.pt_product-details header.header.js-header div.header-in div.header-top-navigation div.header-left-side div.top-naigation-menu-item.header-localization div.js-locale-selector.locale-selector.locale-selector-desktop.visually-hidden div.locale-item a.js-locale.locale-link span.locale-text span.country-currency::text').extract_first())
#         I.add_value("colors" , response.css('html body div.pt_product-details div#main div.primary-content div.pdp-main.js-pdpMain div.container div.product-top-wrapper.row div.col-xs-12.col-sm-6.col-md-4.product-description-col div.product-col-2.product-detail div#product-content div.product-variations ul li div.value ul.swatches.color li.selectable a::attr(title)').extract())
#         I.add_value("sizes" , response.css('html body div.pt_product-details div#main div.primary-content div.pdp-main.js-pdpMain div.container div.product-top-wrapper.row div.col-xs-12.col-sm-6.col-md-4.product-description-col div.product-col-2.product-detail div#product-content div.product-variations ul li div.value ul.swatches.size li.selectable a::text').extract())
#         I.add_value("availability_status" , response.css('html body div.pt_product-details div#main div.primary-content div.pdp-main.js-pdpMain div.container div.product-top-wrapper.row div.col-xs-12.col-sm-6.col-md-4.product-description-col div.product-col-2.product-detail div#product-content form.pdpForm div.product-add-to-cart div.availability-web div.label span.value div.availability-msg p::text').extract())
#         I.add_value("category" , response.css('html body.is-locale-de_DE div#wrapper.pt_product-details div#main.full-width.clearfix div.container div.pdp-breadcrumbs.breadcrumb-element-back div.breadcrumb a span::text').extract()[1:]
# )
#
#         yield I.load_item()


        item = OrsayItem()

        item["name"] = ' '.join(response.css('html body div.pt_product-details div#main div.primary-content div.pdp-main.js-pdpMain div.container div.product-top-wrapper.row div.col-xs-12.col-sm-6.col-md-4.product-description-col div.product-col-2.product-detail div#product-content h1.product-name::text').extract())
        item["price"] = ' '.join(response.css('html body div.pt_product-details div#main div.primary-content div.pdp-main.js-pdpMain div.container div.product-top-wrapper.row div.col-xs-12.col-sm-6.col-md-4.product-description-col div.product-col-2.product-detail div#product-content div.product-price-wrapper div.product-price span.price-sales::text').extract_first().split('\n')[2])
        item["currency"] = ' '.join(response.css('html body.is-locale-de_DE div#wrapper.pt_product-details header.header.js-header div.header-in div.header-top-navigation div.header-left-side div.top-naigation-menu-item.header-localization div.js-locale-selector.locale-selector.locale-selector-desktop.visually-hidden div.locale-item a.js-locale.locale-link span.locale-text span.country-currency::text').extract_first())
        item["colors"] = ' '.join(response.css('html body div.pt_product-details div#main div.primary-content div.pdp-main.js-pdpMain div.container div.product-top-wrapper.row div.col-xs-12.col-sm-6.col-md-4.product-description-col div.product-col-2.product-detail div#product-content div.product-variations ul li div.value ul.swatches.color li.selectable a::attr(title)').extract())
        item["sizes"] =  ' '.join(response.css('html body div.pt_product-details div#main div.primary-content div.pdp-main.js-pdpMain div.container div.product-top-wrapper.row div.col-xs-12.col-sm-6.col-md-4.product-description-col div.product-col-2.product-detail div#product-content div.product-variations ul li div.value ul.swatches.size li.selectable a::text').extract())
        item["availability_status"] = ' '.join(response.css('html body div.pt_product-details div#main div.primary-content div.pdp-main.js-pdpMain div.container div.product-top-wrapper.row div.col-xs-12.col-sm-6.col-md-4.product-description-col div.product-col-2.product-detail div#product-content form.pdpForm div.product-add-to-cart div.availability-web div.label span.value div.availability-msg p::text').extract())
        item["category"] = ' '.join(response.css('html body.is-locale-de_DE div#wrapper.pt_product-details div#main.full-width.clearfix div.container div.pdp-breadcrumbs.breadcrumb-element-back div.breadcrumb a.breadcrumb-element-link span::text').extract()[1:])

        yield item

        # SQLALCHEMY
