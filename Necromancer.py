import cmd, sys, textwrap

DESC = 'desc'
SHORTDESC = 'shortdesc'
TAKEABLE = 'takeable'
PLACES = 'places'
PEOPLE = 'people'
GROUND = 'ground'
DECEASED = 'deceased'
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'
SCREEN_WIDTH = 75
LOCKED = 'locked'
currLocation = 'Condemned Museum: Atrium'

currLevel = 1
inventory = ['Necronomicon', 'Spade']

'''SOME INTERESTING IDEAS:
Perhaps give main character ability to kill people and then reanimate them and use them - moral quandary (reanimating vs killing)?
	Perhaps this moral quandary wouldn't exist because posing as people for personal gain is bad .. but perhaps it allows for a human element?
	
How evil should the main character be? Should it be more of a sly antihero type?
Should the main character have an emotional interest, yet bluntness about the stories of others?
What are the motives? Revenge? Necromancy isn't soft shit, but revenge seems a little much.
	Just interest? Perhaps just a curious/morbid/weird type that is into the stories of dead people?
	Maybe you go to the library a lot to learn backstory and that's how you learn about the stuff the people you reanimate can do

Should it have more of a solving-a-mystery vibe?
	This might be cool - looking back on people for their backstory, using that backstory to move the plot along - say you reanimate a banker so you can get into the bank's records or something
	
It should definitely be modern-day-ish, probably before Computers and technology but definitely not medeival/fantasy. It would be interesting to go with somewhere maybe around the 1800s
	Enough to be modern-ish, but not so modern so as to make the Necromancer too easy to catch
	
Making people pose as ghosts would be cool.

Should their be fighting / a fighting engine? Should it be possible for you to reanimate people to fight others?
	Perhaps ... I don't think it needs an engine though. Maybe just the ability to kill certain hostile people?
		Or maybe not. I like the sneaky vibe, killing doesn't seem very necessary.
		
Tentative story:

No father since she was a child. Gets locked in the abandoned museum somehow (bullies? orphanage staff as a punishment? Maybe she was placed there by the people who *killed (but not really)* her father so she wouldn't tell?)
Finds Necromancy book
Starts practicing it all the time, finally gets it on a small animal or something
eventually reanimates people
Wants to find out what happened to her father
Reanimates corpses to attempt to solve the mystery
Gets deep into a bunch of cult shit
Her father isn't dead but the leader of a cult against magick, etc
	Father cast you out when you were young because of your magick aura
	Couldn't bring himself to cull you as the cult should
Ending - ???
Options:
	Kill the father because of his genocide of magick users
	Save the father like he saved you, but somehow disband the cult? - How??
	-- Players choice? - maybe, this might be interesting
	
	

'''

def set_currLocation(location):
	global currLocation
	currLocation = location

def next_level():
	currLevel += 1

worldPlaces = {
	'Condemned Museum: Atrium': {
		DESC: 'You find yourself in a large, dark atrium. The skylight above is streaked with dust and dirt. Soft rays of light cut their way through, illuminating sections of the worn, concrete floor. Debris is strewn about haphazardly, and a thick layer of dust sits on most of the exhibits. The centerpiece of the room is a statue of the founder of the town of Heathervale, Charles Alfred, most of which now lies crumbled on the floor.',
		PEOPLE: [],
		GROUND: [],
		NORTH: 'Condemned Museum: Records',
		LOCKED: False},
	'Condemned Museum: Records': {
		DESC: 'The air in the records room is thick with the smell of dusty old books. Rows of shelves fill the area, and stacks of books can be found gathering cobwebs in the corners. The room is dimly lit by an oil lamp sitting on a desk next to the door.',
		PEOPLE: [],
		GROUND: ['Book Of Obituaries, 1896 - 1897'],
		SOUTH: 'Condemned Museum: Atrium',
		LOCKED: False},
	}
	
peopleList = {
	'Self': {
		SHORTDESC: 'A --- woman. Dark hair, blah blah',
		DESC: 'Blah blah',
		DECEASED: False},
}

obituaryLongDesc = ''

def getObituaryLongDesc():
	for p in peopleList:
		if peopleList[p][DECEASED]:
			obituaryLongDesc += p + ' ' + peopleList[p][SHORTDESC] + '\n'
	
