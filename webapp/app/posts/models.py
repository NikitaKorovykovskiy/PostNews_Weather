from django.contrib.auth.models import User
from django.db import models
from django_advance_thumbnail import AdvanceThumbnailField


class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Автор"
    )
    title = models.CharField(
        "Заголовок",
        max_length=50,
    )
    image = models.ImageField("Картинка")
    preview = AdvanceThumbnailField(
        source_field="image",
        upload_to="images/thumbnails/",
        null=True,
        blank=True,
        size=(200, 200),
    )
    text = models.TextField(
        "Текст поста",
    )
    pub_date = models.DateTimeField("Дата и время публикации")

    class Meta:
        ordering = ["-pub_date"]
        verbose_name = "пост"
        verbose_name_plural = "посты"
