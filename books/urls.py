from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BooksList.as_view()),
    path('books/<int:id>', views.BookDetails.as_view())
]
