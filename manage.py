#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# # from HostTor import VicksTor
# import VicksTor as vix
# vix.run_server('flask')

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'helloworld.settings')
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


# python3 -m venv env
# env\Scripts\activate

# pip install --upgrade pip
# pip install -r requirements.txt

# python3 manage.py migrate
# python3 manage.py createsuperuser --username admin --email admin@mail.com

# python3 setup.py install
# python3 manage.py runserver

# http://127.0.0.1:8000
# http://127.0.0.1:8000/admin

# # Ctrl + C to exit 
# deactivate
