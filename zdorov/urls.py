from django.urls import path, re_path, register_converter
from zdorov.views import *
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('login/', login, name='login'),
    path('add-med/', add_medicine, name='add_medicine'),
    path('contact/', contact, name='contact'),

    path('cats/<int:cat_id>/', categories, name='cats_by_id'),
    path('cats/<slug:cat_slug>/', categories_by_slug, name='cats'),
    re_path(r'archive/(?P<year>20[0-9]{2})/', archive),
    re_path(r'archive/(?P<year>19[0-9]{2})/', archive),
    path('<year4:year>/', archive),


]
