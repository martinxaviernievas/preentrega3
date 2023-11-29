from django.urls import path
from .views import index, add_categoria

urlpatterns = [
    path('', index, name='index'),
    path('add_categoria/', add_categoria, name='add_categoria'),
    # Agrega más URLs según tus necesidades
]