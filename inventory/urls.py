from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('', views.InventoryList.as_view(), name='inventory-list'),
    path('<int:pk>/', views.InventoryDetail.as_view(), name='inventory-detail'),
]