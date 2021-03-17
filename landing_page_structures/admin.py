from django.contrib import admin

from .models import Block, Image, Text


class ImageInline(admin.StackedInline):
    model = Image
    extra = 1


class TextInline(admin.StackedInline):
    model = Text
    extra = 1


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('id', 'sorting')
    inlines = [TextInline, ImageInline]
