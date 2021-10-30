from django.db import models

from core import models as core_models
from users.models import User
from rooms.models import Room


class List(core_models.TimeStampedModel):
    name = models.CharField(max_length=80)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rooms = models.ManyToManyField(Room, blank=True)

    def __str__(self):
        return self.name
