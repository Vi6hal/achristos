import asyncio
import time 
import aiohttp
from aiohttp.client import ClientSession

async def download_link(url:str,session:ClientSession):
    async with session.get(url) as response:
        pass
    return

async def download_all(urls:list):
    my_conn = aiohttp.TCPConnector(limit=10)
    conn = aiohttp.ClientSession(connector=my_conn)
    async with conn:
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(download_link(url=url,session=conn))
            tasks.append(task)
        await asyncio.gather(*tasks,return_exceptions=True)

url_list = ["https://sobercheck.herokuapp.com/"]*100

start = time.time()
asyncio.run(download_all(url_list))
end = time.time()
# print(f'download {len(url_list)} links in {end - start} seconds')