from django.urls.resolvers import URLPattern
from genesis_proj import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_prod, name='product'),
    path('<int:pk>/update/', views.prod_update, name='product_update'),
    path('add/', views.prod_add, name='product_add'),
]