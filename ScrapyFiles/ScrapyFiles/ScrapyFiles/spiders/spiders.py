# -*- coding: utf-8 -*-
"""
https://www.youtube.com/watch?v=evnbUI09vQQ&list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t&index=8
Watch the above tutorial series

https://www.tutorialspoint.com/scrapy/scrapy_following_links.htm
Read this to see how to follow links in a page.
"""
import scrapy
from ..items import QuotetutorialItem
from ..items import strat_articles_item

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
                'http://quotes.toscrape.com/'
                ]
            
    def parse(self, response):
        items = QuotetutorialItem()
        all_div_quotes = response.css('div.quote')
        
        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()
            
            items ['title'] = title
            items['author'] = author
            items['tags'] = tag
            
            yield items 
            
        next_page = response.css('li.next a::attr(href)').get()
        
        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)
            
class strat_articles_spider(scrapy.Spider):
    name = 'strat_articles'
    
    start_urls = [
                'https://stratpoint.com/articles/'
                ]
    
    def parse(self, response):
        all_sub_urls = response.xpath("//h3/@onclick").extract()
        
        for sub_url in all_sub_urls:
            temp = sub_url.split("='")
            url = response.urljoin(temp[1])
            yield scrapy.Request(url, callback = self.parse_dir_contents)
    
    def parse_dir_contents(self, response):
        items = strat_articles_item()
        body = ""
        temp = response.css("p::text").extract()
        temp = temp + response.css("span::text").extract()
        for sentence in temp:
            body = body + sentence
        
        items['title'] = response.css("h1.entry-title::text").extract() 
        items['body'] = body
       
        
        yield items