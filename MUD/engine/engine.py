#-----------------------------------------------------------------------------#

### PYTHON IMPORTS ###

import time

#-----------------------------------------------------------------------------#

### MUD IMPORTS ###

from engine.server import MudServer
from mud.mud_world import MudWorld

#-----------------------------------------------------------------------------#

### ENGINE CLASS ###

class MudEngine():

    server = MudServer()

    world = MudWorld() # 
    #commands MudCommands() # 
    
    def __init__(self, *args, **kwargs):

        self.players = {}

        #
        self.run()

    ## RUN ##
    def run(self):

        '''Runs a While loop, that updates the server ever 0.2 seconds,
        checks new connections and disconnections, and then checks 
        and processes, all commands/data sent by each id in that 
        time period. '''

        while True:

            # update after 0.2 seconds
            time.sleep(0.2)
            self.server.update()

            # check for new connections
            for id in self.server.get_new_players():
                if id not in self.players:
                    self.players[id] = {}

            # check for disconnections
            for id in self.server.get_disconnected_players():
                if id in self.players:
                    self.players.pop(id, None)

            # process commands
            for id, data in self.server.get_commands():
                self.process_commands(id, data)

    ## PROCESS ##
    def process_commands(self, id, raw_data):

        print(id, raw_data)
        data = raw_data.split()

        if len(data) > 1:
            print(data)
            if data[0] == "korero":
                to = int(data[1])
                message = (" ").join(data[2:])
                self.server.send_data(to, message)





#-----------------------------------------------------------------------------#'




#-----------------------------------------------------------------------------#
