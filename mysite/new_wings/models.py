from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator


class Slider(models.Model):
    name = models.CharField(blank=True, max_length=50)
    screen = models.ImageField(blank=True, null=True, upload_to='image')

    class Meta:
        verbose_name_plural = "Слайдер"

    def __str__(self):
        return 'Cлайд'.format(self.id)



class Information(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to='image')
    text = models.CharField(max_length=500)
    class Meta:
        verbose_name_plural = "Про нас"
    def __str__(self):
        return 'Про нас'.format(self.id)


class Contact(models.Model):
    phone = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)

    class Meta:
        verbose_name_plural = "Контактні дані"

class Social(models.Model):
    link = models.URLField(max_length=200)
    icon = models.ImageField(blank=False, null=True, upload_to='image')

    class Meta:
        verbose_name_plural = "Соціальні мережі"


class Reabil(models.Model):
    title = models.CharField(max_length=150,help_text="Ведіть назву процедури",null=True)
    text = models.TextField(max_length=1000,help_text="Ведіть опис процедури" )
    image = models.ImageField(blank=True, null=True, upload_to='image')

    class Meta:
        verbose_name_plural = "Реабілітація"


class Donate(models.Model):
    account = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Реквізити"


class Sponsor(models.Model):
    logo = models.ImageField(blank=True, null=True, upload_to='image')

    class Meta:
        verbose_name_plural = "Спонсори"


class New(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    images = models.ImageField(blank=False, null=True, upload_to='image/' )
    text = models.TextField("Опис")
    created = models.DateTimeField("Дата створення", auto_now_add=True)

    keywords = models.CharField("Ключові слова", max_length=50)

    def __str__(self):
        return self.title


class Suport(models.Model):
    full_name = models.CharField("Прізвище Ім'я По батькові", max_length=150)
    age = models.IntegerField("ваш вік", default=1,
                              validators=[MaxValueValidator(10), MinValueValidator(1)])
    city = models.TextField("Місце проживання", max_length=200)
    problem = models.TextField("Проблема що торбує")
    live_through = models.TextField("Перенесині травми,операції а також наяві захворювання:  ", max_length=200)
    recent_treatment = models.CharField(max_length=200)
    reabil_type = models.CharField("Вид реабілітації", max_length=100, )
    exemption = models.BooleanField("Наявність пільг", )

    class Meta:
        verbose_name_plural = "Зворотний зв'язок"
    def __str__(self):
        return self.full_name
