from django.db import models


class User(models.Model):
    uid = models.IntegerField("ТелеграмАйди")
    status = models.CharField("Статус юзера", max_length=20)

    def __str__(self):
        return self.uid

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Category(models.Model):
    category_title = models.CharField("Название категории (отображается юзеру в боте в разделе с выбором категории)", max_length=50)
    category_id = models.CharField("Айди категории (придумай короткое название (оно не отображается юзеру) для более удобного добавления товаров в админке. Может совпадать с первым параметром (отображаемым названием)", max_length=100)

    def __str__(self):
        return self.category_title


    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Item(models.Model):
    item_title = models.CharField("Название товара", max_length=30)
    item_category = models.CharField("Категория товара (вводить короткое название категории, указанное в разделе с категориями)", max_length=100)
    item_price = models.IntegerField("Цена товара в рублях (только целые числа)")

    def __str__(self):
        return self.item_title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
