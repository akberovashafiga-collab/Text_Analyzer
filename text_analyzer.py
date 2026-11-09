import re
from collections import Counter
from pathlib import Path


def read_text_file(file_path: str) -> str:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Файл {file_path} не знайдено.")
    content = path.read_text(encoding="utf-8").strip()
    if not content:
        raise ValueError("Файл порожній.")
    return content


def extract_words(text: str) -> list[str]:
    pattern = r"[a-zA-Zа-щьюяєіїґА-ЩЬЮЯЄІЇҐ'’]+"
    return re.findall(pattern, text.lower())


def analyze_text(file_path: str) -> dict:
    text = read_text_file(file_path)
    words = extract_words(text)
    return {
        "total_words": len(words),
        "word_frequency": dict(Counter(words)),
    }


if __name__ == "__main__":
    try:
        res = analyze_text("sample_text.txt")
        print("=== Результати аналізу тексту ===")
        print(f"Загальна кількість слів: {res['total_words']}\n")
        print("Топ-10 слів за частотністю:")
        sorted_words = sorted(
            res["word_frequency"].items(), key=lambda x: x[1], reverse=True
        )
        for word, count in sorted_words[:10]:
            print(f"  {word}: {count}")
    except Exception as e:
        print(f"Помилка: {e}")