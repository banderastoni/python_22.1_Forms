from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(verbose_name='Изображение', upload_to='img/', **NULLABLE)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Цена', **NULLABLE)
    data_created = models.DateTimeField(verbose_name='Дата создания')
    data_updated = models.DateTimeField(verbose_name='Дата последнего изменения', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='в наличии')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)


class Version(models.Model):
    version_number = models.IntegerField(verbose_name='номер версии')
    version_name = models.CharField(max_length=50, verbose_name='название версии')
    is_active = models.BooleanField(verbose_name='активная версия', **NULLABLE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')

    # переопределяем сейв метод для установки единственной is_active версии (*)
    def save(self, *args, **kwargs):
        if self.is_active:
            Version.objects.filter(product=self.product).exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.version_number} - {self.version_name}: {self.is_active}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
