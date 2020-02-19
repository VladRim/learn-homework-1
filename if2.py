"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""


def str_comp(string1, string2):
	if type(string1).__name__ == "str" and type(string1).__name__ == "str":
		if string1 == string2:
			return 1
		elif len(string1) > len(string2):
			return 2
		elif string2 == "Learn":
			return 3
	else:
		return 0


def main():
	print(str_comp(23, "23"))
	print(str_comp("123", "345"))
	print(str_comp("fd", "gf"))
	print(str_comp("1238", "123"))
	print(str_comp("123", "123"))
	print(str_comp("123", "Learn"))


if __name__ == "__main__":
	main()
