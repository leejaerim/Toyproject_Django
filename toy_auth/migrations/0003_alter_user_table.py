# Generated by Django 3.2.2 on 2021-06-22 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toy_auth', '0002_auto_20210622_0849'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='toy_auth_user',
        ),
    ]
