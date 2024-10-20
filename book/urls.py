from django.urls import path
from .views import (
    create,
    getAll,
    getByID
)

urlpatterns = [
    path('create', create, name='create'),
    path('<id>', getByID, name='book'),
    path('', getAll, name='books'),
]