from django.urls import path, re_path
from . views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "housing"

urlpatterns = [
    path( '', homepage , name = "index"),
    path('property_list', PropertyListView.as_view(), name = 'property_list'),
    path('about_us', about_us, name = 'about_us'),
    path('invest', invest, name = 'invest'),
    path('contact', contact, name = 'contact'),
    path('contact_validate', contact_validate, name ="contact_validate")

]
