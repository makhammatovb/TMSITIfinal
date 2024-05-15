from django.db import models


# Create your models here.
class Dictionary(models.Model):
    word_number = models.IntegerField()
    word_uz = models.CharField(max_length=255)
    word_ru = models.CharField(max_length=255)
    word_en = models.CharField(max_length=255)
    word_tk = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.word_uz} - {self.word_ru} - {self.word_en} - {self.word_tk}"

    class Meta:
        db_table = 'dictionary'
        verbose_name = 'Dictionary'
        verbose_name_plural = 'Dictionaries'
        ordering = ['word_number']



class Word(models.Model):
    number = models.IntegerField()
    word = models.ForeignKey(Dictionary, on_delete=models.CASCADE)
    word_description_uz = models.TextField()
    word_description_ru = models.TextField(null=True)
    word_description_en = models.TextField(null=True)
    word_description_tk = models.TextField(null=True)