# Generated by Django 4.1.3 on 2022-12-02 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_recipe_cooktime_alter_recipe_method_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/recipes'),
        ),
    ]