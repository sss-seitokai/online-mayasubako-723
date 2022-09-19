from unicodedata import name
from django.db.models.query import NamedValuesListIterable
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import include
app_name = 'meyasubako'
urlpatterns = [
  path('',views.index,name='index'),
  path('detail/<int:opinion_id>',views.detail,name='detail'),
  path('form',views.form,name='form'),
  path('owner',views.owner,name='owner'),
  path('answer/<int:opinion_id>',views.answer,name='answer'),
  path('owner_detail/<int:opinion_id>',views.owner_detail,name='owner_detail'),
  path('edit/<int:timeline_id>',views.edit,name='edit'),
  path('delete/<int:timeline_id>',views.delete,name='delete'),
  path('promise',views.promise,name='promise'),

]
