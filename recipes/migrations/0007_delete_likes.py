# Generated by Django 4.1.3 on 2022-12-10 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_likes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Likes',
        ),
    ]
