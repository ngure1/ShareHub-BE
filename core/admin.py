from django.contrib import admin
from . import models


class InnovationAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "created_at", "updated_at", "status")


class InnovationCommentAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "text", "created_at", "updated_at", "likes")


admin.site.register(models.Innovation, InnovationAdmin)
admin.site.register(models.InnovationComment, InnovationCommentAdmin)
