from django.db import models
from db.models.world.room import Room, RoomJanus

class Player(models.Model):

    name = models.CharField(max_length=30, unique=True, blank=False, null=False)
    password = models.CharField(max_length=30, blank=False, null=False)
    description = models.TextField(blank=True, null=True)

    room = models.ForeignKey(Room, null=True, on_delete=models.SET_NULL, related_name="players")
    found_exits = models.ForeignKey(RoomJanus, null=True, on_delete=models.SET_NULL, related_name="exit_found_by")
