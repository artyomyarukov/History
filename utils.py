import os
from models import ROUTES


def check_files_exist():
    missing_files = []
    for route_id, route_data in ROUTES.items():
        for i, audio_path in enumerate(route_data["audios"]):
            if not os.path.exists(audio_path):
                missing_files.append(f"{route_id} - шаг {i + 1}: {audio_path}")

    if missing_files:
        print("⚠️ Отсутствуют файлы:")
        for file in missing_files:
            print(file)
    else:
        print("✅ Все файлы на месте")