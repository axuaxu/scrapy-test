import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

response = HtmlResponse(url='http://ca.indeed.com')
print response.selector.xpath('//span/text()').extract()
