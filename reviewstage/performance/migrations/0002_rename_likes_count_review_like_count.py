# Generated by Django 4.2.11 on 2024-04-18 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='likes_count',
            new_name='like_count',
        ),
    ]
