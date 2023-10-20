## Курсовая работа по 8 модулю в онлайн школе SkyPro

#### Реализованы задачи:
* Для разных сервисов созданы отдельные контейнеры (django, postgresql, redis, celery).
* Всё оформлено в файле docker-compose и Dockerfiles.
* Проект готов на размещение на удаленном сервере:
  * можно запустить по инструкции, приложенной в Readme-файл
  * для запуска не требуется дополнительных настроек.

#### Перед запуском проекта, необходимо сделать следующие действия:
* Установить [Docker](https://www.docker.com/products/docker-desktop/) и docker-compose на свой ПК
* Создать файл .env для работы с переменными окружения

# Содержимое .env файла:
Для открытия всех портов:

    ALLOWED_HOSTS=* 
Можете менять язык по желанию, например en-en:

    LANGUAGE_CODE=ru-ru
Можете выбрать удобный для вас [часовой пояс](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

    TIME_ZONE=Europe/Moscow 
* Название базы данных postgres
* Пользователь postgres
* Пароль от базы данных postgres

      POSTGRES_DB=<DATABASES_NAME>
      POSTGRES_USER=<DATABASES_USER>
      POSTGRES_PASSWORD=<DATABASES_PASSWORD>
  
Для socker-compose 

    DATABASES_HOST=db 
Необходимо получить api-ключ от [телеграм бота](https://t.me/BotFather)

    TG_API_KEY=<TG_API_KEY>
Настройка celery:
    
    CELERY=redis://redis:6379

## Запуск проекта:
    git clone git@github.com:Kusto7/atomic_habits.git
    cd atomic_habits
    docker-compose build
    docker-compose up
