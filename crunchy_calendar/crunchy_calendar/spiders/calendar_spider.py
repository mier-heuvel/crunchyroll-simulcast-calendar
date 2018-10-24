import scrapy

class CrunchyrollCalendar(scrapy.Spider):
    name = "crunchydates"
    start_urls = ['https://www.crunchyroll.com/simulcastcalendar']

    def parse(self, response):
        for day in response.css('.calendar-day'):
            yield {
                'date': day.css('.day-date::attr(data-ga-date)').extract(),
                'show': day.css('.season-name cite::text').extract(),
                'time': day.css('.available-time::text').extract(),
            }