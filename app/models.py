from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    video_file = models.FileField(upload_to='videos/')  # Путь для сохранения видео
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
