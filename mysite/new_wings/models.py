from django.db import models
from django.core.exceptions import ValidationError


def validate_only_two_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.id != model.objects.get().id):
        raise ValidationError("перед тим як додати новы данні видаліть вже додані ")
class Slider(models.Model):
    screen = models.ImageField(blank=True, null=True, upload_to='image')
class PersonalDate(models.Model):
    full_name = models.CharField(verbose_name='Повне імя',max_length=100)
    age = models.CharField(verbose_name='Вік',max_length=50)
    city = models.CharField(verbose_name='Місце проживання ',max_length=100)
    profesion = models.CharField(verbose_name='Професія', max_length=100)
    problem  = models.CharField(verbose_name='Проблема що торбує',max_length=220)
    reabilitations_type = models.CharField(verbose_name='Нещодавно проведена реабілітація',max_length=220, blank=True)
    diseases = models.TextField(verbose_name='Травми,операції хронологічні захворювання', max_length=500,null=True)

    def __str__(self):
        return 'full_name' .format(self.id)

