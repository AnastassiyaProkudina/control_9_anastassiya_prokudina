# Введение
### Эта документация поможет вам ознакомиться с ресурсами Gallery API и покажет, как выполнять различные запросы, чтобы вы могли извлечь из этого максимальную пользу.

## Rest
**На данный момент доступен один ресурс:** 
<br>
favorites: используется для получения всех избранных фото.
<br>


## избранные фото

Схема избранных фото


| **Ключ** | **Тип** | **Описание**                     |
|----------|---------|----------------------------------|
| id       | int     | Идентификатор записи в избранное |     
| author   | int     | Идентификатор Автора             |
| photo    | int     | Идентификатор Фото               |

## Получить все избранное
Вы можете получить доступ к списку избранных фото, используя: http://127.0.0.1:8000/api/favorites/

## Получить одну запись из избранного
Вы можете получить запись из избранного, добавив id в качестве параметра: http://127.0.0.1:8000/favorites/1
используя метод DELETE можно удалить запись
используя метод POST можно добавить запись
метод PUT не используется


---
for  superuser admin:
<br>username: admin
<br>Password: admin
<hr>
for  users:
<br>John
<br>Password: A123456a
<hr>
