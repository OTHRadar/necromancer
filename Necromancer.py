import cmd, sys, textwrap

DESC = 'desc'
SHORTDESC = 'shortdesc'
TAKEABLE = 'takeable'
PLACES = 'places'
PEOPLE = 'people'
DECEASED = 'deceased'
DUGUP = 'dugup'
REANIMATED = 'reanimated'
REANIMATOR = 'reanimator'
GROUND = 'ground'
UNDERGROUND = 'underground'
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'
END = 'end'
SCREEN_WIDTH = 75
LOCKED = 'locked'
READ = 'read'
currLocation = 'The Condemned Museum\'s Records Room'

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

#K.W. -> Khan Me'el
#A.O. -> Aloran Orazio

def set_curr_location(location):
	global currLocation
	currLocation = location

worldPlaces = {
	'The Condemned Museum\'s Atrium': {
		DESC: 'The skylight above is streaked with dust and dirt. Soft rays of light cut their way through, illuminating sections of the worn, concrete floor. Debris is strewn about haphazardly, and a thick layer of dust sits on most of the exhibits. The centerpiece of the room is a statue of the founder of the town of Heathervale, Charles Alfred, most of which now lies crumbled on the floor.',
		PEOPLE: [],
		DECEASED: [],
		GROUND: [],
		UNDERGROUND: [],
		NORTH: 'The Condemned Museum\'s Records Room',
		SOUTH: 'The Condemned Museum\'s Courtyard',
		LOCKED: False},
	'The Condemned Museum\'s Records Room': {
		DESC: 'You find yourself in a small, musty room. The air is thick with the smell of dusty old books. Rows of shelves fill the area, and stacks of paper can be found gathering cobwebs in the corners. The room is dimly lit by an oil lamp sitting on a desk next to the door. Beside the lamp is a book bound in black velvet.',
		PEOPLE: [],
		DECEASED: [],
		GROUND: ['Book - Obituaries, 1890 - 1900', 'Book - Necronomicon'],
		UNDERGROUND: [],
		SOUTH: 'The Condemned Museum\'s Atrium',
		LOCKED: False},
	'The Condemned Museum\'s Courtyard': {
		DESC:'The cold night air assails you as you leave the museum. It carries with it the stench of wet livestock, from the farms of nearby Heathervale. Crumbled stone benches surround a fountain in which stagnant water is pooling from the recent rain.',
		PEOPLE: [],
		DECEASED: [],
		GROUND: [],
		UNDERGROUND: [],
		NORTH: 'The Condemned Museum\'s Atrium',
		EAST: 'Heathervale Town Square',
		LOCKED: False},
	'Heathervale Town Square': {
		DESC:'You enter the town square. The shops and streets lie abandoned as everyone has turned in for the night. The streets are cobbled and well-maintaned, though weeds are beginning to emerge from the cracks.',
		PEOPLE: [],
		DECEASED: [],
		GROUND: [],
		UNDERGROUND: [],
		WEST: 'The Condemned Museum\'s Courtyard',
		SOUTH: 'Old Mary\'s Farm',
		EAST: 'Heathervale Graveyard',
		LOCKED: False},
	'Old Mary\'s Farm': {
		DESC:'Blah farm.',
		PEOPLE: [],
		DECEASED: [],
		GROUND:[],
		UNDERGROUND: [],
		NORTH:'Heathervale Town Square',
		WEST:'Old Mary\'s Farmhouse',
		LOCKED: False},
	'Old Mary\'s Farmhouse': {
		DESC: 'A small yellow house with white trim. The paint is cracking and peeling, and has lost its luster. An ornamental windmill sits next to the house, slowly rotating in the wind.',
		PEOPLE: [],
		DECEASED: [],
		GROUND: ['Spade'],
		UNDERGROUND: [],
		EAST:'Old Mary\'s Farm',
		LOCKED: False},
	'Heathervale Graveyard': {
		DESC: 'The gate to the graveyard creaks slightly as you push it open. The lawn is dotted with trees and bushes, and headstones line the three paths splitting from the entrance. A small shack lies at the end of the path to the North.',
		PEOPLE: [],
		DECEASED: [],
		GROUND: [],
		UNDERGROUND: [],
		WEST: 'Heathervale Town Square',
		NORTH: 'North Graveyard Path',
		SOUTH: 'South Graveyard Path',
		EAST: 'East Graveyard Path',
		LOCKED: False},
	'East Graveyard Path': {
		DESC: 'You walk down the path to the east, treading lightly so as to not disturb the gravel beneath your feet. The path you are walking on is thin and overgrown. A few headstones sit on the sides of the path.',
		PEOPLE: [],
		DECEASED: ['Joseph Orazio'],
		UNDERGROUND: ['Silver Watch'],
		GROUND: ['Joseph Orazio\'s Gravestone'],
		WEST: 'Heathervale Graveyard',
		LOCKED: False}
	}
	
