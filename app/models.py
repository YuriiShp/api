from django.db import models


# Create your models here.
class Report(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    readings = models.JSONField()
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title) + ' by ' + str(self.author)


class Author(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title) + ' by: ' + str(self.author)

