Установка зависимостей:
pip install -m req.txt

Запуск
python manage.py runserver

admin: admin
pass: admin12345

celery:  celery -A distribution worker -l info

celery beat: celery -A distribution beat -l info
