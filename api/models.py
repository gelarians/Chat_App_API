from django.db import models

class chat(models.Model):
    username = models.CharField(max_length=30)
    massage = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
