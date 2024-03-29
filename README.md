---
ЯП - Спринт 9 - Проект «API для Yatube». Python-разработчик (бекенд) (Яндекс.Практикум)
---
Описание
API для Yatub - проект социальной сети в которой можно, публиковать записи, комментировать записи, а так же подписываться или отписываться от авторов.

Технологии
Python 3.9, Django 3.2, DRF, JWT + Djoser

Запуск проекта в dev-режиме
1) Клонируем репозиторий:
```
git@github.com:code3452/api_final_yatube.git
```
2) устанавливаем виртуальное окружение:
```
python -m venv venv
```
3) Активируем виртуальное окружение:
```
source venv/Scripts/activate
python -m pip install --upgrade pip
```
5) Устанавлиаем зависимости:
```
pip install -r requirements.txt
```
6) Выполняем миграции:
```
python manage.py migrate
```
Запускаем проект:
```
python manage.py runserver
```
Доступ авторизованным пользователем доступен по JWT-токену (Joser), который можно получить выполнив POST запрос по адресу:
```
POST /api/v1/jwt/create/
```
Обновление JWT токена
```
POST /api/v1/jwt/refresh/ - обновление JWT-токена
```
Примеры работы с API для всех пользователей только для чтения:
```
GET api/v1/posts/ - получить список всех публикаций.
GET api/v1/posts/{id}/ - получение публикации по id

GET api/v1/groups/ - получение списка доступных групп
GET api/v1/groups/{id}/ - получение информации о группах по id

GET api/v1/{post_id}/comments/ - получение всех комментариев к публикации
GET api/v1/{post_id}/comments/{id}/ - Получение комментария к публикации по id
```
Автор [Дмитрий Прибавкин](https://github.com/code3452)
