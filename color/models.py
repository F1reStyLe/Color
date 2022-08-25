from django.db import models
from django.urls import reverse


class RalGroup(models.Model):
    """Цветовая группа"""
    name = models.SmallIntegerField("RAL group")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Цветовую группу'
        verbose_name_plural = 'Цветовые группы'
        ordering = ['name']


class ApplicationMethod(models.Model):
    """Метод нанесения"""
    method = models.CharField("Метод нанесения", max_length=150)

    def __str__(self):
        return self.method

    class Meta:
        verbose_name = 'Метод нанесения'
        verbose_name_plural = 'Методы нанесения'


class Conditions(models.Model):
    """Условия"""
    place = models.CharField("Условия", max_length=150)

    def __str__(self):
        return self.place

    class Meta:
        verbose_name = 'Условие'
        verbose_name_plural = 'Условия'


class Product(models.Model):
    """Описание продукта"""
    name = models.CharField("Наименование", max_length=150, db_index=True)
    ral = models.CharField("RAL", max_length=50)
    batch = models.SmallIntegerField("Номер партии №", unique=True)
    consumer = models.CharField("Потребитель", max_length=150)
    qr = models.ImageField("QR", upload_to='QR/%Y/%m/%d/', blank=True)
    note = models.TextField("Описание", blank=True)
    created_at = models.DateTimeField("Время создания", auto_now=True)
    is_published = models.BooleanField("Опубликовано", default=True)

    def get_absolute_url(self):
        return reverse('view_products', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.name} RAL {self.ral}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-created_at']


class Sample(models.Model):
    """Образец"""
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    application_method = models.ForeignKey(ApplicationMethod, on_delete=models.CASCADE, verbose_name='Метод нанесения')
    ral_group = models.ForeignKey(RalGroup, on_delete=models.CASCADE, verbose_name='Цветовая группа')
    conditions = models.ForeignKey(Conditions, on_delete=models.CASCADE, verbose_name='Условие')
    created_at = models.DateTimeField(auto_now=True)
    note = models.TextField("Описание", blank=True)
    delta_L = models.FloatField("L", default=0)
    delta_a = models.FloatField("a", default=0)
    delta_b = models.FloatField("b", default=0)
    delta_E = models.FloatField("E", default=0)
    L = models.FloatField("*L", default=0)
    a = models.FloatField("*a", default=0)
    b = models.FloatField("*b", default=0)

    def get_absolute_url(self):
        return reverse('view_samples', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.product_id.name} {self.product_id.ral}'

    class Meta:
        verbose_name = 'Образец'
        verbose_name_plural = 'Образцы'
        ordering = ['-created_at']