peopleList = {
	'Self': {
		SHORTDESC: 'You are Katya, an emaciated young woman with piercing blue eyes and pale white skin, short in stature. Your hair is black and haphazardly cut to neck length. You are wearing a black shirt and pants, which are worn and tearing in places.',},
}
deceasedPeopleList = {
	'Joseph Orazio': {
		SHORTDESC: 'Joseph Orazio, son of Barbera Orazio, died May 18, 1892. He was 24. He was an educated man, an excellent farmhand and cared for his family. He was buried on the East side of the Heathervale graveyard. He is survived by his wife, Sera.',
		DUGUP: False,
		REANIMATED: False,
		REANIMATOR: 'Silver Watch'}
}

def getObituaryLongDesc():
	obit = ''
	for p in deceasedPeopleList:
		obit += p[0:p.index('\'')] + ': ' + deceasedPeopleList[p][SHORTDESC] + '\n'
	return obit
	
itemList = {
	'Book - Necronomicon': {
		SHORTDESC: 'A book bound in black velvet with silver markings inscribed upon the cover.',
		DESC: 'A book bound in black velvet with silver markings inscribed upon the cover. It is filled with detailed descriptions of necromancy and other rituals surrounding death. The pages are marked heavily with notes.',
		READ: '\nThis unholy manuscript endeavors in its entirety to impress upon the reader such knowledge so as to speak (and even bring life) to the resting spirits of men. Here within lie the writings of the great conjurer K.W. as he himself inscribed them upon his deathbed. He so accurately predicted his departure; not a second after the last drop of ink from his pen spilled forth he slumped soundlessly into his chair, leaving to us those whispers the great Divine himself kept secret from men. Upon myself I have taken the burden of distilling this work to its barest necessities, and it is with pleasure that I present here the fruits of my labor. Take heed and read on with prudence, for the details of ceremony may mean the difference between life and death. Tread not lightly on this path, for in the practice of black magick, diligence alone keeps one from death.\n\n1. One must first of course acquire some piece of flesh or bone of he you wish to call upon.\n\n2. A part or parcel dear to them must be collected too, for an offering must be made to entice the spirit forth.\n\n3. Once gathered one must sit alone inside a circle inscribed with an upturned 5-point star, both parcel and flesh at either side. Against one\'s back inscribe a cross and leave an untouched sacrament of wine and bread, that the spirit may not play upon you a trick from your behind.\n\n4. Say aloud in voice unwavering the incantation \'Carmina haec sunt verba inania ignotus incantatum.\' and then keep utter silence.\n\n5. Once a quarter minute you have thus remained, the spirit shall appear as though in human form.\n\n6. Some spirits will be eager to work with you, others may be timid, or even angered by your presence. Each interaction must be handled in its course, and no two spirits are the same.\n\nThus in so many more words K.W. instructs the intrigued reader. I assure you I have missed nothing of import. Godspeed you, acolyte of the dark path. Iter in pace. - A.O.',
		TAKEABLE: True},
	'Spade': {
		SHORTDESC: 'A rusty old spade with a wooden handle and an iron tip.',
		TAKEABLE: True},
	'Book - Obituaries, 1890 - 1900': {
		SHORTDESC: 'A large book of obituaries. It is heavy in your hand.',
		READ: 'obituaryLongDesc',
		TAKEABLE: False },
	'Joseph Orazio\'s Gravestone': {
		SHORTDESC: 'A small headstone. A solitary daisy lies on the ground at its base.',
		DESC: 'Joseph Orazio\n1868 - 1892',
		TAKEABLE: False },
	'Silver Watch': {
		SHORTDESC: 'Joseph Orazio\'s most prized possession, a silver pocketwatch given to him by his father.',
		TAKEABLE: True }
	}

