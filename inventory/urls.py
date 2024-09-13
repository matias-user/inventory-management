from django.urls import path
from . import views


app_name= "inventory"
urlpatterns = [
    path('', views.index, name='index' ),
    path('create/', views.createProduct, name='create-product' ),
]
