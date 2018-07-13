from django.db import models

# Create your models here.

class GroupModelClass(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(models.TextField,max_length=100)
    groups = models.CharField(max_length=250)
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'group_details'