def pretty_print(text):
	tarray = text.split('\n')
	for txt in tarray:
		for line in textwrap.wrap(txt, SCREEN_WIDTH):
			print(line)
def d_print(text):
	pretty_print('\"' + text + '\"')
			
def pretty_center_print(text):
	tarray = text.split('\n')
	for txt in tarray:
		for line in textwrap.wrap(txt, SCREEN_WIDTH):
			print (' ' * ((SCREEN_WIDTH - len(txt)) / 2) + line + (' ' * ((SCREEN_WIDTH - len(txt)) / 2)) )

def replace_last(sourceString, replaceWhat, replaceWith):
    head, sep, tail = sourceString.rpartition(replaceWhat)
    return head + replaceWith + tail
			
def display_place_info(place):
	pretty_print(place)
	pretty_print('-' * SCREEN_WIDTH)
	pretty_print(worldPlaces[place][DESC])
	print
	exits = ''
	numexits = 0
	if NORTH in worldPlaces[place]:
		numexits += 1
		exits += worldPlaces[place][NORTH] + ' is to the NORTH, '
	if SOUTH in worldPlaces[place]:
		numexits += 1
		exits += worldPlaces[place][SOUTH] + ' is to the SOUTH, '
	if EAST in worldPlaces[place]:
		numexits += 1
		exits += worldPlaces[place][EAST] + ' is to the EAST, '
	if WEST in worldPlaces[place]:
		numexits += 1
		exits += worldPlaces[place][WEST] + ' is to the WEST, '
	if (numexits == 1):
		pretty_print((exits)[:-2] + '.')
	else:
		exits = replace_last(exits, ',', ' and')
		exits = replace_last(exits, ',', ' and')
		pretty_print((exits)[:-5] + '.')
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
		pretty_print('You can\'t go to this location right now.')
	else:
		set_curr_location(location)
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
	#TODO: FIX TO MEET NEW DISCUSSION PARADIGM (2 people talking, not one)
	if arg == '':
		pretty_print('Who are you talking to?')
		return
	if arg == 'Self':
		pretty_print('Don\'t do that. People will think you\'re weird.')
		return
	for person in (worldPlaces[currLocation][PEOPLE] + worldPlaces[currLocation][DECEASED]):
		if arg in person:
			talk_switch(person)
		return
	pretty_print('Nobody named ' + arg + ' could be found at this location.')

def is_int(x):
	try:
		int(x)
	except ValueError:
		return False
	return True
	
def choose_response():
	choice = 'x'	
	while not is_int(choice) or int(choice) < 1 or int(choice) > 3:
		choice = raw_input('>')
	return int(choice)
	
def talk_switch(person):
	if person == 'Joseph Orazio':
		d_print('Hello, my name is Katya. Who are you?')
		tw()
		d_print('Why, it says it right there on the stone. Surely you are smarter than you look?')
		tw()
		d_print('(1) I was just making small talk.')
		d_print('(2) I know who you are.')
		d_print('(3) And probably smarter than you.')
		r = choose_response()
		if r == 1:
			d_print('And I, just having a little fun.')
		if r == 2:
			d_print('Then why waste the breath?')
		if r == 3:
			d_print('So young, and full of pride. You would do well to check your aggression.')
		d_print('But I will give some advice. Say what you mean, and mean what you say. Other spirits, you\'ll find, are much less agreeable than I.')
		tw()
		d_print('Do you know anything about my father?')
		tw()
		d_print('Much better! Short and to the point.')

