from django.db import models


class Block(models.Model):
    sorting = models.PositiveSmallIntegerField(help_text='Последовательность вывода блоков на странице', unique=True)

    class Meta:
        ordering = ('sorting',)


class Text(models.Model):
    text = models.CharField(max_length=300)
    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name='texts')


class Image(models.Model):
    image_url = models.URLField(verbose_name='Ссылка на фото', null=True, blank=True)
    image_file = models.ImageField(upload_to='images/', verbose_name='Фотография', null=True, blank=True)
    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name='images')
