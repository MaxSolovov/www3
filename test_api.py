from requests import get, post, delete

print(get('http://localhost:8080/api/news').json())
#
# print(get('http://localhost:8080/api/news/1').json())
#
# print(get('http://localhost:8080/api/news/999').json())
# # новости с id = 999 нет в базе
#
# print(get('http://localhost:8080/api/news/q').json())

# print(post('http://localhost:8080/api/news').json())
#
# print(post('http://localhost:8080/api/news',
#            json={'title': 'Заголовок'}).json())


# print(post('http://localhost:8080/api/news',
#            json={'title': 'Добавлено через API повтор ',
#                  'content': 'Новость добавлена через API blueprint повтор',
#                  'user_id': 1,
#                  'is_private': False
#                  }).json())
#
# print(get('http://localhost:8080/api/news').json())

# print(delete('http://localhost:8080/api/news/999').json())
# новости с id = 999 нет в базе

# print(delete('http://localhost:8080/api/news/8').json())


print(get('http://localhost:8080/api/v2/news').json())
#
print(get('http://localhost:8080/api/v2/news/1').json())
#
print(post('http://localhost:8080/api/v2/news').json())

print(post('http://localhost:8080/api/v2/news',
           json={'title': 'Заголовок'}).json())

print(post('http://localhost:8080/api/v2/news',
           json={'title': 'API test V2',
                 'content': 'Новость добавлена через API методом POST версия API 2',
                 'user_id': 1,
                 'is_private': True
                 }).json())