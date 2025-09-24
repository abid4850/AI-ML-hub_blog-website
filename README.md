    AI & ML Hub - Minimal Django skeleton


    Instructions:

1. Create & activate a virtualenv
   python -m venv .venv
   source .venv/Scripts/activate  # windows
   source venv/bin/activate # linux/mac

2. Install requirements
   pip install -r requirements.txt

3. Run migrations & create superuser
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser

4. Run server
   python manage.py runserver

Open http://127.0.0.1:8000/ in your browser.
