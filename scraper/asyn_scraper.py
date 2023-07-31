from parsel import Selector
import asyncio
import httpx





DEFAULT_HEADERS = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
}


class AsyncNewsScraper:
    START_URL = "https://www.prnewswire.com/news-releases/news-releases-list/?page=1&pagesize=100"
    LINK_XPATH = '//a[@class="newsreleaseconsolidatelink display-outline w-100"]/@href'
    TITLE_XPATH = '//div[@class="col-sm-8 col-lg-9 pull-left card"]/h3/text()'


    async def get_url(self, client, url):
        response = await client.get(url)
        await self.parsel_links(response.text)
        return response

    async def parsel_links(self, content):
        tree = Selector(text=content)
        urls = tree.xpath(self.LINK_XPATH).extract()
        print(urls)

    async def parse_data(self):
          timeout = httpx.Timeout(10.0)
          async with httpx.AsyncClient(headers=DEFAULT_HEADERS, timeout=timeout) as client:
              tasks = []
              for page in range(1, 5):
                  print(self.START_URL.format(page))
                  tasks.append(asyncio.create_task(
                      self.get_url(client, self.START_URL.format(page))))

              new_gather = await asyncio.gather(*tasks)
              await client.aclose()

if __name__ == "__main__":
    scraper = AsyncNewsScraper()
    asyncio.run(scraper.parse_data())