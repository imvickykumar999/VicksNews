#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


rf'''
python -m venv env
env\Scripts\activate

env\Scripts\python.exe -m pip install --upgrade pip
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser --username imvickykumar999 --email imvickykumar999@gmail.com

python manage.py runserver

http://127.0.0.1:8000
http://127.0.0.1:8000/admin

# Ctrl + C to exit 
deactivate
'''
