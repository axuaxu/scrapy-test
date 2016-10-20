import scrapy


class IndeedSpider(scrapy.Spider):
    name = 'indeed'
    #start_urls = ['http://stackoverflow.com/questions?sort=votes']
    start_urls = ['http://ca.indeed.com/jobs?q=python&l=Toronto%2C+ON&sort=date']

    def parse(self, response):
        #for href in response.css('.question-summary h3 a::attr(href)'):
        for href in response.css('.jobtitle a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):
        yield {
            #'title': response.css('h1 a::text').extract_first(),
            'title': response.xpath('//title/text()').extract(),
            'summary': response.css('#job_summary p:nth-of-type(1)').extract(),
            'body': response.css('.question .post-text').extract_first(),
            'tags': response.css('.question .post-tag::text').extract(),
            'link': response.url,
        }
