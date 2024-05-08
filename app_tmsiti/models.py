from django.db import models


# Create your models here.
class Announcements(models.Model):
    announcement_date = models.DateTimeField(auto_now_add=True)
    announcement_title = models.CharField(max_length=255)
    announcement_description = models.TextField()

    def __str__(self):
        return self.announcement_title

    class Meta:
        verbose_name_plural = 'Announcements'
        db_table = 'announcements'


class News(models.Model):
    news_date = models.DateTimeField(auto_now_add=True)
    news_title = models.CharField(max_length=255)
    news_description = models.CharField(max_length=255)
    news_image = models.ImageField(upload_to='news/')

    def __str__(self):
        return self.news_title

    class Meta:
        verbose_name_plural = 'News'
        db_table = 'news'


class NewsDetail(models.Model):
    news_date = models.DateTimeField(auto_now_add=True)
    news_title = models.CharField(max_length=255)
    news_description = models.TextField()
    news_image = models.ImageField(upload_to='news/')