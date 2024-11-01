from bs4 import BeautifulSoup
import requests

def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на успешный ответ

        soup = BeautifulSoup(response.content, 'html.parser')
        english_word = soup.find("div", id="random_word")
        word_definition = soup.find("div", id="random_word_definition")

        # Проверка на наличие элементов
        if english_word and word_definition:
            return {
                "english_words": english_word.text.strip(),
                "word_definition": word_definition.text.strip()
            }
        else:
            print("Не удалось найти слово или его определение.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        return None

def word_game():
    print("Игра началась")

    while True:
        word_dict = get_english_words()
        if not word_dict:  # Если произошла ошибка, выходим из цикла
            break

        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        print(f"Значение слова - {word_definition}")
        user = input("Ваш ответ? ")
        if user == word:
            print("Поздравляем, вы угадали слово!")
        else:
            print(f"Вы не угадали слово, попробуйте еще раз - {word}")

        play_again = input("Хотите сыграть еще раз? (y/n) ")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
            break

word_game()