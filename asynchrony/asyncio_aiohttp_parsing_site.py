import time
import asyncio
# pip install aiohttp
import aiohttp
# pip install fake-useragent
from fake_useragent import UserAgent
# pip install beautifulsoup4
# pip install lxml
from bs4 import BeautifulSoup

URL = "https://zebrazoo.ru/catalog/koshki/sukhoy-korm/?PAGEN_1="
HEADERS = {"User-Agent": str(UserAgent.random)}
PAGES = 42


async def main():
    product_url_list = []
    try:
        for page in range(PAGES):
            print(f"[*] Start parsing page #{page + 1}")
            new_url = URL + str(page + 1)
            async with aiohttp.ClientSession() as session:
                async with session.get(url=new_url, headers=HEADERS) as response:
                    response_content = await aiohttp.StreamReader.read(response.content)
                    soup = BeautifulSoup(response_content, "lxml")
                    products = soup.find_all(class_="list-showcase__name")
                    for product in products:
                        product_href = product.find("a", href=True).get("href", None)
                        product_url_list.append(f"https://zebrazoo.ru{product_href}")
                    print(f"[*] Parsing page #{page +1} was finished")
    except Exception as ex:
        print(f"[!!] Error: {ex}")
    print(f"[**] All URL products: {product_url_list}")
    return product_url_list


if __name__ == "__main__":
    time_start = time.time()
    event = asyncio.get_event_loop()
    event.run_until_complete(main())
    time_end = time.time()
    print("Delta time: ", time_end - time_start)
