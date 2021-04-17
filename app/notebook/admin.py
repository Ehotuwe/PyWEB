from django.contrib import admin

# Register your models here.
from .models import Notebook


@admin.register(Notebook)
class NotebookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "date_add", "public", "important", "activity")
    list_editable = ("title", "public", "important", "activity")
    list_display_links = ("id",)

    def save_model(self, request, obj, form, change):
        if not hasattr(obj, 'user') or not obj.user:
            obj.user = request.user
        return super().save_model(request, obj, form, change)
