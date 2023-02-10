ЯП - Спринт 9 - Проект «API для Yatube». Python-разработчик (бекенд) (Яндекс.Практикум)

Описание
API для Yatub - проект социальной сети в которой можно, публиковать записи, комментировать записи, а так же подписываться или отписываться от авторов.

Технологии
Python 3.9, Django 3.2, DRF, JWT + Djoser

Запуск проекта в dev-режиме
1) Клонировать репозиторий:
git@github.com:code3452/api_final_yatube.git
2) Установите виртуальное окружение:
python -m venv venv
3) venv/Scripts/activate
4) Обновляем pip: 
python -m pip install --upgrade pip
5) Устанавлиаем зависимости из файла requirements.txt
pip install -r requirements.txt
Выполняем миграции:
python manage.py migrate

Запускаем проект:

python manage.py runserver
Примеры работы с API для всех пользователей только для чтения:

GET api/v1/posts/ - получить список всех публикаций.
GET api/v1/posts/{id}/ - получение публикации по id

GET api/v1/groups/ - получение списка доступных групп
GET api/v1/groups/{id}/ - получение информации о группах по id

GET api/v1/{post_id}/comments/ - получение всех комментариев к публикации
GET api/v1/{post_id}/comments/{id}/ - Получение комментария к публикации по id

Получение доступа к эндпоинту /api/v1/follow/ (подписки) доступен только для авторизованных пользователей.

GET /api/v1/follow/ - подписка пользователя от имени которого сделан запрос
на пользователя переданного в теле запроса. 

Доступ авторизованным пользователем доступен по JWT-токену (Joser), который можно получить выполнив POST запрос по адресу:

POST /api/v1/jwt/create/
Передав в body данные пользователя (например в postman):

{
"username": "string",
"password": "string"
}
Полученный токен добавляем в headers (postman), после чего буду доступны все функции проекта:

Authorization: Bearer {your_token}
Обновить JWT-токен:

POST /api/v1/jwt/refresh/ - обновление JWT-токена

Автор Дмитрий Прибавкин

