from parsel import  Selector
import requests


class LukScraper:
    START_URL_XPATH = "https://mangalib.me/oemojisangjuui?section=chapters"
    LINKS_LUKIZM_XPATH = '//a[@class="link-default"]/@href'

    def get_data(self):
        text = requests.get(self.START_URL_XPATH).text
        tree = Selector(text=text)
        links_luk = tree.xpath(self.LINKS_LUKIZM_XPATH).getall()
        for links in links_luk:
               print("https://mangalib.me"+links)

        # return links_luk


if "__name__" == '__main__':
    scraper = LukScraper()
    scraper.get_data()