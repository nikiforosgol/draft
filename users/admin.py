
from django.contrib import admin
from .models import *


class DocumentInline(admin.TabularInline):
    model = Document


class ProjectAdmin(admin.ModelAdmin):
    inlines = [DocumentInline]


admin.site.register(PracticeArea)
admin.site.register(Project)
admin.site.register(Document)
admin.site.register(Placeholder)




