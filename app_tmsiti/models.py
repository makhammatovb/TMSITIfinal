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
    # news = models.ForeignKey(News, on_delete=models.CASCADE)
    news_image = models.ImageField(upload_to='news/')



class Leadership(models.Model):
    leader_image = models.ImageField(upload_to='leaders/')
    leader_position = models.CharField(max_length=100)
    leader_name = models.CharField(max_length=255)
    leader_days = models.CharField(max_length=10)
    leader_phone = models.CharField(max_length=13)
    leader_email = models.CharField(max_length=255)
    leader_bachelor = models.CharField(max_length=255, blank=True, null=True)
    leader_master = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.leader_name

    class Meta:
        verbose_name_plural = 'Leaderships'
        db_table = 'leadership'


class Units(models.Model):
    staff_image = models.ImageField(upload_to='units/', null=True, blank=True)
    staff_position = models.CharField(max_length=255)
    staff_name = models.CharField(max_length=255)
    staff_phone = models.CharField(max_length=13)
    staff_email = models.CharField(max_length=255)

    def __str__(self):
        return self.staff_name

    class Meta:
        verbose_name_plural = 'Units'
        db_table = 'units'



class Standards(models.Model):
    standard_name = models.CharField(max_length=100)
    standard_description = models.CharField(max_length=100)

    def __str__(self):
        return self.standard_name

    class Meta:
        verbose_name_plural = 'Standards'
        db_table = 'standards'


class StandardsInformation(models.Model):
    standard = models.ForeignKey(Standards, on_delete=models.CASCADE)
    standard_file = models.FileField(upload_to='standards/')


class Contact(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    leadership = models.ForeignKey(Leadership, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name_plural = 'Contacts'
        db_table = 'contact'


class BuildingRegulations(models.Model):
    building_number = models.IntegerField(unique=True)
    building_mark = models.CharField(max_length=15, unique=True)
    building_name = models.CharField(max_length=255)
    building_document = models.FileField(upload_to='buildings/')

    def __str__(self):
        return self.building_name

    class Meta:
        verbose_name_plural = 'Building Regulations'
        db_table = 'building_regulations'


