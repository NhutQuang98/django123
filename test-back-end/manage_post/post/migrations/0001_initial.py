# Generated by Django 4.2 on 2023-04-12 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostModels',
            fields=[
                ('post_id', models.AutoField(db_column='post_id', primary_key=True, serialize=False)),
                ('title', models.CharField(db_column='title')),
                ('content', models.TextField(db_column='content')),
                ('amount_view', models.IntegerField(db_column='amount_view', default=0)),
                ('submit_date', models.DateTimeField(auto_now_add=True, db_column='submit_date')),
                ('update_last_date', models.DateTimeField(auto_now=True, db_column='update_last_date')),
                ('account_id', models.ForeignKey(db_column='account_id', on_delete=django.db.models.deletion.CASCADE, to='account.accountmodels')),
                ('category_id', models.ForeignKey(db_column='category_id', on_delete=django.db.models.deletion.CASCADE, to='category.categorymodels')),
            ],
        ),
    ]
