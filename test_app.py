import unittest
import requests
from db_add import data


class TestFlaskApp(unittest.TestCase):

    def test_add_data(self):
        """ Добавляем данные из db_add в нашу базу """
        response = requests.post('http://localhost:5000/add', json=data)
        self.assertEqual(response.status_code, 200)

    def test_email(self):
        """ Тестируем емейл запросы """
        search_data = {'email': 'test@example.com'}
        response = requests.post('http://localhost:5000/find', data=search_data)
        self.assertEqual(response.status_code, 200)

    def test_phone(self):
        """Тищем телефон"""
        search_data = {'phone': "+76483524344"}
        response = requests.post('http://localhost:5000/find', data=search_data)
        self.assertEqual(response.status_code, 200)

    def test_phone_email(self):
        """Телефон и емейл"""
        search_data = {'phone': "+76483524344", "email": "example@gmail.com"}
        response = requests.post('http://localhost:5000/find', data=search_data)
        self.assertEqual(response.status_code, 200)

    def test_bad_test(self):
        """Невалидные данные"""
        search_data = {'phone': "+76483524344ffff"}
        response = requests.post('http://localhost:5000/find', data=search_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{"phone": "text"}])


if __name__ == '__main__':
    unittest.main()
