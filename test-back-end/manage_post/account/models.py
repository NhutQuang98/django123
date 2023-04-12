from django.db import models

class AccountModels(models.Model):
    account_id = models.AutoField(primary_key=True, db_column='account_id')
    user_name = models.CharField(db_column='user_name')
    password = models.CharField(db_column='password')
    name = models.CharField(db_column='name')
    birth_date = models.DateField(db_column='birth_date')
    phone_number = models.CharField(db_column='phone_number')
    email = models.EmailField(db_column='email')
    create_date = models.DateTimeField(auto_now_add=True, db_column='create_date')
    update_date = models.DateTimeField(auto_now=True, db_column='update_date')

    def __str__(self):
        return self