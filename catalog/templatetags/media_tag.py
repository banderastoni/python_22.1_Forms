import os

from django import template
from django.conf import settings
from django.template.defaultfilters import truncatechars

from config.settings import MEDIA_URL

register = template.Library()


@register.simple_tag
def media_tag(product):
    return MEDIA_URL + str(product)


@register.filter
def media_tag(image):
    # Формируем полный путь к медиафайлу, добавляя префикс '/media/'
    media = settings.MEDIA_URL
    return f"{media}{image}"


@register.filter
def truncate_description(description, length=100):
    # Обрезаем описание до первых 100 символов
    return truncatechars(description, length)


@register.simple_tag
def media_tag(path):
    return os.path.join('/', settings.MEDIA_URL, str(path))