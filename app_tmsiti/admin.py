from django.contrib import admin

# Register your models here.
from .models import(
    Announcements,
    News,
    NewsDetail,
    Leadership,
    Units,
    Standards,
    StandardsInformation
)


admin.site.register(Announcements)
admin.site.register(News)
admin.site.register(NewsDetail)
admin.site.register(Leadership)
admin.site.register(Units)
admin.site.register(Standards)
admin.site.register(StandardsInformation)