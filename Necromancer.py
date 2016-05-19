import cmd, sys, textwrap

DESC = 'desc'
SHORTDESC = 'shortdesc'
TAKEABLE = 'takeable'
PLACES = 'places'
PEOPLE = 'people'
GROUND = 'ground'
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'
SCREEN_WIDTH = 75
LOCKED = 'locked'
curr_location = 'Condemned Museum'

curr_level = 1
inventory = []

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

def set_curr_location(location):
	global curr_location
	curr_location = location

def next_level():
	curr_level += 1

worldPlaces = {
	'Condemned Museum': {
		DESC: 'Condemned Museum Desc',
		PEOPLE: [],
		GROUND: [],
		LOCKED: False},
	}

itemList = {
	'Necronomicon': {
		SHORTDESC: 'A book bound black ...',
		DESC: 'Blah blah blah',
		TAKEABLE: True},
	}

peopleList = {
	'Self': {
		SHORTDESC: 'A --- woman. Dark hair, blah blah',
		DESC: 'Blah blah'},
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
	print
	pretty_print(place)
	pretty_print('-' * SCREEN_WIDTH)
	pretty_print(worldPlaces[place][DESC])
	#if len(worldPlaces[place][PEOPLE]) > 0:
	#	print
	#	print 'People at this location:'
	#	for person in worldPlaces[place][PEOPLE]:
	#		pretty_print(' -' + person)
	#print
	#if len(worldPlaces[place][GROUND]) > 0:
	#	print 'Things in this location:'
	#	for item in worldPlaces[place][GROUND]:
	#		pretty_print(' -' + item)
	pretty_print('-' * SCREEN_WIDTH)

def list_places():
	for place in worldPlaces:
		print place

def change_location(location):
	if worldPlaces[location][LOCKED]:
		pretty_print('You have no reason to go here.')
	else:
		set_curr_location(location)
		display_place_info(location)

def take_item(item):
	worldPlaces[curr_location][GROUND].remove(item)
	inventory.append(item)

class adventureConsole(cmd.Cmd):
	prompt = '\n> '
	def default(self, arg):
		pretty_print('That isn\'t a valid command. Type \"help\" for a list of commands.')
	def do_quit(self,arg):
		return True
	def help_quit(self):
		pretty_print('Quits the game.')
	def do_location(self, arg):
		display_place_info(curr_location)
	def help_location(self):
		pretty_print('Shows information on the current location.')
	def do_talk(self, arg):
		arg = arg.title()
		if arg == '':
			pretty_print('Who are you talking to?')
			return
		if arg == 'Self':
			pretty_print('Don\'t do that. People will think you\'re weird.')
			return
		for person in worldPlaces[curr_location][PEOPLE]:
			if arg in person:
				if peopleList[person][DNUM] >= len(peopleList[person][DIALOG]):
					pretty_print('They don\'t have anything more to say.')
				else:
					pretty_print('\"' + peopleList[person][DIALOG][peopleList[person][DNUM]] + '\"')
					peopleList[person][DNUM] += 1
				return
		pretty_print('Nobody named ' + arg + ' could be found at this location.')
	def help_talk(self):
		pretty_print('Usage: talk <person>')
		pretty_print('Begins a conversation with a person in the location.')	
	def do_inventory(self, arg):
		inventory.sort()
		if len(inventory) == 0:
			pretty_print('Your inventory is empty.')
		inv_printer = ''
		for item in inventory:
			pretty_print(item + ': ' + itemList[item][SHORTDESC] + '\n')

	def help_inventory(self):
		pretty_print('Shows the items in your inventory.')
	def do_look(self, arg):
		arg = arg.title()
		if arg == '':
			if len(worldPlaces[curr_location][PEOPLE]) > 0:
				print
				print 'People at this location:'
				for person in worldPlaces[curr_location][PEOPLE]:
					pretty_print(' -' + person)
			print
			if len(worldPlaces[curr_location][GROUND]) > 0:
				print 'Things in this location:'
				for item in worldPlaces[curr_location][GROUND]:
					pretty_print(' -' + item)
			if len(worldPlaces[curr_location][PEOPLE]) == 0 and len(worldPlaces[curr_location][GROUND]) == 0:
				pretty_print('There\'s nothing of interest here.')
			return
		for item in (inventory + worldPlaces[curr_location][GROUND]):
			if arg in item:
				pretty_print(item + ': ' + itemList[item][SHORTDESC] + '\n')
				return
		for person in (worldPlaces[curr_location][PEOPLE] + ['Self']):
			if arg in person:
				pretty_print(person + ': ' + peopleList[person][SHORTDESC] + '\n')
				return
		pretty_print('There isn\'t anything like that to look at.')
	def help_look(self):
		pretty_print('Usage: look  OR  look <item>  OR  look <person>')
		pretty_print('Gives a short description of the item.')
	def do_examine(self, arg):
		arg = arg.title()
		if arg == '':
			pretty_print('What are you examining?')
			return
		for item in (inventory + worldPlaces[curr_location][GROUND]):
			if arg in item:
				pretty_print(item + ': ' + itemList[item][DESC] + '\n')
				return
		for person in (worldPlaces[curr_location][PEOPLE] + ['Self']):
			if arg in person:
				pretty_print(person + ': ' + peopleList[person][DESC] + '\n')
				return
		pretty_print('There isn\'t anything like that to look at.')
	def help_examine(self):
		pretty_print('Usage: examine <item>  OR  examine <person>')
		pretty_print('Various uses. Typically gives a more in depth description of an item, allows you to see its contents (like in the case of letters or maps), or gives extra information.')
	def do_take(self, arg):
		arg = arg.title()
		if arg == '':
			pretty_print('What are you taking?')
			return
		for item in worldPlaces[curr_location][GROUND]:
			if arg in item:
				if itemList[item][TAKEABLE]:
					pretty_print('Taken.')
					take_item(item)
				else:
					pretty_print('You can\'t take this item.')
				return
		pretty_print(arg + ' can\'t be picked up.')
	def help_take(self):
		pretty_print('Usage: take <item>')
		pretty_print('Picks up an item and put it in your inventory, along with any associated effects of doing so.')
	def do_drop(self, arg):
		arg = arg.title()
		for item in inventory:
			if arg in item:
				yn = ''
				while yn != 'Y' and yn != 'N':
					yn = raw_input('Drop Item? (y/n): ')
					yn = yn.title()
				if yn == 'Y':
					inventory.remove(item)
					worldPlaces[curr_location][GROUND].append(item)
					print 'Dropped.'
					return
		pretty_print('Nothing like that could be dropped.')
	def help_drop(self):
		pretty_print('Usage: drop <item>')
		pretty_print('Removes an item from your inventory, along with any associated effects of doing so.')
	def do_go(self, arg):
		dest = ''
		arg = arg.title()
		if arg == '':
			pretty_print('Where are you going?')
			return
		if arg == curr_location:
			pretty_print('You\'re already at ' + arg + '.')
		elif arg in worldPlaces:
			change_location(arg)
		elif arg:
			for place in worldPlaces:
				if arg in place.split():
					if place == curr_location:
						pretty_print('You\'re already at ' + place + '.')
					else:
						change_location(place)
					return
			pretty_print('That isn\'t a valid location.')
		else:
			pretty_print('That isn\'t a valid location.')
	def help_go(self):
		pretty_print('Usage: go <place>')
		pretty_print('Takes you to the specified location.')
	
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
	list_places()
	adventureConsole().cmdloop()
	print('Fin')
