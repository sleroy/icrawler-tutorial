from icrawler.builtin import GoogleImageCrawler

def download_images(query, limit):
    google_crawler = GoogleImageCrawler(
        feeder_threads=1,
        parser_threads=2,
        downloader_threads=4,
        storage={'root_dir': 'images'})
    filters = dict(
        size='large',
        color='orange',
        license='commercial,modify',
        date=((2017, 1, 1), (2017, 11, 30)))
    google_crawler.crawl(keyword=query, filters=filters, max_num=1000, file_idx_offset=0)
# Задаем список достопримечательностей и количество изображений, которые нужно загрузить
sights = [
    "Кинотеатр Художественный на Арбате",
    "Театр им. Вахтангова",
    "Центральный Дом Актера на Арбате",
    "Мемориальная квартира А.С. Пушкина на Арбате",
    "Памятник Пушкину и Гончаровой на Арбате",
    "Памятник Окуджаве на Арбате",
    "Хард-рок кафе на Арбате",
    "Дома-книжки на Новом Арбате"
]
num_images = 200

for sight in sights:
    print(f"Загрузка изображений достопримечательности '{sight}':")
    image_paths = download_images(sight, num_images)
    print(f"Загружено {len(image_paths)} изображений\n")