def tw():
	raw_input('...')
	
def show_inventory():
	inventory.sort()
	if len(inventory) == 0:
		pretty_print('Your inventory is empty.')
	inv_printer = ''
	for item in inventory:
			pretty_print(item + ': ' + itemList[item][SHORTDESC] + '\n')
		
def dig():
	if not 'Spade' in inventory:
		pretty_print('You don\'t have anything to dig with.')
		return
	if UNDERGROUND in worldPlaces[currLocation] or DECEASED in worldPlaces[currLocation]:
		for item in worldPlaces[currLocation][UNDERGROUND]:
			worldPlaces[currLocation][UNDERGROUND].remove(item)
			worldPlaces[currLocation][GROUND].append(item)
			pretty_print(item + ' dug up.')
		for dp in worldPlaces[currLocation][DECEASED]:
			deceasedPeopleList[dp][DUGUP] = True
			pretty_print(dp + ' dug up.')
		return
	pretty_print('Nothing to dig, here.')
			
def reanimate(arg):
	inInventory = False
	dropItem = ''
	if ' With ' not in arg:
		print_check_usage()
		return
	argarray = arg.split(' With ')
	arg1 = argarray[0]
	arg2 = argarray[1]
	exists = False
	for item in (inventory + worldPlaces[currLocation][GROUND]):
		if (arg2 in item):
			exists = True
			if item in inventory:
				inInventory = True
				dropItem = item
	if not exists:
		pretty_print('You don\'t have any items like that.')
		return
	for dp in worldPlaces[currLocation][DECEASED]:
		if deceasedPeopleList[dp][DUGUP] == True and arg1 in dp:
			if arg2 in deceasedPeopleList[dp][REANIMATOR]:
				pretty_print('Reanimation succesful.')
				deceasedPeopleList[dp][REANIMATED] = True
				if inInventory:
					inventory.remove(dropItem)
				return
			else:
				pretty_print('Reanimation failed. Try again.')
				return
	pretty_print('There\'s no one like that here.')
			

def examine(arg):
	if arg == '':
		pretty_print('What are you examining?')
		return
	for item in (inventory + worldPlaces[currLocation][GROUND]):
		if arg in item:
			if DESC in itemList[item]:
				pretty_print(item + ': ' + '\n' + itemList[item][DESC] + '\n')
			else:
				pretty_print(item + ': ' + '\n' + itemList[item][SHORTDESC] + '\n')
			if READ in itemList[item]:
				yn = ''
				while yn != 'Y' and yn != 'N':
					yn = raw_input('Read Book? (y/n): ')
					yn = yn.title()
				if yn == 'Y':
					read(item)
			return
	for person in (worldPlaces[currLocation][PEOPLE] + ['Self']):
		if arg in person:
			if DESC in peopleList[person]:
				pretty_print(person + ': ' + '\n' + peopleList[person][DESC] + '\n')
				return
			else:
				pretty_print(person + ': ' + '\n' + peopleList[person][SHORTDESC] + '\n')
				return
	for dp in (worldPlaces[currLocation][DECEASED]):
		if arg in dp:
			if DESC in deceasedPeopleList[dp]:
				pretty_print(dp + ': ' + '\n' + deceasedPeopleList[person][DESC] + '\n')
				return
			else:
				pretty_print(dp + ': ' + '\n' + deceasedPeopleList[person][SHORTDESC] + '\n')
				return
	pretty_print('There isn\'t anything like that to look at.')

