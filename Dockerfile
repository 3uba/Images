# should work 
FROM python:3.9
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
RUN mkdir /proj
WORKDIR /proj
COPY requirements.txt /proj/
RUN pip install -r requirements.txt
COPY . /proj/
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'password')" | python manage.py shell
RUN python manage.py runserver