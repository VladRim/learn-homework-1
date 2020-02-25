"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    ask_user_dict = {"Привет": "Привет!", "Как дела?": "Хорошо", "Чем занимаешься?": "Работаю", "Пока": "Пока!"}
    text = None
    while text != "Пока":
        try:
            text = input()
            print(ask_user_dict[text])
        except KeyboardInterrupt:
            print("Пока!")
            break
        except KeyError:
            print(f"А слова {text} нет в словаре")
            print("Добавьте ответ для пополнения словарного запаса, пожаалуйста:)")
            text_ans = input()
            ask_user_dict[text] = text_ans


if __name__ == "__main__":
    ask_user()
