from django.db import models

from core import models as core_models
from users.models import User
from rooms.models import Room


class List(core_models.TimeStampedModel):
    name = models.CharField(max_length=80)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lists")
    rooms = models.ManyToManyField(Room, blank=True, related_name="lists")

    def __str__(self):
        return self.name

    def count_rooms(self):
        return self.rooms.count()

    count_rooms.short_description = "Number of Rooms"
