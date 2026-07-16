Создание Django-приложения:

- создал интепретатор python
- создал файл readme.md
- создал файл requirements.txt
- создал django-приложение
- создал файл .gitignore
- настроил manage.py runserver
- установил необходимые библиотеки
- asgiref, Django, ipython, pillow
- psycopg2-binary, sqlparse, tzdata
- после запуска появится db.sqlite3 
- staticfiles_dirs = (base_dir / 'static',)
- language_code = "ru-ru"
- time_zone = "Europe/Moscow"


Создание приложения catalog:

- static(settings.MEDIA_URL, 
- document_root=settings.MEDIA_ROOT)
- media_url = '/media/' 
- media_root = base_dir / 'media'
- python manage.py startapp catalog
- config - settings - installed apps
- urls - app_name = CatalogConfig.name
- urlpatterns = path('', index, name='index'), 
- path('contact/', contact, name='contact'),
- views - def index(requests): 
- context = {'title': 'Главная' } 
- return render(requests, 'catalog/index.html', context)
- def contact(requests): context = 
- {'title': 'Контакты' } if requests.method == 'POST':
- name = requests.POST.get('name')
- email = requests.POST.get('email')
- message = requests.POST.get('message')
- print(f'{name} ({email}):{message}')
- return render(requests, 'catalog/contacts.html', context)
- создал папку templates - catalog
- добавил index.html, contacts.html
- {% load static %}
- <link href="{% static 'css/bootstrap.min.css' %}" rel="stylesheet">
- <link href="{% static 'css/album.css' %}" rel="stylesheet">
- <script src="{% static 'js/popper.min.js' %}"></script>
- <script src="{% static 'js/bootstrap.min.js' %}"></script>
- <script src="{% static 'js/holder.min.js' %}"></script>
- создал файл static - css - js, media
- css - bootstrap.min.css - album.css
- js - popper.min.js - holder.min.js - bootstrap.min.js
- {% load static %} - <!doctype html> - <head> - <body> 
- <main role="main"> - </main> - <div class="container">
- <div class="row text-start"> - <div class="row">
- {% for object in object_list %}
- <img src="{{ object.image.url }}" width="350" height="250"/>
- <p class="card-text"> - {% if object.is_active %} 
- {{ object|title }} - {% else %} - </p> - </div> - </div> - </div>
- {% endfor %} - </div> - </div> - </div>
- <!-- inc_footer_menu --> - <!-- inc_footer_menu -->
- <!-- inc_scripts_menu --> - <!-- inc_scripts_menu -->


Создание базу данных в приложении:

- настраиваем в config databases
- engine, name, user, password, host, port
- psql -U postgres входим в базу данных
- create database dandan; \q
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser
- http-127.0.0.1:8000/admin
- создаю модель, лучше копировать с другого проекта
- python manage.py makemigrations
- python manage.py migrate
- заполняем данные в админку и запускаем проект 
- @admin.register(Category) - class CategoryAdmin(admin.ModelAdmin):
- list_display = ('id', 'name',)
- list_filter = ('name',) 
- search_fields = ('name',)
- @admin.register(Product) - class ProductAdmin(admin.ModelAdmin):
- list_display = ('id', 'name', 'price', 'category',)
- list_filter = ('category',) - search_fields = ('name', 'description',)
- apps.py - verbose_name = 'Каталог'
- http-127.0.0.1:8000/admin


Создание проект на github:

- захожу на сайт https-github.com/danielrusky
- создаю репозиторий на гитхаб
- прописываю код внутри проекта на pycharm
- git init - git remote add origin
- 