import re
from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongo', 27017)
db = client['test_db']


@app.route('/add', methods=['POST'])
def add():
    """Добавляем данные в бд, при запуске тестов база из db_add автоматически добавится в монго"""
    data = request.get_json()
    db.test_collection.insert_many(data)
    return 'Data added'


def validate_email(email):
    """Валидация email. Любое количество символов жо "@", а так же  до и после '.' """
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True


def validate_phone(phone):
    """ Валидация телефона. +7 и 10 цифр после"""
    if re.match(r'^\+7[0-9]{10}$', phone):
        return True


def validate_date(date):
    """Валидация даты двух вариантов. 2023-01-01 или 01.01.2023"""
    if re.match(r"(\d{4}-\d{2}-\d{2})|(\d{2}\.\d{2}\.\d{4})", date):
        return True


@app.route('/get_form', methods=['POST'])
def search():
    """ Принимаем данные и ищем совпадения"""
    form_data = request.form
    result = []  # пустой список, для создания запроса для поиска

    for field, value in form_data.items():  # Проверяем типы у каждого входящего значения
        field_type = 'text'
        if validate_date(value):
            field_type = "date"
        elif validate_phone(value):
            field_type = "phone"
        elif validate_email(value):
            field_type = "email"

        result.append({field: field_type})  # Добавляем в список
    query = {"$and": result}  # Дополнение к запросу. $and - чтобы все формы присутствовали в шаблоне
    doc = list(db.test_collection.find(query, {"_id": 0, "name": 1}))  # Поиск и вывод только имени
    if doc:
        return str(doc)
    else:
        return result  # Если в бд нет нужного документа, то у нас сразу готов нужный ответ. имя поля : тип значения


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
