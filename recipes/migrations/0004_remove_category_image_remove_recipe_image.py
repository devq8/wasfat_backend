# Generated by Django 4.1.3 on 2022-12-01 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_ingredient_rename_name_category_title_category_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='image',
        ),
    ]