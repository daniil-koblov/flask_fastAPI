import asyncio
import aiohttp
import aiofiles
import argparse
import time
import os
from download_func import download_image

URLS = [
    "https://img2.akspic.ru/crops/9/3/5/6/7/176539/176539-yagami_lajt-ryuk-tetrad_smerti-r_e_m-multik-7680x4320.jpg",
    "https://img3.akspic.ru/crops/9/3/5/4/7/174539/174539-zheleznyj_chelovek-supergeroj-kapitan_amerika-zhest-palec-7680x4320.jpg",
    "https://img3.akspic.ru/previews/6/2/3/7/7/177326/177326-besporyadochnaya_galaktika_106-messe_106-galaktika-spiralnaya_galaktika-obekt_messe-x750.jpg",
    "https://img1.akspic.ru/crops/4/1/0/7/6/167014/167014-svet-belye-sinij-zelenyj-elektronnyj_instrument-7680x4320.png",
    "https://img2.akspic.ru/crops/7/7/8/5/6/165877/165877-minimalizm-rastenie-simvol-logo-derevo-7680x4320.jpg",
]

async def async_download(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                start_time = time.time()
                filename = url.split("/")[-1]
                if "downloads" not in os.listdir():
                    os.mkdir("downloads")
                image = await aiofiles.open(
                    os.path.join(os.getcwd(), "downloads", filename), mode="wb"
                )
                await image.write(await resp.read())
                await image.close()
                print(
                    f"Время скачивания картинки: {time.time() - start_time:.2f} секунд"
                )


async def main(urls: list[str] = URLS):
    tasks = [asyncio.create_task(async_download(url)) for url in urls]
    await asyncio.gather(*tasks)


# Возможность задавать список URL-адресов через аргументы командной строки
parser = argparse.ArgumentParser(
    prog='list["urls"]', description="Список URL-адресов картинок"
)
parser.add_argument(
    "image_urls", type=str, nargs="*", help="Введите URL-адреса картинок через пробел"
)
args = parser.parse_args()

start = time.time()

if __name__ == "__main__":
    # если список адресов передан в командную строку выполняем эту строку
    if args.image_urls:
        asyncio.run(main(args.image_urls))

    # если список адресов не передан, скачиваем картинки из списка URLS (передан по-умолчанию)
    else:
        asyncio.run(main())
    print(f"Общее время работы программы: {time.time() - start:.2f}")
