# Generated by Django 5.0 on 2023-12-04 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Город', 'verbose_name_plural': 'Города'},
        ),
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterModelOptions(
            name='offers',
            options={'verbose_name': 'Предложение', 'verbose_name_plural': 'Предложения'},
        ),
        migrations.AlterModelOptions(
            name='stars',
            options={'verbose_name': 'Звезда', 'verbose_name_plural': 'Звезды'},
        ),
    ]