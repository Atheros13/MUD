from django.db import models


class Command(models.Model):

    command = models.CharField(max_length=20, blank=False, null=False)

    # ??? world, player, room level commands i.e. is this command one that occurs across the world (look),
    # or a player specific one (to a specific player) or one that only occurs in a room (ring bell)

    def __str__(self):

        return self.command

class CommandShort(models.Model):

    command = models.CharField(max_length=5, blank=False, null=False)
    main_command = models.ForeignKey(on_delete=models.CASCADE, related_name="short_commands")

    def __str__(self):

        return "(%s) %s" % (self.command, self.main_command.command)