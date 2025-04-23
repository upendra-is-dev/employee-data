This project is a 3-hour challenge to build a Django-based web application that:
- Generates synthetic employee data
- Stores it in PostgreSQL
- Provides REST APIs for analytical summaries
- Visualizes key metrics via Swagger UI


Run command  to migrate data base 

python manage.py makemigrations
python manage.py migrate


Run command to seed dummy data  

python manage.py seed_data


Run command to start the server   

python manage.py runserver

default url to get token for authntication  is http://127.0.0.1:8000/api/token/

default url to swagger api is http://127.0.0.1:8000/swagger/



