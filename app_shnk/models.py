from django.db import models


# Create your models here.
class SHNKSystemsModel(models.Model):
    system_number = models.IntegerField()
    system_name = models.CharField(max_length=255)

    def __str__(self):
        return self.system_name

    class Meta:
        db_table = 'shnk_systems'
        verbose_name = 'SHNK System'
        verbose_name_plural = 'SHNK Systems'


class SHNKGroupsModel(models.Model):
    group_number = models.IntegerField()
    group_name = models.CharField(max_length=255)
    group_system = models.ForeignKey(SHNKSystemsModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.group_name

    class Meta:
        db_table = 'shnk_groups'
        verbose_name = 'SHNK Group'
        verbose_name_plural = 'SHNK Groups'


class SHNKSubSystemsModel(models.Model):
    subsystem_code = models.CharField(max_length=25)
    subsystem_name = models.CharField(max_length=255)
    subsystem_file_uz = models.FileField(upload_to='subsystems_uz')
    subsystem_file_ru = models.FileField(upload_to='subsystems_ru')
    subsystem_group = models.ForeignKey(SHNKGroupsModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.subsystem_name

    class Meta:
        db_table = 'shnk_subsystems'
        verbose_name = 'SHNK Subsystem'
        verbose_name_plural = 'SHNK Subsystems'
