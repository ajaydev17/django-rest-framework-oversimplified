from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_books),
    path('create/', views.post_book)
]