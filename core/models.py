from django.db import models

# Create your models here.
class Problems(models.Model):
    class Meta:
        verbose_name='Проблема'
        verbose_name_plural='Проблемы'


    name=models.CharField("Наименование",max_length=255)
    def __str__(self):
        return self.name

class PolEnum(models.IntegerChoices):
    MALE = 1, 'Мужской'
    FEMALE = 2, 'Женский'


class Status(models.Model):
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    name = models.CharField("Наименование", max_length=255)

    def __str__(self):
        return self.name

class Obrashenie(models.Model):
    class Meta:
        verbose_name='Обращение'
        verbose_name_plural='Обращения'

    data_vnesenia=models.DateTimeField("Дата внесения", auto_now_add=True)
    phone = models.CharField("Телефон", max_length=255)
    first_name = models.CharField("Фамилия", max_length=255)
    second_name = models.CharField("Имя", max_length=255)
    otchestvo = models.CharField("Отчество", max_length=255,null=True,blank=True)
    vozrast = models.IntegerField("Возраст",null=True,blank=True)
    pol = models.IntegerField("Пол",choices=PolEnum.choices,default=PolEnum.MALE)
    adress = models.CharField("Место жительства", max_length=255)
    opisanie = models.TextField("Описание проблемы",null=True,blank=True)
    status=models.ForeignKey(Status,verbose_name='Статус',on_delete=models.SET_NULL,null=True,blank=False,default=1)
    problems = models.ForeignKey(Problems, verbose_name='Проблемы', on_delete=models.SET_NULL, null=True, blank=False,default=1)

    def __str__(self):
        return f"{self.first_name} {self.second_name} {self.phone}"
