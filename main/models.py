from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class asexam(models.Model):
    title = models.CharField('Название экзамена', max_length=255)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    exam_date = models.DateField('Дата проведения экзамена')
    image = models.ImageField('Задание (картинка)', upload_to='exam_images/')
    users = models.ManyToManyField(get_user_model(), verbose_name='Пользователи, которые пишут экзамен')
    is_public = models.BooleanField('Опубликовано', default=False)

    def __str__(self):
        return self.title
