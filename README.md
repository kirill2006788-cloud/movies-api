# Описание проекта: 
простой учебный API для каталога фильмов. Проект создан на FastAPI, данные хранятся в базе SQLite, а структура базы управляется с помощью Alembic.
# Основные возможности: 
запуск веб-приложения на FastAPI; проверка работы API через корневой маршрут; хранение информации о фильмах в SQLite; асинхронное подключение к базе данных; модель фильма с проверкой рейтинга и года выпуска; автоматическая документация Swagger и ReDoc; поддержка миграций базы данных через Alembic.
# Технологический стек: 
Python 3.12; FastAPI; Uvicorn; SQLAlchemy; SQLite и aiosqlite; Alembic; Pydantic; Pytest
# Структура проекта: 
moves_api/
|-- alembic/                 
|   |-- versions/            
|   |-- env.py               
|-- src/
|   |-- models/
|   |   |-- __init__.py    
|   |   |-- movie.py         
|   |-- repositories/        
|   |-- routers/             
|   |-- schemas/             
|   |-- database.py          
|   |-- main.py              
|-- tests/                   
|-- alembic.ini              
|-- requirements.txt         
|-- README.md

# Быстрый старт: 
 клонирование репозитория: 
git clone (https://github.com/kirill2006788-cloud/movies-api)>
cd moves_api
 установка зависимостей:
pip install -r requirements.txt
 применение миграций:
alembic upgrade head
 запуск приложения через uvicorn:
uvicorn src.main:app --reload

# Основные эндпоинты: 
"GET /" - проверяет, что приложение запущено и работает; "GET /docs" - открывает интерактивную документацию Swagger; "GET /redoc" - открывает документацию ReDoc
# Фильтрация и сортировка: 
маршрут "GET /movies" возвращает список фильмов; параметр genre фильтрует по жанру; year — по году; min_rating — по минимальному рейтингу; sort_by задаёт поле сортировки (title, year или rating); order задаёт порядок (asc или desc). 
# Модель данных: 
id - integer - уникальный идентификатор фильма, title - string - название фильма, genre - string - жанр, rating - float - рейтинг фильма, year - integer - год выпсука
# Ограничения бд: 
id является первичным ключом; title и genre обязательны для заполнения; rating должен находиться в диапазоне от 0 до 10; year не может быть меньше 1888; для поля title создан индекс для ускорения поиска
