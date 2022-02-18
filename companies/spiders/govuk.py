import scrapy

class GovukSpider(scrapy.Spider):
    name = 'govuk'
    allowed_domains = ['find-and-update.company-information.service.gov.uk']
    start_urls = [
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/A?page=1',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/B?page=1',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/C?page=1',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/D?page=1',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/E?page=1',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/F?page=1',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/G?page=1',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/H?page=1',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/I?page=1',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/J?page=1',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/K?page=1',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/L?page=1',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/M?page=1',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/N?page=1',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/O?page=1',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/P?page=1',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/Q?page=1',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/R?page=1',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/S?page=1',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/T?page=1',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/U?page=1',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/V?page=1',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/W?page=1',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/X?page=1',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/Y?page=1',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/Z?page=1',
    ]

    def parse(self, response):
        for row in response.css("table").css("tr"):
            a = row.css('a')
            if a != None:
                try:
                    td = row.css('td')
                    ref = "https://find-and-update.company-information.service.gov.uk"
                    link = a.attrib['href']
                    if ref not in link:
                        link = ref + link
                    yield {
                        "name": td.css('a::text').get(),
                        "link": link,
                        "date": td[1].css('td::text').get(),
                        "post_town": td[2].css('td::text').get()
                    }
                except: pass

        next_page = response.css('a.page[id="next-page"]::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
