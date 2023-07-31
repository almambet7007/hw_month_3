from parsel import  Selector
import asyncio
import httpx
from aiogram import  types, Dispatcher
from config import bot


limon_headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
  'Accept': 'application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8'
}

class AsyncLimonScraper:
    START_URL = "https://limon.kg/ru/cat:45"
    LINK_XPATH = '//div[@class="newslist-item"]'

    async def get_limon_url(self,client,url):
       response = await client.get(url)
       await self.parsel_limon_links(response.text)
       return response
    async def parsel_limon_links(self, content):
        tree = Selector(text=content)
        urls = tree.xpath(self.LINK_XPATH).extract()
        print(urls)

    async def pars_limon_data(self):
        timeout = httpx.Timeout(10.0)
        async with httpx.AsyncClient(headers=limon_headers, timeout=timeout) as client:
            articles = []
            for page in range(1, 5):
                print(self.START_URL.format(page))
                articles.append(asyncio.create_task(
                    self.get_limon_url(client, self.START_URL.format(page))))

            new_gather = await asyncio.gather(*articles)
            await client.aclose()
        # return self.urls

async def get_data(message: types.Message):
        limon_scraper = AsyncLimonScraper()
        urls = []
        urls_list = await limon_scraper.pars_limon_data()
        for url in urls_list:
            urls.extend(url)
        for i in range(1,5):
            await bot.send_message(chat_id=message.chat.id,text=urls[i])



def register_scraper(dp: Dispatcher):
    dp.register_message_handler(get_data, commands=["limon_news"])

if __name__ == "__main__":
   scraper = AsyncLimonScraper()
   asyncio.run(scraper.pars_limon_data())