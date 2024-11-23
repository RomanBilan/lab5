import re

# Функція для сортування українських та англійських слів
def custom_sort(words):
    ukr_letters = "абвгґдежзийклмнопрстуфхцчшщьюяєії"
    eng_letters = "abcdefghijklmnopqrstuvwxyz"

    def sort_key(word):
        word_lower = word.lower()
        if word_lower[0] in ukr_letters:
            return (0, word_lower)
        elif word_lower[0] in eng_letters:
            return (1, word_lower)
        return (2, word_lower)

    return sorted(words, key=sort_key)

# Читання файлу
def read_first_sentence(file_path: object) -> object:
    try:
        print(f"Шлях до файлу: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            first_sentence = re.split(r'[.!?]', text)[0]
            print("Перше речення:", first_sentence)
            words = re.findall(r'\b\w+\b', first_sentence)
            sorted_words = custom_sort(words)
            print("Відсортовані слова:", sorted_words)
            print("Кількість слів:", len(sorted_words))
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

file_path = 'D:/Білан/text.txt'
read_first_sentence(file_path)
