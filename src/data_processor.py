import json
import os


def save_to_json(data, file_path):
    directory = os.path.dirname(file_path)

    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print(f"Data saved to {file_path}")
