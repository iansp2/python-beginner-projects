import scrapy
import re

class WwiiSpider(scrapy.Spider):
    name = "wwii_spider"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/World_War_II"]

    def parse(self, response):
        # Scrape the article title
        page_title = response.css("h1::text").get() or response.xpath('//title/text()').get()
        if page_title:
            page_title = page_title.replace(" - Wikipedia", "")
            print(f"Scraping article: {page_title}")

        # Extract key dates using a regular expression
        dates = re.findall(r'\b(19[0-9]{2}|20[0-9]{2})\b', response.text)
        
        if dates:
            # Track unique date-paragraph combinations to avoid repetition
            seen_date_paragraphs = set()
            paragraphs = response.css('div.mw-parser-output p::text').getall()
            for paragraph in paragraphs:
                for date in dates:
                    if date in paragraph:
                        date_paragraph_pair = (date, paragraph.strip())
                        if date_paragraph_pair not in seen_date_paragraphs:
                            # Yield the data as a dictionary for Scrapy to save
                            yield {
                                "date": date,
                                "event": paragraph.strip()[:200],  # Limit to 200 characters for simplicity
                                "source": page_title  # Include the source article title
                            }
                            # Mark this pair as seen
                            seen_date_paragraphs.add(date_paragraph_pair)

        # Follow more links from the current article
        article_links = response.css('div.mw-parser-output a::attr(href)').getall()
        for link in article_links:
            if (link.startswith('/wiki/') and 
                not link.startswith('/wiki/Wikipedia:') and 
                not link.startswith('/wiki/Special:') and 
                not link.startswith('/wiki/Help:') and 
                not link.startswith('/wiki/File:') and 
                'disambiguation' not in link):
                yield response.follow(link, callback=self.parse_item)

    def parse_item(self, response):
        # This is a helper method to keep the parsing logic consistent across multiple pages
        return self.parse(response)