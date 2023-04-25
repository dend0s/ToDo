from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse


class ToDo(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Имя')
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ['-date_created']

    def get_absolute_url(self):
        return reverse('detail_todo', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
