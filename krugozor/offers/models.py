from django.db import models


class Offers(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    work_time = models.CharField(max_length=150, verbose_name='Время работы')
    phone_num = models.CharField(max_length=11, verbose_name='Номер телефона')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    description = models.TextField(verbose_name='Описание')
    map_link = models.TextField(verbose_name='Ссылка на карту')
    picture = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изображение')
    city = models.ForeignKey('City', on_delete=models.PROTECT, verbose_name='Город')


class Feedback(models.Model):
    stars = models.ForeignKey('Stars', on_delete=models.PROTECT, verbose_name='Звезда')
    content = models.TextField(verbose_name='Контент')
    id_offer = models.CharField(max_length=150, verbose_name='ID предложения')


class City(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')


class Stars(models.Model):
    title = models.CharField(max_length=1, verbose_name='Звезда')
