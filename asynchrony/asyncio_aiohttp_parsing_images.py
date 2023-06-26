import time
import asyncio
# pip install aiohttp
import aiohttp

URL = "https://loremflickr.com/320/240"
COUNT_IMAGES = 10


async def create_image(response_data: bytes, count_image: int):
    """ Create file image. """
    with open(f"images/file_{time.time() * 1000}.jpeg", "wb") as file_image:
        file_image.write(response_data)
    print(f"Uploaded image #{count_image}")


async def fetch_content(url: str, session: aiohttp.ClientSession, count_image: int):
    """ Get data from session with get http-request. """
    async with session.get(url=url) as response:
        response_data = await response.read()
        await create_image(response_data, count_image)


async def main():
    """ Create ClientSession and TaskGroup. """
    async with aiohttp.ClientSession() as session:
        async with asyncio.TaskGroup() as tg:
            for count_image in range(COUNT_IMAGES):
                tg.create_task(fetch_content(URL, session, count_image))


if __name__ == "__main__":
    t_start = time.time()
    print(f"[*] Upload started on {t_start}")
    asyncio.run(main())
    t_end = time.time()
    print(f"[*] Upload finished on  {t_end}.\nDownload time: {t_end-t_start}")
