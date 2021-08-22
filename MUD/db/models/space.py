from django.db import models

class Space(models.Model):

    pass

#-----------------------------------------------------------------------------#

### IMPORTS ###

#from mud_command import *

#-----------------------------------------------------------------------------#

### ROOM CLASS ###

class Room():

    def __init__(self, engine, *args, 
                 area=None,
                 x=None, y=None, z=None, 
                 title='Enter Title Here',
                 description='Enter Description Here',
                 **kwargs):

        self.mud = self.engine.mud
        self.world = self.engine.world

        self.x = x
        self.y = y
        self.z = z
        
        self.title = title
        self.description = description

        self.commands = self.build_commands()
        self.players = {}

    ## BUILD ##
    def build_commands(self):

        commands = {}
        for c in self.world.commands:
            pass

    ## COMMANDS ##
    def process_command(self, id, command, params):

        ''' '''

        pass

    ## DESCRIBE ##
    def describe_room(self, player):
    
        line = '#' + '-'*77 + '#'

        # this might change if a player notices something extra
        description = self.description

        #? exits - not sure how this will work
        exit_list = []
        if exit_list == []:
            exits = 'There are no known exits.'
        else:
            exits = 'There are some exits.' # to change

        # sends description to player
        self.mud.send_data(player.id,
                           '%s\n\t%s\n\n%s\n\n%sExits: %s\n>>>' % (line, self.title, description, line, exits))



#-----------------------------------------------------------------------------#