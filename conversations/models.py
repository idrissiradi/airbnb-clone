from django.db import models

from core import models as core_models
from users.models import User


class Conversation(core_models.TimeStampedModel):
    participants = models.ManyToManyField(
        User, blank=True, related_name="conversations"
    )

    def __str__(self):
        usernames = []
        for user in self.participants.all():
            usernames.append(user.username)
        return ", ".join(usernames)

    def count_message(self):
        return self.messages.count()

    count_message.short_description = "Number of Messages"

    def count_participants(self):
        return self.participants.count()

    count_participants.short_description = "Number of Participants"


class Message(core_models.TimeStampedModel):
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation = models.ForeignKey(
        Conversation, on_delete=models.CASCADE, related_name="messages"
    )

    def __str__(self):
        return f"{self.user} says: {self.message}"
