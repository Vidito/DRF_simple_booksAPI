from django.urls import path
from .views import BookList, BookCreate, BookDetail
urlpatterns = [
    path('', BookCreate.as_view()),
    path('list/', BookList.as_view()),
    path('<int:pk>/', BookDetail.as_view()),
]