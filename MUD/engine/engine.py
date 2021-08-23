#-----------------------------------------------------------------------------#

### PYTHON IMPORTS ###

import time

#-----------------------------------------------------------------------------#

### MUD IMPORTS ###

from engine.server import MudServer
from mud.mud_world import MudWorld

#-----------------------------------------------------------------------------#

### ENGINE CLASS ###

class Room():

    def __init__(self, title, description):

        self.title = title
        self.description = description

        self.exits = {}

class MudEngine():

    server = MudServer()

    def __init__(self, *args, **kwargs):

        self.players = {}

        self.line = '#' + '-'*77 + '#'

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
                    self.players[id] ={
                        "name":None,
                        "room":"te_kore",                   
                        }
                    self.te_kore(id)
                    

            # check for disconnections
            for id in self.server.get_disconnected_players():
                if id in self.players:
                    name = self.players[id]["name"]
                    self.players.pop(id, None)
                    for id in self.players:
                        self.server.send_data(id, "%s has left the world" % name)

            # process commands
            for id, data in self.server.get_commands():
                self.process_commands(id, data)

    ## PROCESS ##
    def process_commands(self, id, raw_data):

        # 
        if self.players[id]["name"] == None:
            self.players[id]["name"] = raw_data
            for pid in self.players:
                if pid != id:
                    self.server.send_data(pid, "%s has entered the world" % self.players[id]["name"])
            self.move_room(id, "yard")

        data = raw_data.split()

        if data[0] in ["Hut", "hut"]:
            self.move_room(id, "hut")
        elif data[0] in ["Yard", "yard"]:
            self.move_room(id, "yard")
        elif data[0] in ["Look", "look", "l"]:
            if self.players[id]["room"] == "yard":
                self.yard(id)
            else:
                self.hut(id)
        elif data[0] in ["Say", "say"] and len(data) > 1:
            sentence = " ".join(data[1:])
            self.speak(id, sentence)

    def speak(self, id, sentence):

        room = self.players[id]["room"]
        name = self.players[id]["name"]

        for pid in self.players:
            if self.players[pid]["room"] == room and pid != id:
                self.server.send_data(pid, "%s says: '%s'\n" % (name, sentence))

    def move_room(self, id, room):

        for pid in self.players:
            if self.players[pid]["room"] == room:
                self.server.send_data(pid, "%s enters the %s" % (self.players[id]["name"], room))
        self.players[id]["room"] = room

        if room == "yard":
            self.yard(id)
        elif room == "hut":
            self.hut(id)

    def te_kore(self, id):
        
        if self.players[id]["name"] == None:
            desc = [self.line, "\nTe Kore - The Nothingness\n\n\n\n\n",
                    "What is your name?\n\n\n\n", "\n\n>>>"]
        for d in desc:
            self.server.send_data(id, d)

    def yard(self, id):

        desc = [self.line, 
                "\nThe Yard\n\n",
                "You stand in a yard outside the door to a small hut.", "The area is bare and locked in on three sides by a tall fence.",
                "\n\nThe only exit you can see is the door to the hut.\n\n",
                "EXITS: Hut"]

        present = "PLAYERS PRESENT: %s" % self.players[id]["name"]
        for pid in self.players:
            if self.players[pid]["room"] == "yard" and pid != id:
                present += " and %s" % self.players[pid]["name"]

        desc +=  [present, 
                "\n\n>>>"]

        for d in desc:
            self.server.send_data(id, d)

    def hut(self, id):

        desc = [self.line, 
                "\nThe Hut\n\n",
                "You stand inside a small one room hut. There is not much besides a single bed and a table and chair.", 
                "Clearly the creator has not had time to make more.",
                "\n\nThe only exit you can see is the door to the yard.\n\n",
                "EXITS:Yard"]

        present = "PLAYERS PRESENT: %s" % self.players[id]["name"]
        for pid in self.players:
            if self.players[pid]["room"] == "hut" and pid != id:
                present += " and %s" % self.players[pid]["name"]

        desc +=  [present, 
                "\n\n>>>"]

        for d in desc:
            self.server.send_data(id, d)

#-----------------------------------------------------------------------------#'




#-----------------------------------------------------------------------------#
