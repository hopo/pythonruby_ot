from django.db import models

from django.utils import timezone

# Create your models here.


class Post(models.Model):
    class Meta:
        verbose_name_plural = "Post"

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        timezone.now()
        self.save()

    def __str__(self):
        return self.title
