cd ./proj
pip install -r requirements.txt
python manage.py makemigrations
python manage.py makemigrations dapp
python manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'password')" | python manage.py shell
python manage.py runserver