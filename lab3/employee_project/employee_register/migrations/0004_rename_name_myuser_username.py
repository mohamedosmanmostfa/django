# Generated by Django 4.0.1 on 2022-02-01 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0003_myuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='name',
            new_name='username',
        ),
    ]
