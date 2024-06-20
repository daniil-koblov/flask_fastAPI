import threading
import argparse
import time
from download_func import download_image


URLS = [
    "https://img2.akspic.ru/crops/9/3/5/6/7/176539/176539-yagami_lajt-ryuk-tetrad_smerti-r_e_m-multik-7680x4320.jpg",
    "https://img3.akspic.ru/crops/9/3/5/4/7/174539/174539-zheleznyj_chelovek-supergeroj-kapitan_amerika-zhest-palec-7680x4320.jpg",
    "https://img3.akspic.ru/previews/6/2/3/7/7/177326/177326-besporyadochnaya_galaktika_106-messe_106-galaktika-spiralnaya_galaktika-obekt_messe-x750.jpg",
    "https://img1.akspic.ru/crops/4/1/0/7/6/167014/167014-svet-belye-sinij-zelenyj-elektronnyj_instrument-7680x4320.png",
    "https://img2.akspic.ru/crops/7/7/8/5/6/165877/165877-minimalizm-rastenie-simvol-logo-derevo-7680x4320.jpg",
]


def thr_download(url_list: list[str] = URLS):
    threads = []
    for url in url_list:
        thread = threading.Thread(target=download_image, args=(url,))
        threads.append(thread)
        thread.start()

    for thr in threads:
        thr.join()


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
    if (
        args.image_urls
    ):  # если список адресов передан в командную строку выполняем эту строку
        thr_download(args.image_urls)
    else:  # если список адресов не передан, скачиваем картинки из списка URLS (передан по-умолчанию)
        thr_download()
    print(f"Общее время работы программы: {time.time() - start:.2f}")