def read(arg):
	if arg == '':
		pretty_print('What are you reading?')
		return
	for item in (inventory + worldPlaces[currLocation][GROUND]):
		if arg in item:
			if READ in itemList[item]:
				if 'obituaryLongDesc' in itemList[item][READ]:
					pretty_print(getObituaryLongDesc())
					return
				pretty_print(item + ': ' + itemList[item][READ] + '\n')
			return
	pretty_print('That isn\'t a book.')
	
def look(arg):
	if arg == '':
		if len(worldPlaces[currLocation][PEOPLE]) > 0:
			print
			print 'People at this location:'
			for person in worldPlaces[currLocation][PEOPLE]:
				pretty_print(' -' + person)
		print
		if len(worldPlaces[currLocation][GROUND]) > 0 or len(worldPlaces[currLocation][DECEASED]) > 0:
			print 'Things in this location:'
			for item in worldPlaces[currLocation][GROUND]:
				pretty_print(' -' + item)
			for dp in worldPlaces[currLocation][DECEASED]:
				if deceasedPeopleList[dp][DUGUP] == True:
					pretty_print(' -' + dp)
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
	i = 0
	dpToExamine = ''
	for dp in (worldPlaces[currLocation][DECEASED]):
		if arg in dp:
			i += 1
			if i > 1:
				pretty_print('You\'ll have to be more specific.')
				return
			dpToExamine = dp
	if (itemToExamine is not '' and personToExamine is not '') or (itemToExamine is not '' and dpToExamine is not '') or (dpToExamine is not '' and personToExamine is not ''):
		pretty_print('You\'ll have to be more specific.')
		return
	if itemToExamine is not '':
		pretty_print(itemToExamine + ': ' + itemList[itemToExamine][SHORTDESC] + '\n')
		return
	if personToExamine is not '':
		pretty_print(person + ': ' + peopleList[personToExamine][SHORTDESC] + '\n')
		return
	if dpToExamine is not '':
		pretty_print(dp + ': ' + deceasedPeopleList[dpToExamine][SHORTDESC] + '\n')
		return
	pretty_print('There isn\'t anything like that to look at.')
	
def take(arg):
	itemTaken = False
	if arg == '':
		pretty_print('What are you taking?')
		return
	for item in worldPlaces[currLocation][GROUND]:
		if arg in item:
			if itemList[item][TAKEABLE]:
				pretty_print('Taken.')
				take_item(item)
				itemTaken = True
				return
	for person in worldPlaces[currLocation][PEOPLE]:
		if arg in person:
			pretty_print('You can\'t just take people. It\'s indecent.')
			return
	for dp in worldPlaces[currLocation][DECEASED]:
		if arg in dp:
			pretty_print('You\'re a necromancer, not a necrophiliac.')
			return
	pretty_print('You can\'t take this item.')
	return

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

def print_check_usage():
	pretty_print('Unable to execute command. Check usage.')
	
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
	def cmdloop(self):
		try:
			cmd.Cmd.cmdloop(self)
		except TypeError as e:
			print_check_usage()
			self.cmdloop()
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
	def do_loc(self, arg):
		print
		display_place_info(currLocation)
	def help_loc(self):
		print
		pretty_print('Shorthand for \'location\'')
	def help_location(self):
		print
		pretty_print('Shows information on the current location.')
	def do_dig(self, arg):
		print
		dig()
	def help_dig(self):
		pretty_print('Use items like shovels and spades.')
	def do_reanimate(self, arg):
		reanimate(arg.title())
	def help_reanimate(self):
		pretty_print('Usage: reanimate <person> <item>')
		pretty_print('Performs a ceremony with the given item to reanimate the corpse.')	
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
	def do_read(self, arg):
		print
		read(arg.title())
	def help_read(self, arg):
		print
		pretty_print('Usage: read <book>')
		pretty_print('Read a book.')
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
					sys.exit('ERROR: There was a problem loading items: All ground items must be in the itemList: ' + item)
			for person in worldPlaces[worldPlace][PEOPLE]:
				if person not in peopleList:
					sys.exit('ERROR: There was a problem loading people: All world people must be in the peopleList:' + person)
	
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
