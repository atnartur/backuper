# Backuper

Утилита для создания бекапов. Это ядро приложения, которое содержит в себе адаптеры помогает запускать задачи.
Конфигурации задач хранятся в формате yml. Код задач описывается на языке Python 3.

Пример конфигурации, кода задачи и docker-compose файл для запуска находятся в папке `tasks_examples`.

## Доступные адаптеры:

- `ssh` - подключение по ssh 
- `task_config` - погрузка конфигураций
- `temp` - создание и очистка временной папки
- `uploader` - загрузка в Яндекс.Диск

## Запуск

- `python app.py` - запуск приложения
- `python app.py TASKNAME` - запуск только задачи TASKNAME
 
## Получение токена Яндекс.Диска

Загрузка файлов происходит через официальный клиент [ydcmd](https://github.com/abbat/ydcmd).
Авторизация в этом клиенте работает через токены. Ниже описан процесс получения этого токена.

- Авторизоваться в необходимом аккаунте Яндекса
- Войти в контейнер (`docker run -ti --rm atnartur/backuper:latest bash`)
- Выполнить: `ydcmd token`
- Открыть ссылку, которая вышла в программе
- Получить код авторизации, выполнить: `ydcmd token КОД_АВТОРИЗАЦИИ`
- Выведенный OAuth токен вписать в значение переменной среды `YADISK_TOKEN`
(пример запуска через `docker-compose` находится в папке `tasks_examples`)

## Docker

- `docker build -t atnartur/backuper:latest .` - сборка
- `docker push atnartur/backuper:latest` - отправка в Docker Registry

## Авторы

&copy; 2017-2018 [Артур Атнагулов](http://i.atnartur.ru) & [Евгений Жуковец](https://vk.com/id48582913)