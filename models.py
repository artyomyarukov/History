from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).parent
BOT_TOKEN = os.getenv("BOT_TOKEN")

ROUTES = {
    "orus": {
        "name": "🏛️ Гостиный двор — Чернышевская",
        "link": "https://yandex.ru/maps/?um=constructor%3A4f248e8458d0de2f7167ba4426127d85a08a7da874a3ad8a54a359c2bff0cd2b&source=constructorLink",  # Добавьте реальную ссылку
        "audios": [
            str(BASE_DIR / "assets" / "route_1" / f"{i}-Orus_Gostinka-Chernyshevskaya.wav")
            for i in range(1, 31)
        ]
    },
"tehnologicheskaya": {
        "name": "🏭 Технологический - Василеостровская",
        "link": "https://yandex.ru/maps/2/saint-petersburg/?ll=30.308166%2C59.928251&mode=usermaps&source=constructorLink&um=constructor%3Aa6c9446f80c1daec0e9bcd4366da5c2daa0a794f8ac275db1e7d09f3babb55aa&z=14",
        "audios": [
            str(BASE_DIR / "assets" / "route_2" / f"{i}-tehnologicheskaya-vasileostrovskaya.wav")
            for i in range(1, 17)  # 16 файлов
        ]
    },
    "gostinka": {
        "name": "🌉 Гостиный двор - Невский проспект",
        "link": "https://yandex.ru/maps/?um=constructor%3Ab5ad4733a6a24ea66b074a257108c613b6df135e0a4a3d4c79a6bf6ceaedafcb&source=constructorLink",
        "audios": [
            str(BASE_DIR / "assets" / "route_3" / f"{i}-gostinka-nevskiy.wav")
            for i in range(1, 18)  # 5 файлов
        ]
    },

    "vladimirskaya": {
        "name": "🌃 Владимирская - Чернышевская",
        "link": "https://yandex.ru/maps/2/saint-petersburg/?ll=30.366677%2C59.922064&mode=usermaps&source=constructorLink&um=constructor%3A62e7906ac9a1362c030da8f154a8b6f5a295bb1136d92f71a6c95575a465e16b&z=12.64",
        "audios": [
            str(BASE_DIR / "assets" / "route_4" / f"{i}_vladimirskaya-chernyshevskaya.wav")
            for i in range(1, 23)  # 22 файлов
        ]
    },

    "vosstaniya": {
        "name": "🌆 Площадь Восстания - Чернышевская",
        "link": "https://yandex.ru/maps/2/saint-petersburg/?ll=30.370519%2C59.934041&mode=usermaps&source=constructorLink&um=constructor%3Aeeca6e77b314849b8a158575a6228ed8030eb046147b1276ef5a0786184dbd30&z=14.27",
        "audios": [
            str(BASE_DIR / "assets" / "route_7" / f"{i}-vosstaniya-chernyshevskaya.wav")
            for i in range(1, 7)  # 6 файлов
        ]
    },

    "chernaya-rechka": {
        "name": "🎑 Черная речка - Старая Деревня",
        "link": "https://yandex.ru/maps/?um=constructor%3A5385f8bde711a9f3a3ffc9d5d729b55abfb0cf5ff7032e15af01080368e6ea2c&source=constructorLink",
        "audios": [
            str(BASE_DIR / "assets" / "route_5" / f"{i}-chernaya-rechka-staraya-derevnya.wav")
            for i in range(1, 8)  # 7 файлов
        ]
    },

    "krestovskij": {
        "name": "🎢🎪 Крестовский остров - Беговая",
        "link": "https://yandex.ru/maps/?um=constructor%3A11c9db94d539fa3d2c5fc8cded29afcf8a1451358eb70c9e4d80e024d3d2751a&source=constructorLink",
        "audios": [
            str(BASE_DIR / "assets" / "route_6" / f"{i}-krestovskij-begovaya.wav")
            for i in range(1, 3)  # 2 файлов
        ]
    },
}

# Контакты и информация о проекте
PROJECT_INFO = {
    "website": "https://progulkispbgid.tilda.ws",
    "developers": ["@ArinaRromanova", "@FilatovaElina1","@artemartemmmmm","@helldreamm","@ilbik891"],
    "about": "Этот бот создан для аудиогидов по Санкт-Петербургу..."
}