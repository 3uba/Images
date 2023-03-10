Projekt `Images`

Możliwość uruchomienia aplikacji przez Dockera (na oko pisałem),
jeżeli jednak niechcesz uruchamiać aplikacji przez Dockera
można uruchomić skrypt run.sh w głównym folderze pliku, <u>on powinnien</u>
zainstalować wszystkie potrzebne zależności, ustawić administratora, i uruchomić aplikacje

Jeżeli jednak opcja która wybrałeś/aś nie działa,
podaje komendy podtrzebne do uruchomienia aplikacji:

W głównym folderze:

`pip install -r requirements.txt`

Przejdź do folderu proj, (ROOT_FOLDER/proj) i wykonaj te komendy:

`python manage.py makemigrations`

(w przypadku nie działania poprawnego aplikacji `python manage.py makemigrations dapp`)

`python manage.py migrate`

`python manage.py createsuperuser.py`

i w tym miejscu należy stworzyć super użytkownika aby móc sie zalogować na konto administratora

`python manage.py runserver`

i koniec aplikacja powinna działać na localhoscie port 8000