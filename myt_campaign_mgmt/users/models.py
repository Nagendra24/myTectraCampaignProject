from django.db import models
from django.core.validators import RegexValidator

class GroupModelClass(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(models.TextField,max_length=100)
    groups = models.CharField(max_length=250)
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'group_details'


class UserModelClass(models.Model):
    email = models.EmailField(max_length=50,unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{10,10}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
    mobile_number = models.CharField(validators=[phone_regex], max_length=10, blank=False,unique=True)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    group = models.ForeignKey(GroupModelClass,on_delete=models.PROTECT)
    selectedGroup = models.CharField(max_length=50)

    def _str_(self):
        return self.user_name

    class Meta:
        db_table = 'user_details'