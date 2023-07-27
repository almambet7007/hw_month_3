from parsel import  Selector
import requests


class LukScraper:
    START_URL_XPATH = "https://mangalib.me/oemojisangjuui/v1/c1?page=1"
    LINKS_LUKIZM_XPATH = '//a[@class="menu__item text-truncate"]/@href'

    def get_data(self):
        text = requests.get(self.START_URL_XPATH).text
        tree = Selector(text=text)
        links_luk = tree.xpath(self.LINKS_LUKIZM_XPATH).getall()
        for links in links_luk:
          return links


if __name__ == '__main__':
    scraper = LukScraper()
    scraper.get_data()