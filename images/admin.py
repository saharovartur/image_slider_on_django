from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from images.models import Image


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['id', 'title', 'img']

