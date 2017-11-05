from django.db import models

class MyPost(models.Model):
    title=models.CharField()
    body=models.TextField()
    date=models.DateTimeField()

    def _str_(self):
        return self.title