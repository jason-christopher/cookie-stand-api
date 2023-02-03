# LAB - Class 34

## Project: Cookie Stand API

### Author: Jason Christopher

### Links and Resources

* Django Rest Framework
* PostgreSQL
* ElephantSQL
* Docker
* [Code Fellows API QuickStart](https://github.com/codefellows/python-401-api-quickstart)

### Setup

* Clone down repo to local machine.
* Create and activate a virtual environment.
* Run `pip install -r requirements.txt`.
* Add `.env` file in the `project` directory with follpwing info:

    ```
    SECRET_KEY=GRnf-twOp7YzBEsKtV8ED-ef3FZlI4c1W6wjuuhdQuw
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0
    #ALLOW_ALL_ORIGINS=True

    DATABASE_ENGINE=django.db.backends.postgresql
    DATABASE_NAME=ksowkauw
    DATABASE_USER=ksowkauw
    DATABASE_PASSWORD=fjkNOyew97RhTvHWQdgr7Am_ueBGU6cO
    DATABASE_HOST=fanny.db.elephantsql.com
    DATABASE_PORT=5432
    ```

* In one tab of your terminal, run `docker compose up`.
* In a ***different*** terminal tab, run `docker compose run web bash` and then `python manage.py runserver`.
* Now you can go `/cookie_stands/` to see the app's home page.
* You won't able to access the database information without logging in. In the URL, add `/admin` and log in with:
  * Username: `admin`
  * Password: `12345`
* You can also go `/api/v1/cookie_stands/` to access, create, update, and delete homes in the database.

### Tests

* ***When testing, make sure to NOT use PostgreSQL. COmment out the `.env` DATABASE fields to run tests***
* Run `python manage.py test` to run tests.
* ***Remember to un-comment out the DATABASE fields in the `.env` file when done with testing***.

### Notes

* Django `environ` allows you to read environment variables.
* Add `.env` file in the `project` folder and add all of `.env.sample` content except `ALLOW_ALL_ORIGINS` (can comment out).
  * Run `python -c "import secrets; print(secrets.token_urlsafe())"` and add to `SECRET_KEY` in `.env` file.
  * Run `python manage.py makemigrations` and `python manage.py migrate` inside VENV.
* Create superuser inside VENV.
* Run `python manage.py startapp cookie_stands` to create `cookie_stands` app.
  * Add to `APPS` in `settings.py`, and register in app's `admin.py`.
* After signing in and creating a project in ElephantSQL, grab:
  * User & Default database -> DATABASE_NAME & DATABASE_USER
  * Password -> DATABASE_PASSWORD
  * Server -> DATABASE_HOST
* Run `pip install psycopg2-binary` and `pip freeze > requirements.txt` inside VENV.
* Delete `0001_initial.py` migrations in the `things` app in `migrations` directory (you can delete the entire `things` app later once you've copied the important info from the files).
* Run `migrate` inside VENV because of the new database.
* Run `python manage.py createsuperuser` to create a new super-user for ElephantSQL.
* Remove `Things` from the database by unregistering `things` app my commenting out in the `things` app's `admin.py` file.
* Add `urls.py`, `serializers.py`, `permissions.py` `urls_front.py`, and `views_front.py` files in `cookie_stands` directory.
* In project's `urls.py` file replace `things` path with `path("api/v1/cookie_stands/", include("cookie_stands.urls")),` and `path("cookie_stands/", include("cookie_stands.urls_front")),`.
* Update `cookie_stand` app's `urls.py`, `serializers.py`, `permissions.py` `urls_front.py`, and `views_front.py` files using data from `things` app.
* Update `base.html` file and replace `thing` with `cookie_stand` for the List and Create options.
* Create a `cookie_stands` directory in `templates` and add HTML files for each item in the app's `views_front.py` file.
* Update each of the HTML files with the required info.
* In the app's `views_front.py` file, add `context_object_name = "cookie_stand"` to each class and add `success_url = reverse_lazy("cookie_stand_list")` to the required classes.
* Make sure the app's `models.py` file has this at the bottom:

    ```python
    def get_absolute_url(self):
        return reverse('cookie_stand_detail', args=[str(self.id)])
    ```
