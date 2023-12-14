from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    date = models.DateTimeField()
    agree = models.BooleanField()
    url = models.URLField()

    def __str__(self):
        return f'Пользователь {self.name}. Его возраст {self.age}'

class Posts(models.Model):
    title = models.CharField(max_length=25, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Тело статьи')
    is_published = models.BooleanField(verbose_name='опубликовано')
    date = models.DateField(verbose_name='Дата публикации')
    url = models.URLField(verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
