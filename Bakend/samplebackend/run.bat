
@echo off

rem Activate the virtual environment
call C:\Users\Admin\anaconda3\Scripts\activate
call Conda activate venv
rem Run the Django development server
python manage.py makemigrations
python manage.py migrate
python .\manage.py runserver  192.168.1.8:8000
