from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=20, null=True)
    description = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='project/', null=False)

    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='project', null=True)

    create_at = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.pk} : {self.title}'
