from django.urls import path
from . import views

urlpatterns = [
    # task4/urls.py
    path('', views.platform_view, name='platform'),
    path('games/', views.game_list_view, name='games'),
    path('cart/', views.cart_view, name='cart'),
    # task5/urls.py
    path('django_sign_up/', views.sign_up_by_django, name='sign_up_by_django'),
]
