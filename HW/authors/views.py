from django.shortcuts import render
from bson.objectid import ObjectId
import pymongo


def get_mongodb():
    # Підключаємося до локальної бази даних MongoDB
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    # Вибираємо базу даних, яку ви використовуєте
    db = client['hw']
    return db


def get_author(request, author_id):
    # Перетворюємо рядок `author_id` у об'єкт ObjectId
    mongo_author_id = ObjectId(author_id)

    # Припустимо, що у вас є функція `get_mongodb()`, яка повертає підключення до MongoDB
    db = get_mongodb()

    # Отримуємо дані автора з MongoDB за його ObjectId
    author_data = db.authors.find_one({'_id': mongo_author_id})

    # Ви можете використовувати дані автора для відображення у шаблоні
    return render(request, 'authors/author.html', {'author_data': author_data})
