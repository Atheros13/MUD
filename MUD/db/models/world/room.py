from django.db import models

### ROOM CLASS ###


class Room(models.Model):

    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    # exits
    # entrances
    # players

    def __str__(self):

        return self.title

    ## DESCRIBE ##
    def describe_room(self, player):
    
        line = '#' + '-'*77 + '#'

        # sends description to player
        #self.mud.send_data(player.id,
        #                   '%s\n\t%s\n\n%s\n\n%sExits: %s\n>>>' % (line, self.title, description, line, exits))

        pass

class RoomJanus(models.Model):

    """ Janus is the Roman two faced gods of doorways entrance and exit. """

    # From
    exit = models.CharField(max_length=50, blank=False, null=False)
    room_from = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="exits")
    hidden = models.BooleanField(default=False)
    # exit_found_by

    # To
    entrance = models.CharField(max_length=50, blank=False, null=False)
    room_to = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="entrances")
       
    def __str__(self):

        pass

#-----------------------------------------------------------------------------#