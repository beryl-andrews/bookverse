from django.urls import path
from .views import (
   create,
   getReviewByBookID,
   getReviewByUserID
)

urlpatterns = [
    path('create', create, name='create'),
    path('book/<book_id>', getReviewByBookID, name='fetch by book'),
    path('user/<user_id>', getReviewByUserID, name='fetch by user'),
]