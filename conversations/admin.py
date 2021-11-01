from django.contrib import admin

from . import models


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "count_message",
        "count_participants",
    )


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "created",
    )
