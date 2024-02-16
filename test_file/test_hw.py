import unittest
from main import hw_1, create_file

"""Задача №2 Автотест API Яндекса
Проверим правильность работы Яндекс.Диск REST API. Написать тесты, проверяющий создание папки на Диске.
Используя библиотеку requests напишите unit-test на верный ответ и возможные отрицательные тесты на ответы с ошибкой

Пример положительных тестов:

Код ответа соответствует 200.
Результат создания папки - папка появилась в списке файлов."""


class TestCode(unittest.TestCase):
	"""test for method hw_1()"""
	
	def test_hw_1(self):

		expected = ("Адилет, Азамат, Александр, Алексей, Алена, Анатолий, Анна, Антон, Вадим, Валерий, Владимир, Денис, "
					"Дмитрий, Евгений, Елена, Иван, Илья, Кирилл, Константин, Максим, Михаил, Никита, Николай, Олег,"
					" Павел, Ринат, Роман, Сергей, Татьяна, Тимур, Филипп, Эдгар, Юрий")
		name_mentors = hw_1()
		self.assertEqual(name_mentors, expected)

	def test_create_file(self):
		status_code = 200
		create_folder = create_file()
		self.assertEqual(status_code, create_folder)

	"""it`s errors methods"""
	def test_errors_file(self):
		status_code = 200
		create_folder = create_file()
		self.assertGreater(create_folder, status_code)

	def test_errors_file2(self):
		status_code = 200
		create_folder = create_file()
		self.assertLess(create_folder, status_code)

	def test_errors_file3(self):
		status_code = 200
		create_folder = create_file()
		self.assertLess(create_folder, status_code)


if __name__ == '__main__':
	unittest.main()