from parsel import Selector
import requests

class NewScraper:
    START_URL = "https://www.prnewswire.com/news-releases/news-releases-list/?page=1&pagesize=100"
    LINK_XPATH = '//a[@class="newsreleaseconsolidatelink display-outline w-100"]/@href'
    TITLE_XPATH = '//div[@class="col-sm-8 col-lg-9 pull-left card"]/h3/text()'

    def parse_data(self):
        text = requests.get(self.START_URL).text
        tree = Selector(text=text)
        links = tree.xpath(self.LINK_XPATH).getall()
        # title = tree.xpath(self.TITLE_XPATH).getall()
        for link in links:
            print("https://www.prnewswire.com" + link)
        return links
        #     print(title)



if __name__ == '__main__':
    scraper = NewScraper()
    scraper.parse_data()