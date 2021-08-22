#-----------------------------------------------------------------------------#

### IMPORTS ###


#-----------------------------------------------------------------------------#

### BASE COMMAND CLASSE ###

class Command():

    def __init__(self, engine, *args, **kwargs):

        self.engine = engine
        self.mud = self.engine.mud
        self.players = self.engine.players

    def syntax_check(self, *args, params=[], group=None, **kwargs):

        '''Compares arg values to params values. Assigns the next value in 
        params as the focus and searches the group keyword object for 
        that focus. If that focus is found, it returns True, the focus object
        and the remaining items in the params argument, otherwise it 
        returns False, '#!error_message', None'''


        # check there is a focus word/s after the grammar syntax 
        # i.e. args = ['ki', 'a'] params = ['ki', 'a', 'Toni']
        # focus = 'Toni'
        if len(params) <= len(args):
            return False, '#!focus', None
        
        # check each arg value is matched to same index params value
        count = 0
        for i in len(args):
            if args[i] != params[i]:
                return False, '#!syntax', None
            count += 1
        focus = params[count]
        try:
            extra_words = params[count+1:]
        except:
            extra_words = []

        # search for the focus word in the group object 
        if type(group) == 'list':
            if focus in group:
                return True, focus, extra_words
        elif type(group) == 'dict':
            if focus in group:
                return True, group[focus], extra_words

        # if check failed
        return False, '#!group', None

    def process_command(self, id, player, params):

        pass

#-----------------------------------------------------------------------------#

### WORLD COMMAND CLASSES ###

class CommandKorero(Command):

    '''Communicatea a message to any player in the same room.'''

    command = 'korero'

    def process_command(self, id, player, params):

        message = ' '.join(params)

        # (later) check player isn't silenced

        # if they say nothing
        if params == []:
            self.mud.send_data(player.id, '\nKaore koe e korero')
            return

        # speak
        for p in player.room.players:
            if p != player:
                self.mud.send_data(p.id, '\nKei te korero a %s:"%s"' % (player.name, message))
            else:
                self.mud.send_data(player.id, '\nKei te korero koe:"%s"' % message)

class CommandPanui(Command):
    
    '''Communicates a message to any player in the world. '''

    command = 'panui'

    def process_command(self, id, player, params):
 
        message = ' '.join(params)
        
        if params == []:
            self.mud.send_data(player.id, '\nKaore koe e panui')
            return

        players = {}
        for id in self.players:
            p = self.players[id]
            players[p.name.lower()] = p
        check, focus, extra_words = self.syntax_check('ki', 'a', params=params, group=players)
        if check:
            if extra_words != []:
                self.mud.send_data(focus.id, 'Panui o %s: "%s"' % (player.name, (''.join(extra_words))))
            else:
                self.mud.send_data(player.id, "You didn't say anything") 
        elif focus == '#!focus':
            self.mud.send_data(player.id, "You didn't indicate who you wanted to panui to")
        elif focus == '#!syntax':
            self.mud.send_data(player.id, "Your grammar/syntax isn't correct")
        elif focus == '#!group':
            self.mud.send_data(player.id, "That person is not in the world")

#-----------------------------------------------------------------------------#

### ROOM GENERAL COMMAND CLASSES ###

class CommandTitiro(Command):

    command = 'titiro'

    def process_command(self, id, player, params):

        room = player.room

        # only titiro -> look at room
        if params == []:
            room_description = room.describe_room(player)
            self.mud.send_data(id, 'Kei te titiro koe.\n%s' % room_description)
            return

        # check if he is looking at another player
        other_players = {}
        for p in room.players:
            other_players[p.name] = p
        check, focus, extra_words = self.syntax_check('ki', 'a', params, other_players)
        if check:
            # change this
            self.mud.send_data(id, 'Kei te titiro koe ia %s' % focus.name)
            return

        # if not any of the above 'general' titiro events, check room specific
        # commands
        self.process_specific_commands(id, player, params)

    def process_specific_commands(self, id, player, params):

        pass

#-----------------------------------------------------------------------------#

### ROOM SPECIFIC COMMAND CLASSES ###


#-----------------------------------------------------------------------------#