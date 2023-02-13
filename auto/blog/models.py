from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


class Car(models.Model):
    title = models.CharField(max_length=200, verbose_name='Модель')
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name='URL')
    birthday = models.PositiveSmallIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2100)],
                                                blank=True, verbose_name='Год выпуска')
    description = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/car/', blank=True, verbose_name='Фото')
    published = models.DateTimeField(auto_now=True, verbose_name='Добавлено')
    brd = models.ForeignKey('Brand', on_delete=models.CASCADE, verbose_name='Марка/Бренд')
    carcl = models.ForeignKey('CarClass', on_delete=models.CASCADE, verbose_name='Класс автомобиля')
    btype = models.ForeignKey('BodyType', on_delete=models.CASCADE, verbose_name='Тип кузова')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('car', kwargs={'car_slug': self.slug})

    class Meta:
        verbose_name = 'Автомобили'
        verbose_name_plural = 'Автомобили'

class Specification(models.Model):
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name='URL')
    max_speed = models.PositiveSmallIntegerField(validators=[MinValueValidator(100), MaxValueValidator(1000)])
    engine_power = models.CharField(max_length=50)
    drive_unit = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    doors = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    сr = models.ForeignKey('Car', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Технические характеристики'
        verbose_name_plural = 'Технические характеристики'
    
    
class Brand(models.Model):
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name='URL')
    title = models.CharField(max_length=100, verbose_name='Марка/Бренд')
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/brands/', blank=True, verbose_name='Фото')
    countr = models.ForeignKey('Country', on_delete=models.CASCADE, verbose_name='Страна')

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse('brands', kwargs={'brands_slug': self.slug})


    class Meta:
        verbose_name = 'Автомобильные бренды'
        verbose_name_plural = 'Автомобильные бренды'


class Country(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/countries/', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страны'
        verbose_name_plural = 'Страны'


class CarClass(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Классы автомобилей'
        verbose_name_plural = 'Классы автомобилей'
    

class BodyType(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Типы кузова'
        verbose_name_plural = 'Типы кузова'




