


Необходим api endpoint с jwt авторизацией (с проверкой поля isDoctor == true) в теле самого jwt-токена
JWT-токены необходимо подписывать с помощью секретного ключа (алгоритм HS256)
2) Данный API Endpoint должен вернуть список пациентов (3 штуки)
3) Данные пациента должны содержать 4 поля 
{
    id,
    date_of_birth (Дата рождения пациента),
    diagnoses (массив строк с названиями диагнозов),
    created_at (дата создания записи)
}
4) Код должен быть снабжён комментариями и README с инструкци
иями по поднятию сервера и отправке запросов
5) Код должен быть запушен в git-репозиторий (github, gitlab, bitbucket - любой на выбор). Желательно с коммитами по ходу написания кода
6) Завернуть в docker


### Как запустить
Копируем `.test.env в .env ` 
Собираем докер образ `docker-compose up --build`

Получаем токен доступа 
```
curl -X 'GET' \
  'http://127.0.0.1:10001/auth/?is_doctor=true' \
  -H 'accept: application/json'
  ```
Востановить бэкап базы если необходимо  
`dump.sql`
``````
Поулчаем список из 3 пациентов
```angular2html
curl -X 'GET' \
  'http://127.0.0.1:10001/patients/' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImRlZjQ4OTQ2LTMwMWQtNDk1Yi1iMmQ2LTgzYmQ3MWUyOTgzMCIsImlzX2RvY3RvciI6dHJ1ZSwic3ViIjoic2Vzc2lvbiIsIm5iZiI6MTY0NzQ1MzA0MywiaWF0IjoxNjQ3NDUzMDQzLCJleHAiOjE2NDc1Mzk0NDN9.9l2K94o7l5Te00QPcPnPwa3rIGplsAjob2jGLviwJ-g'
```