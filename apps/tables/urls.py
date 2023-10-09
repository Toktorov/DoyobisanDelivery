from django.urls import path 

from apps.tables.views import menu


urlpatterns = [
    path('<int:table_uuid>/', menu, name='menu')
]