from django.urls import path
from . import views


app_name= "inventory"
urlpatterns = [
    path('', views.listProduct, name=''),
    path('home/', views.listProduct, name='home' ),
    path('create/', views.createProduct, name='create' ),
    path('delete/<str:product>/', views.deleteProduct, name='delete')
]
