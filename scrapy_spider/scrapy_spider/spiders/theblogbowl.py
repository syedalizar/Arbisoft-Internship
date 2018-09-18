# -*- coding: utf-8 -*-
import scrapy


class TheblogbowlSpider(scrapy.Spider):
    name = 'theblogbowl'
    allowed_domains = ['dada.theblogbowl.in']
    start_urls = ['http://dada.theblogbowl.in/']

    def parse(self, response):

        feed = response.css('div.blog-posts.hfeed div.post.hentry.uncustomized-post-template').extract()
        for i in range(0, len(feed)):
            print("article no. " + str(i+1))
            print(feed[i])
        # for title in response.css('div.post.hentry h3.post-title a::text').extract():
        #     print(title)
        # for date in response.css('div.blog-posts.hfeed h4.date-header span::text').extract():
        #     print(date)


#scraping text from all divisions under the current xpath division /div/text()
#for hrefs under anchor tags, a/@href
