# Generated by Django 3.1 on 2020-08-23 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_auto_20200822_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(upload_to='media'),
        ),
    ]