itemList = {
	'Necronomicon': {
		SHORTDESC: 'A book bound in black velvet with silver markings inscribed upon the cover.',
		DESC: 'A book bound in black velvet with silver markings inscribed upon the cover. It is filled with detailed descriptions of necromancy and other rituals surrounding death. The pages are marked heavily with notes.',
		TAKEABLE: True},
	'Spade': {
		SHORTDESC: 'A rusty old spade with a wooden handle and an iron tip.',
		TAKEABLE: True},
	'Book Of Obituaries, 1896 - 1897': {
		SHORTDESC: 'A large book of obituaries. It is heavy in your hand.',
		DESC: obituaryLongDesc,
		TAKEABLE: False },
	}

def pretty_print(text):
	tarray = text.split('\n')
	for txt in tarray:
		for line in textwrap.wrap(txt, SCREEN_WIDTH):
			print(line)
			
def pretty_center_print(text):
	tarray = text.split('\n')
	for txt in tarray:
		for line in textwrap.wrap(txt, SCREEN_WIDTH):
			print (' ' * ((SCREEN_WIDTH - len(txt)) / 2) + line + (' ' * ((SCREEN_WIDTH - len(txt)) / 2)) )

def display_place_info(place):
	pretty_print(place)
	pretty_print('-' * SCREEN_WIDTH)
	pretty_print(worldPlaces[place][DESC])
	pretty_print('-' * SCREEN_WIDTH)

def list_places():
	for place in worldPlaces:
		print place

def go(direction):
	if direction in worldPlaces[currLocation]:
		change_location(worldPlaces[currLocation][direction])
	else:
		pretty_print('You can\'t go that direction.')
		
def change_location(location):
	if worldPlaces[location][LOCKED]:
		pretty_print('You have no reason to go here.')
	else:
		set_currLocation(location)
		display_place_info(location)

def take_item(item):
	worldPlaces[currLocation][GROUND].remove(item)
	inventory.append(item)

def quit_game():
	yn = ''
	while yn != 'Y' and yn != 'N':
		yn = raw_input('Do you really want to quit? All unsaved progress will be lost (y/n): ')
		yn = yn.title()
		if yn == 'Y':
			sys.exit('You have quit the game.')
		if yn == 'N':
			return
				
def talk(arg):
	if arg == '':
		pretty_print('Who are you talking to?')
		return
	if arg == 'Self':
		pretty_print('Don\'t do that. People will think you\'re weird.')
		return
	for person in worldPlaces[currLocation][PEOPLE]:
		if arg in person:
			if peopleList[person][DNUM] >= len(peopleList[person][DIALOG]):
				pretty_print('They don\'t have anything more to say.')
			else:
				pretty_print('\"' + peopleList[person][DIALOG][peopleList[person][DNUM]] + '\"')
				peopleList[person][DNUM] += 1
			return
	pretty_print('Nobody named ' + arg + ' could be found at this location.')

def show_inventory():
	inventory.sort()
	if len(inventory) == 0:
		pretty_print('Your inventory is empty.')
	inv_printer = ''
	for item in inventory:
			pretty_print(item + ': ' + itemList[item][SHORTDESC] + '\n')
		
def examine(arg):
	if arg == '':
		pretty_print('What are you examining?')
		return
	for item in (inventory + worldPlaces[currLocation][GROUND]):
		if arg in item:
			if DESC in itemList[item]:
				pretty_print(item + ': ' + itemList[item][DESC] + '\n')
				return
			else:
				pretty_print(item + ': ' + itemList[item][SHORTDESC] + '\n')
				return
	for person in (worldPlaces[currLocation][PEOPLE] + ['Self']):
		if arg in person:
			if DESC in itemList[item]:
				pretty_print(person + ': ' + peopleList[person][DESC] + '\n')
				return
			else:
				pretty_print(person + ': ' + peopleList[person][SHORTDESC] + '\n')
				return
	pretty_print('There isn\'t anything like that to look at.')

