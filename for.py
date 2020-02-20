"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    list_of_classes = [
        {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
        {'school_class': '4б', 'scores': [3, 5, 4, 5, 4, 5]},
        {'school_class': '4в', 'scores': [3, 3, 5, 5]},
        {'school_class': '4г', 'scores': [5, 4, 4, 5, 5]}
    ]
    mean_school = 0
    summ_scores_school = 0
    cnt_class = 0
    for clas in list_of_classes:
        summ_scores = 0
        cnt_score = 0
        mean_class = 0
        for score in clas['scores']:
            summ_scores += score
            cnt_score += 1
        mean_class = summ_scores / cnt_score
        print(f"средняя оценка по классу {clas['school_class']} {mean_class}")
        summ_scores_school += mean_class
        cnt_class += 1
        mean_school = summ_scores_school / cnt_class
    print(f"средняя оценка по школе {mean_school}")


if __name__ == "__main__":
    main()
