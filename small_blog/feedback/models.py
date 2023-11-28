from django.db import models


class Feedback(models.Model):

    to_publish = models.BooleanField(
        default=False,
        verbose_name='Проверено',
        help_text='Поставьте галочку, чтобы опубликовать.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено'
    )
    text = models.TextField('Текст отзыва')
    author = models.CharField(
        max_length=128,
        verbose_name='ФИО'
    )
    email = models.CharField(max_length=64, verbose_name='email')

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        if len(self.text) > 32:
            return self.text[:29] + '...'
        return self.text