def look(arg):
	if arg == '':
		if len(worldPlaces[currLocation][PEOPLE]) > 0:
			print
			print 'People at this location:'
			for person in worldPlaces[currLocation][PEOPLE]:
				pretty_print(' -' + person)
		print
		if len(worldPlaces[currLocation][GROUND]) > 0:
			print 'Things in this location:'
			for item in worldPlaces[currLocation][GROUND]:
				pretty_print(' -' + item)
		if len(worldPlaces[currLocation][PEOPLE]) == 0 and len(worldPlaces[currLocation][GROUND]) == 0:
			pretty_print('There\'s nothing of interest here.')
		return
	i = 0
	itemToExamine = ''
	for item in (inventory + worldPlaces[currLocation][GROUND]):
		if arg in item:
			i += 1
			if i > 1:
				pretty_print('You\'ll have to be more specific.')
				return
			itemToExamine = item
	i = 0
	personToExamine = ''
	for person in (worldPlaces[currLocation][PEOPLE] + ['Self']):
		if arg in person:
			i += 1
			if i > 1:
				pretty_print('You\'ll have to be more specific.')
				return
			personToExamine = person
	if itemToExamine is not '' and personToExamine is not '':
		pretty_print('You\'ll have to be more specific.')
		return
	if itemToExamine is not '':
		pretty_print(itemToExamine + ': ' + itemList[itemToExamine][SHORTDESC] + '\n')
		return
	if personToExamine is not '':
		pretty_print(person + ': ' + peopleList[personToExamine][SHORTDESC] + '\n')
		return
	pretty_print('There isn\'t anything like that to look at.')
	
def take(arg):
	if arg == '':
		pretty_print('What are you taking?')
		return
	for item in worldPlaces[currLocation][GROUND]:
		if arg in item:
			if itemList[item][TAKEABLE]:
				pretty_print('Taken.')
				take_item(item)
			else:
				pretty_print('You can\'t take this item.')
			return
	pretty_print(arg + ' can\'t be picked up.')

def drop(arg):
	for item in inventory:
		if arg in item:
			yn = ''
			while yn != 'Y' and yn != 'N':
				yn = raw_input('Drop Item? (y/n): ')
				yn = yn.title()
			if yn == 'Y':
				inventory.remove(item)
				worldPlaces[currLocation][GROUND].append(item)
				print 'Dropped.'
				return
	pretty_print('Nothing like that could be dropped.')
	
def go_helper(arg):
	dest = ''
	if arg == '':
		pretty_print('Which direction are you going?')
		return
	elif arg.lower() in NORTH:
		go(NORTH)
	elif arg.lower() in SOUTH:
		go(SOUTH)
	elif arg.lower() in EAST:
		go(EAST)
	elif arg.lower() in WEST:
		go(WEST)
	else:
		pretty_print('That\'s not a valid direction. Try NORTH, SOUTH, EAST, or WEST.')
	
