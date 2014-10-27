from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin

from .models import Entry


@admin.register(Entry)
class EntryAdmin(MarkdownModelAdmin):
	pass

#admin.site.register(Entry)