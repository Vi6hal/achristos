import asyncio,time,datetime,aiohttp,os
from aiohttp.client import ClientSession
os.environ.setdefault('DJANGO_SETTINGS_MODULE','achristos.settings')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from django.utils.timezone import make_aware
from registery.models import AppRegistery


async def download_link(url:str,session:ClientSession):
    async with session.get(url) as response:
        result = await response.text()
        print(f'Read {len(result)} from {url}')

async def ping_all(urls:list):
    my_conn = aiohttp.TCPConnector(limit=100)
    async with aiohttp.ClientSession(connector=my_conn) as session:
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(download_link(url=url,session=session))
            tasks.append(task)
        await asyncio.gather(*tasks,return_exceptions=True) # the await must be nest inside of the session

links = list(AppRegistery.objects.filter(bedtime=False).values_list('url',flat=True))
start = time.time()
asyncio.run(ping_all(links))
end = time.time()
print(f'download {len(links)} links in {end - start} seconds')
aware_datetime = make_aware(datetime.datetime.now())
AppRegistery.objects.filter(url__in=links).update(last_pinged=aware_datetime)