class adventureConsole(cmd.Cmd):
	prompt = '\n> '
	doc_header = 'Commands are documented below. Type \'help commands\' to learn how to use them.\n'
	ruler = ''
	def default(self, arg):
		print
		pretty_print('That isn\'t a valid command. Type \'help\' for a list of commands.')
	def emptyline(self):
		print
		pretty_print('You\'ll have to specify a command.')
	def do_commands(self, arg):
		print
		pretty_print('Type \'help commands\' to learn about commands.')
	def help_commands(self):
		print
		pretty_print('Commands are how you interact with the game. Typing \'go north\', for example, will move your character to the north. You can type \'help\' followed by the name of a command to see more information on how to use it. Commands tend to be pretty smart, so you will rarely need to fully qualify names. \'examine book\', for example, will be enough if there is an item called \'Recipe book\': the program is smart enough to figure out what you mean. If the provided argument matches multiple items, for example, you type \'look book\' and both a recipe book and a bookend are in the area, it will ask you to be more specific. Many other shorthands are provided for ease of play.')
	def do_quit(self,arg):
		print
		quit_game()
	def help_quit(self):
		print
		pretty_print('Quits the game.')
	def do_location(self, arg):
		print
		display_place_info(currLocation)
	def help_location(self):
		print
		pretty_print('Shows information on the current location.')
	def do_talk(self, arg):
		print
		talk(arg.title())
	def help_talk(self):
		print
		pretty_print('Usage: talk <person>')
		pretty_print('Begins a conversation with a person in the location.')	
	def do_inventory(self, arg):
		print
		show_inventory()
	def help_inventory(self):
		print
		pretty_print('Shows the items in your inventory.')
	def do_inv(self, arg):
		print
		show_inventory()
	def help_inv(self):
		print
		pretty_print('Shorthand for \'inventory\'.')
	def do_i(self, arg):
		print
		show_inventory()
	def help_i(self):
		print
		pretty_print('Shorthand for \'inventory\'.')
	def do_look(self, arg):
		print
		look(arg.title())
	def help_look(self):
		print
		pretty_print('Usage: look  OR  look <item>  OR  look <person>')
		pretty_print('Gives a short description of the item.')
	def do_examine(self, arg):
		print
		examine(arg.title())
	def help_examine(self):
		print
		pretty_print('Usage: examine <item>  OR  examine <person>')
		pretty_print('Various uses. Typically gives a more in depth description of an item, allows you to see its contents (like in the case of letters or maps), or gives extra information.')
	def do_ex(self, arg):
		print
		examine(arg.title())
	def help_ex(self):
		print
		pretty_print('Shorthand for \'examine\'.')
	def do_take(self, arg):
		print
		take(arg.title())
	def help_take(self):
		print
		pretty_print('Usage: take <item>')
		pretty_print('Picks up an item and put it in your inventory, along with any associated effects of doing so.')
	def do_drop(self, arg):
		print
		drop(arg.title())
	def help_drop(self):
		print
		pretty_print('Usage: drop <item>')
		pretty_print('Removes an item from your inventory, along with any associated effects of doing so.')
	def do_go(self, arg):
		print
		go_helper(arg.title())
	def do_n(self, arg):
		print
		go(NORTH)
	def do_s(self, arg):
		print
		go(SOUTH)
	def do_e(self, arg):
		print
		go(EAST)
	def do_w(self, arg):
		print
		go(WEST)
	def do_north(self, arg):
		print
		go(NORTH)
	def do_south(self, arg):
		print
		go(SOUTH)
	def do_east(self, arg):
		print
		go(EAST)
	def do_west(self, arg):
		print
		go(WEST)
	def help_n(self):
		print
		pretty_print('Shorthand for \'go NORTH\'.')
	def help_s(self):
		print
		pretty_print('Shorthand for \'go SOUTH\'.')
	def help_e(self):
		print
		pretty_print('Shorthand for \'go EAST\'.')
	def help_w(self):
		print
		pretty_print('Shorthand for \'go WEST\'.')
	def help_north(self):
		print
		pretty_print('Shorthand for \'go NORTH\'.')
	def help_south(self):
		print
		pretty_print('Shorthand for \'go SOUTH\'.')
	def help_east(self):
		print
		pretty_print('Shorthand for \'go EAST\'.')
	def help_west(self):
		print
		pretty_print('Shorthand for \'go WEST\'.')
	def help_go(self):
		print
		pretty_print('Usage: go <place>')
		pretty_print('Takes you to the specified location.')
		
def checkAll():
		for worldPlace in worldPlaces:
			for item in worldPlaces[worldPlace][GROUND]:
				if item not in itemList:
					sys.exit('ERROR: There was a problem loading items: All ground items must be in the itemList.')
			for person in worldPlaces[worldPlace][PEOPLE]:
				if person not in peopleList:
					sys.exit('ERROR: There was a problem loading people: All world people must be in the peopleList.')
			for item in itemList:
				if not item.istitle():
					sys.exit('ERROR: There was a problem loading items: items must be title case.')
	
if __name__ == '__main__':
	pretty_center_print('---------------------------------------------------------------')
	pretty_center_print(' _   _                                                         ')
	pretty_center_print('| \\ | |                                                        ')
	pretty_center_print('|  \\| | ___  ___ _ __ ___  _ __ ___   __ _ _ __   ___ ___ _ __ ')
	pretty_center_print('| . ` |/ _ \\/ __| \'__/ _ \\| \'_ ` _ \ / _` | \'_ \ / __/ _ \ \'__|')
	pretty_center_print('| |\\  |  __/ (__| | | (_) | | | | | | (_| | | | | (_|  __/ |   ')
	pretty_center_print('\_| \\_/\\___|\\___|_|  \\___/|_| |_| |_|\\__,_|_| |_|\___\___|_|   ')
	pretty_center_print('---------------------------------------------------------------')
	print
	pretty_center_print('A game about finding life in death')
	pretty_center_print('V 1.0\tAuthor: Jake Meacham')
	pretty_center_print('Type \'help\' for a list of commands.')
	print
	checkAll()
	adventureConsole().cmdloop()
	print('Fin')
