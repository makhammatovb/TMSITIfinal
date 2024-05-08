from django.contrib import admin

# Register your models here.
from .models import(
    Announcements,
    News,
    NewsDetail
)


admin.site.register(Announcements)
admin.site.register(News)
admin.site.register(NewsDetail)