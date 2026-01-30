# Проект hitalent-API
Тестовое задание на направление hitalent python-backend от Никиты Рушковского.
## Ручной деплой на персональный компьютер
* Клонируем репозиторий в текущую рабочую директорию.
```commandline
git clone git@github.com:Seamly71/hitalent-API.git
```
* Заполняем переменные окружения.
В репозитории есть шаблонный файл с необходимыми переменными окружения: template.env.
Значения переменных в нем необходимо записать, а затем переименовать в .env.
```commandline
mv template.env .env
```
* При отсутствии оных необходимо установить Docker.
```commandline
sudo apt update
sudo apt install curl
curl -fSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh
 
```
И Docker compose.
```commandline
sudo apt install docker-compose-plugin
```
* Запускаем проект.
```commandline
sudo docker compose -f docker-compose.yml up
```
* Применяем миграции.
```commandline
sudo docker compose -f docker-compose.yml exec backend sh python manage.py migrate
```
* Проект доступен в сети устройства на 1111м порту.
```
localhost:1111
```
## Примеры запросов к API
```
POST /chats/: {
  "title": "Shadow wizard money gang"
}

201: {
  "id": 1,
  "title": "Shadow wizard money gang",
  "created_at": "2019-07-14T11:32:22Z"
}
```
```
POST /chats/1/messages/: {
  "text": "Wazzup!"
}

201: {
    "id": 1,
    "chat_id": 1,
    "text": "Wazzup!",
    "created_at": "2019-07-14T11:32:22Z"
}
```
## Структура проекта
* API задокументирован по стандарту OpenAPI 3.0.2.
Документация доступна в docs/openapi.
* Проект покрыт юнит тестами DRF TestCase.
```commandline
docker compose -f docker-compose.yml exec backend python manage.py test -v 3
```

## Автор
Никита Seamly71 Рушковский
