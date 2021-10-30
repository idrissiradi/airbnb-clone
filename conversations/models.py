from django.db import models

from core import models as core_models
from users.models import User


class Conversation(core_models.TimeStampedModel):
    participants = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return str(self.created)


class Message(core_models.TimeStampedModel):
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} says: {self.message}"
