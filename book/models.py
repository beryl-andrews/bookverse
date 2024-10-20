from django.db import models
import uuid

class Book(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable= False)
    title = models.CharField(max_length = 225)
    author = models.CharField(max_length = 225)
    description = models.CharField(max_length = 225)
    genre = models.CharField(max_length = 225)
    release = models.DateField()

    def __str__(self):
        return Book.title


