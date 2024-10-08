from django.urls import path, include
# from django.contrib.auth import views as auth_views
from . import views


app_name= "inventory"
urlpatterns = [
    path('', views.redirectHome),
    path('home/', views.listProduct, name='home' ),
    path('home/<str:characteristic>/', views.orderProducts, name='home-ordered' ),
    # re_path('', views.filterProducts, name='filter_products' ),
    path('create/', views.createProduct, name='create' ),
    path('delete/<str:product_id>/', views.deleteProduct, name='delete'),
    path('edit/<str:product_id>/', views.editProduct, name='edit' ),
    path('register/', views.register, name='register' ),
    path('accounts/', include('django.contrib.auth.urls'))
]
    