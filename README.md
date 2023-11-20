# SearchForm
## Установка
```
docker-compose up --build

```
Это установит и запустит контейнер, далее необходимо запустить тесты.
Тесты заполнят бд и сразу покажут наличие ошибок
```
python test_app.py

```
Далее можно свободно тестировать через Postman

### Структура 
app.py - главный файл, где происходит вся магия

test_app.py - тесты

db_add.py - пример базы данных 

