from django.urls import path, include

urlpatterns = [
    path('user/', include("users.urls")),
    path('book/', include("book.urls")),
    path('reviews/', include("review.urls")),
]
