## Фотоальбом slider на Django.

## Технологии:

Backend: Django: 4.1, Python: 3.9; 
База данных: MySQL;
Frontend: HTML/CSS/JS, Boxicons, slick, Bootstrap5.

*Изначально был установлен Django 4.1, в ходе разработки при установке django-filer версия Django была обновлена до версии из req.txt. 

## Описание функциональности

1. Интуитивно понятно настроена админская часть, удобно работать с объектами фото.
2. Для картинок модели слайдера использован пакет  django-filer - через него происходит загрузка картинок.
3. Записи слайдера в админке можно сортировать по принципу "drag&drop" использован пакет django-admin-sortable2
4. Реализована возможность просматривать альбом с картинками в режиме слайдера по endpoint: base/
5. Slider реализован с помощью https://kenwheeler.github.io/slick/
6. Главную картинку можно открыть и листать все картинки галерии. 

# Фото приложения
1. ![image](https://github.com/user-attachments/assets/0dc55a04-3e77-4315-8026-b355898446e7)
2. ![image](https://github.com/user-attachments/assets/d0ccd409-f0ae-4d7e-8f4a-3e0a095c7006)


## Установка
1. Клонируйте репозиторий;
2. Перейдите в папку проекта;
3. Установите зависимости: pip install -r requirements.txt ;
4. Настройте базу данных в файле settings.py;
5. Выполните миграции: py manage.py makemigrations > python manage.py migrate;
6. Запустите сервер: py manage.py runserver.

## Настройка окружения
Убедитесь, что у вас установлен Python версии [3.9].

## Лицензия
Проект распространяется под лицензией MIT.

## Контакты
Разработчик: Артур Сахаров Telegram: grizz_dev


   
