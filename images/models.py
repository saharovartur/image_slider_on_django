from django.db import models
from filer.fields.image import FilerImageField


class Image(models.Model):
    """
    Модель изображения
    """
    title = models.CharField(max_length=100, verbose_name='Название')
    img = FilerImageField(null=True, related_name='images', on_delete=models.CASCADE,
                          verbose_name='Изображение через Filer')

    class Meta:
        ordering = ['id']
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

