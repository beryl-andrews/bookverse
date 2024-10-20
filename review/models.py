import uuid
from django.db import models


class Review(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable= False)
    user_id = models.ForeignKey('users.User', on_delete=models.CASCADE)
    book_id = models.ForeignKey('book.Book', on_delete=models.CASCADE)
    title = models.CharField(max_length= 225)
    content =models.TextField()
    rating = models.IntegerField()
    created_on = models.DateField(auto_now_add=True)


    def __str__(self):
        return Review.id