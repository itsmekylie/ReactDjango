# Generated by Django 5.2 on 2025-04-04 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Todo',
        ),
    ]
