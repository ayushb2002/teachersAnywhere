# Generated by Django 3.1 on 2020-08-24 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0012_auto_20200823_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='teacher_type',
            field=models.CharField(blank=True, choices=[('Home Tutor', 'HT'), ('Tution Center Teacher', 'TT')], max_length=30),
        ),
    ]
