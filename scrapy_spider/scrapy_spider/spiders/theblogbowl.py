# -*- coding: utf-8 -*-
import scrapy
from spider.items import blogblowlitem

class TheblogbowlSpider(scrapy.Spider):
    name = 'theblogbowl'
    allowed_domains = ['dada.theblogbowl.in']
    start_urls = ['http://dada.theblogbowl.in/']

    def parse(self, response):

        articles = response.css('div.blog-posts.hfeed div.post.hentry.uncustomized-post-template')

        for sel in articles:
            item = blogblowlitem()
            #item["postdate"] = sel.css("h4.date-header span::text").extract()
            item["posttitle"] = sel.css("h3.post-title.entry-title a::text").extract()
            item["postlabels"] = sel.css("div.post-footer div.post-footer-line.post-footer-line-2 a::text").extract()
            item["postcontent"] = sel.css("div.post-body.entry-content div::text").extract()

            #if  sel.css('h4.date-header').extract_first(default='not-found')

            #item["postcontent"] = sel.css("div.")
            yield(item)

# sel.css('h4.date-header').extract_first(default='not-found')
#checks if h4.date-header exists in sel response or not

        # for article in articles:
        #
        #     date = article.css('span::text').extract()
        #
        #     item = blogblowlitem()
        #     item["postdate"] = date
        #     yield item



        # for i in range (0, len(articles)):
        #     print("article no.")
        #     print(i+1)
        #     print(articles[i])


        # feed = response.css('div.blog-posts.hfeed div.post.hentry.uncustomized-post-template').extract()
        # for i in range(0, len(feed)):
        #     print("article no. " + str(i+1))
        #     print(feed[i])
        # for title in response.css('div.post.hentry h3.post-title a::text').extract():
        #     print(title)
        # for date in response.css('div.blog-posts.hfeed h4.date-header span::text').extract():
        #     print(date)


#scraping text from all divisions under the current xpath division /div/text()
#for hrefs under anchor tags, a/@href
