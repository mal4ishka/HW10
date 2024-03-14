from django.shortcuts import render
from bson.objectid import ObjectId
import pymongo


def get_mongodb():
    # Підключаємося до локальної бази даних MongoDB
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    # Вибираємо базу даних, яку ви використовуєте
    db = client['hw']
    return db


def get_quotes_by_tag(tag):
    db = get_mongodb()
    quotes = db.quotes.find({'tags': tag})
    return quotes


def quotes_by_tag(request, tag):
    quotes = get_quotes_by_tag(tag)
    return render(request, 'tags/tags.html', {'tag': tag, 'quotes': quotes})
