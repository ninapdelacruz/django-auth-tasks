# Generated by Django 3.2.8 on 2023-07-12 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='created_at',
            new_name='created',
        ),
    ]