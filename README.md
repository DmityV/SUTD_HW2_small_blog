### О проекте:

Проект блога сделан в рамках 3-го домашнего задания.
Для удобcтва проверки в состав проекта включена база данных с примерами постов из блога.

### Как запустить проект:

Клонировать репозиторий и перейти в него, выполнив следующие команды в командной строке:

```
git clone https://github.com/DmityV/SUTD_HW3_small_blog.git
```

```
cd small_blog
```

Далее в командной строке:

создать и активировать виртуальное окружение:

Windows
```
python -m venv venv
source venv/Scripts/activate
```
Linux/macOS
```
python3 -m venv venv
source venv/bin/activate
```

обновить PIP

Windows
```
python -m pip install --upgrade pip
```
Linux/macOS
```
python3 -m pip install --upgrade pip
```

установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

выполнить миграции:

Windows
```
python manage.py makemigrations
python manage.py migrate
```

Linux/macOS
```
python3 manage.py makemigrations
python3 manage.py migrate
```

запустить проект:

Windows
```
python manage.py runserver
```

Linux/macOS
```
python3 manage.py runserver
```