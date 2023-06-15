
from django.contrib import admin
from .models import *


class DocumentInline(admin.TabularInline):
    model = Document.project.through
    extra = 1


class PlaceholderInline(admin.TabularInline):
    model = Placeholder.documents.through
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [DocumentInline]


class DocumentAdmin(admin.ModelAdmin):
    inlines = [PlaceholderInline]


admin.site.register(PracticeArea)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Placeholder)




