# django celery task progress example
# start celery
```bash
celery -A core worker -l INFO --autoscale=5,0
```
# start app
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
