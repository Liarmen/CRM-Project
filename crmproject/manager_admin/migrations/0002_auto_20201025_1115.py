# Generated by Django 3.1.1 on 2020-10-25 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email address'),
        ),
    ]
