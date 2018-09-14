# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
            'author_name' : quote.css('small.author::text').extract_first(),
            'text' : quote.css('span.text::text').extract_first(),
            'tags' : quote.css('a.tag::text').extract()
            }
