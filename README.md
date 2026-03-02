# Django

`uv add Django`

```
django-admin startproject myProjectName # first time only
python manage.py runserver # start server at 8000 port and create a db.sqlite3



```

# Request Flow

Client ---> Req ---> django ---> UrlResolver ---> urls.py ---> [urls.py, urls.py ,...]
----> views.py with/without helps of  models.py ---> with/without help of templates ----> response ---> django ---> client

Basic Views
```python
# views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World. You are at HRM world.")

def about(request):
    return HttpResponse("You are at ABOUT PAGE.")

def contact(request):
    return HttpResponse("You are at CONTACT PAGE.")
```

`urls.py`
```python
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about/', views.about, name='about'), # name is optinal but recommeded
    path('contact/', views.contact),
]
```


# Lets learn more
Start with adding `templates`
in root directory ---> `static and `templates` folder

insited of `django.http` --> `HttpResponse`
we will use `django.shortcuts` --> `render`    return render(request, 'myhtmlfile.html')

in `settings.py` ---> `TEMPLATES` ---> `DIRS` ---> ['templates']

# Lets add css from static

```
in static --> style.css

body {
    background-color: ;
    color: ;
}
```

in index.html
at top ---> {% load static %}
<link rel="stylesheet" href="{% static 'style.css' %}">

in settings.py
import os
STATIC_URL = 'static/' # after this line
STATICFILES_DIRS =  [os.path.join(BASE_DIR, 'static')]

```
