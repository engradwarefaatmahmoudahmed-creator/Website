web: python manage.py migrate && python manage.py loaddata core_data.json && python manage.py collectstatic --noinput && gunicorn service_course.wsgi:application 
