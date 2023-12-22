django: daphne core.asgi:application -b 0.0.0.0 -p 8000
celery: celery -A core worker -B -E -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
flower: celery -A core flower
