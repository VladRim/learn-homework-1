"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    ask_user_dict = {"Привет": "Привет!", "Как дела?": "Хорошо", "Чем занимаешься?": "Работаю", "Пока": "Пока!"}
    text = ""
    while text != "Пока":
        try:
            text = input()
            for key in ask_user_dict:
                if text == key:
                    print(ask_user_dict[key])
        except KeyboardInterrupt:
            print("Пока!")
            break


if __name__ == "__main__":
    ask_user()
