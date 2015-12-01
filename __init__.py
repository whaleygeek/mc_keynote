import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
#import anyio.GPIO as GPIO

class DummyPrompt():
    def say(msg):
        print(msg)


    def wait():
        raw_input("?") # python2


class Prompt():
    def __init__(self, mc, gpio, pin=4):
        self.mc   = mc
        self.gpio = gpio
        self.pin  = pin


    def say(msg):
        self.mc.postToChat(msg)


    def wait():
        # wait for press
        while self.gpio.input(self.pin) == True:
            time.sleep(0.1)
        print("v") # DEBUG

        # wait for release
        while self.gpio.input(self.pin) == False:
            time.sleep(0.1)
        print("^") # DEBUG


mc = None

def connect():
    global mc, prompt
    mc = minecraft.Minecraft.create()
    # prompt = Prompt(mc, GPIO, 4)
    prompt = DummyPrompt()

    mc.postToChat("READY!")


#--------------------------------------------------------------------------------

def countdown():
    import time
    import audio
    import mc_clock

    pos = mc.player.getTilePos()
    mc.player.setTilePos(pos.x, pos.y, pos.z+50)
    mc_clock.init(mc)
    mc_clock.draw_face(pos)
    time.sleep(3)

    audio.play("babcock_keynote/countdown.wav")
    for secs in range(30):
        mc_clock.draw_secs(secs, block.GOLD_BLOCK.id)
        time.sleep(1)
        mc_clock.draw_secs(secs, block.AIR.id)

    #audio.play("bang.wav")
    mc_clock.clear_face()

#--------------------------------------------------------------------------------

def eval1():
    prompt.say("Put up your hand")
    prompt.wait()

    prompt.say("IF you've never HEARD of minecraft, THEN put your hand down")
    prompt.wait()

    prompt.say("IF you've never USED minecraft, THEN put your hand down")
    prompt.wait()

    prompt.say("IF you've never CODED in python, THEN put your hand down")
    prompt.wait()


#--------------------------------------------------------------------------------

def sequence():
    pass
    #  cs unplugged process - sequence, selection, loops
    #  minecraft chat:
    #    put up left hand, delay
    #    put up right hand, delay
    #    put down both hands


#--------------------------------------------------------------------------------

def selection():
    pass
    #  minecraft chat:
    #    if you are a girl, put up left hand, delay
    #    put down your hand

#--------------------------------------------------------------------------------

def loops():
    pass
    #  minecraft chat:
    #    until I say stop, delay
    #      clap once
    #      wait 1 second
    #    (3 times) STOP!


#--------------------------------------------------------------------------------

def whatis():
    pass
    #    virtual Lego, never run out of bricks - it's a platform to build on
    #    survival mode, creative mode*
    #    moving (WASD space)
    #    building (E, left click, right click)
    #    coding...


#--------------------------------------------------------------------------------

def clear():
    pass
    # Get the player position
    #pos = mc.player.getTilePos()

    # Ask the user how big a space to clear
    #size = int(raw_input("size of area to clear? "))

    # Clear a space size by size*size*size, by setting it to AIR
    #mc.setBlocks(pos.x, pos.y, pos.z, pos.x+size, pos.y+size, pos.z+size,
    #             block.AIR.id)


#--------------------------------------------------------------------------------

def trampoline():
    pass
    # TRAMPOLINE() bouncing on a block, input and output in minecraft


#--------------------------------------------------------------------------------

def house():
    # Get the players position
    pos = mc.player.getPos()

    # Decide where to start building the house, slightly away from player
    x = pos.x + 2
    y = pos.y
    z = pos.z


    # A constant, that sets the size of your house
    SIZE = 20

    # Calculate the midpoints of the front face of the house
    midx = x+SIZE/2
    midy = y+SIZE/2  
    
    # Build the outer shell of the house
    mc.setBlocks(x, y, z, x+SIZE, y+SIZE, z+SIZE, block.COBBLESTONE.id)
    
    # Carve the insides out with AIR    
    mc.setBlocks(x+1, y, z+1, x+SIZE-2, y+SIZE-1, z+SIZE-2, block.AIR.id)

    # Carve out a space for the doorway
    mc.setBlocks(midx-1, y, z, midx+1, y+3, z, block.AIR.id)

    # Carve out the left hand window
    mc.setBlocks(x+3, y+SIZE-3, z, midx-3, midy+3, z, block.GLASS.id)
    
    # Carve out the right hand window    
    mc.setBlocks(midx+3, y+SIZE-3, z, x+SIZE-3, midy+3, z, block.GLASS.id)

    # Add a wooden roof  
    mc.setBlocks(x, y+SIZE, z, x+SIZE, y+SIZE, z+SIZE, block.WOOD.id)

    # Add a woolen carpet, the colour is 14, which is red.
    mc.setBlocks(x+1, y-1, z+1, x+SIZE-2, y-1, z+SIZE-2, block.WOOL.id, 14)
    



#--------------------------------------------------------------------------------

def maze():
    FILENAME = "maze.csv"

    # Define some constants for the different blocks you will use
    # to build your maze out of. This allows you to experiment with
    # different blocks and create interesting mazes
    GAP   = block.AIR.id
    WALL  = block.GOLD_BLOCK.id
    FLOOR = block.GRASS.id

    # This is the name of the file to read maze data from.
    # It is a constant, so that you can change it easily to read from
    # other data files in the future
    FILENAME = "maze1.csv"

    # Open the file containing your maze data
    f = open(FILENAME, "r")

    # Get the player position, and work out coordinates of the bottom corner
    # The x and z are moved slightly to make sure that the maze doesn't get
    # built on top of your players head
    pos = mc.player.getTilePos()
    ORIGIN_X = pos.x+1
    ORIGIN_Y = pos.y
    ORIGIN_Z = pos.z+1

    # The z coordinate will vary at the end of each line of data
    # So start it off at the origin of the maze
    z = ORIGIN_Z

    # Loop around every line of the file
        for line in f.readlines():
            # Split the line into parts, wherever there is a comma
            data = line.split(",")
  
            # Restart the x coordinate every time round the "for line" loop
            x = ORIGIN_X
  
            # This is a nested loop (a loop inside another loop)
            # It loops through every item in the "data" list
            # It loops through cells, just like cells in a spreadsheet
            for cell in data:
                # Check if this cell of data is a gap or a wall
                if cell == "0": # f.readlines read it in as a string, so use quotes
                    # choose the gap block id
                    b = GAP
                else:
                    # otherwise choose the wall block id
                    b = WALL
      
                # build two layers of the required block id (held in the b variable)
                mc.setBlock(x, ORIGIN_Y, z, b)
                mc.setBlock(x, ORIGIN_Y+1, z, b)
    
                # build one layer of floor underneath it
                mc.setBlock(x, ORIGIN_Y-1, z, FLOOR)
    
            # move to the next x coordinate at the end of this "for cell" loop
            x = x + 1
    
        # move to the next z coordinate at the end of this "for line" loop
        z = z + 1



#--------------------------------------------------------------------------------

def friend():
    import math
    import time

    #function get the distance between 2 points
    def distanceBetweenPoints(point1, point2):
        xd = point2.x - point1.x
        yd = point2.y - point1.y
        zd = point2.z - point1.z
        return math.sqrt((xd*xd) + (yd*yd) + (zd*zd))

    #constants
    # how far away the block has to be before he stops following
    TOO_FAR_AWAY = 15

    #create minecraft and minecraftstuff objects
    mc = minecraft.Minecraft.create()
    mcdrawing = minecraftstuff.MinecraftDrawing(mc)

    #set the blocks mood
    blockMood = "happy"

    #create the block next to the player
    friend = mc.player.getTilePos()
    friend.x = friend.x + 5
    # find out the height of the world at x, y, so the friend is on top
    friend.y = mc.getHeight(friend.x, friend.z)
    # create the block 
    mc.setBlock(friend.x, friend.y, friend.z, block.DIAMOND_BLOCK.id)
    # say hello
    mc.postToChat("<block> Hello friend")
    # the friends target is where he currently is
    target = friend.clone()

    while True:

        #get players position
        pos = mc.player.getTilePos()
        distance = distanceBetweenPoints(pos, friend)
        #apply the rules to work out where the block should be doing next
        # am I happy?
        if blockMood == "happy":
            #where is the player?  Are they near enough to me or should I move to them?
            if distance < TOO_FAR_AWAY:
                target = pos.clone()
            if distance >= TOO_FAR_AWAY:
                blockMood = "sad"
                mc.postToChat("<block> Come back. You are too far away. I need a hug!")
        # am I sad?
        elif blockMood == "sad":
            #if Im sad, I'll wait for my friend to come close and give me a hug before I'm happy again
            #print distance
            if distance <= 1:
                blockMood = "happy"
                mc.postToChat("<block> Awww thanks. Lets go.")

        #move block to the target
        if friend != target:
            #get the blocks in between block friend and player, by 'drawing' an imaginary line
            blocksBetween = mcdrawing.getLine(friend.x, friend.y, friend.z,
                                              target.x, target.y, target.z)
            #loop through the blocks in between the friend and the target
            # loop to the last but 1 block (:-1) otherwise the friend will be sitting on top of the player
            for blockBetween in blocksBetween[:-1]:
                #move the block friend to the next block
                # clear the old block by making it air
                mc.setBlock(friend.x, friend.y, friend.z, block.AIR.id)
                # set the position of the block friend to be the next block in-line
                friend = blockBetween.clone()
                # get the height of the land at the new position
                friend.y = mc.getHeight(friend.x, friend.z)
                # draw the block friend in the new position 
                mc.setBlock(friend.x, friend.y, friend.z, block.DIAMOND_BLOCK.id)
                # time to sleep between each block move
                time.sleep(0.25)
            # we have reached our target, so set the target to be friend's position
            target = friend.clone()

        #sleep for a little bit to give the computer a rest!
        time.sleep(0.25)


#--------------------------------------------------------------------------------

def maths():
    pass
    #  where's the maths?
    #    coordinates
    #    variables
    #    distance between points (pythagoras)

#--------------------------------------------------------------------------------

def other_topics():
    pass
    #  other topics? A few slides, tab over to PDF with these pictures on
    #    gemma 'programming with hammers' - teaches binary
    #    building school in minecraft (twitter)
    #    electronics - doing a workshop later
    #    history - archaeological dig in minecraft pics from twitter steven
    #    social interaction - multiplayer mode, rules "don't burn down his house"


#--------------------------------------------------------------------------------

def quotes():
    pass
    #   quotes from teachers:
    #     my kids *WANT* to do screen dumps
    #     [anon]

    #     after 180 children came to see a minecraft assembly, 45 were knocking on the
    #     door the next day wanting to set up a minecraft coding club.
    #     [Secondary school in Essex]

    #     I set assignmets in minecraft, I mark the kids homework in minecraft
    #     [SEN School in Bedfordshire]

    #   never underestimate how much attention you will get from kids when you
    #   say the word 'minecraft'
    #   [maker from cheshire]


#--------------------------------------------------------------------------------

def takeaways():
    pass
    #     Minecraft is a platform
    #     Children want to use it
    #     You can code it
    #     Children will bring their own ideas
    #     You don't have to be an expert, be a coach
    #     Its free and pre-installed on Raspberry Pi
    #     You can do this on mac/pc also
    #     Minecraft EDU for classroom licences

#--------------------------------------------------------------------------------

def microbit():
    #   Here is something we built with a 12 year old at computer club
    #   show Jamie's minecraft microbit
    #   hit button A, scrolls 'Hello' on the screen
    #   hit button B, scrolls 'Fun?" on the screen
    #   hit pad 0, scrolls 'THE END' on the screen.

#--------------------------------------------------------------------------------

def disasters():
    # run natural_disasters code (might do this interactively?)
    # import natural_disasters as nd
    # pos = mc.player.getTilePos()
    # x = pos.x
    # z = pos.z
    # nd.metor(x, z)
    # nd.geyser(x+20, z)
    # nd.earthquake(x+40, z)
    # nd.eruption(x+60, z)
    pass


#--------------------------------------------------------------------------------

def eval2():
    pass
    #   1. Have you heard of minecraft?
    #   2. Will you try minecraft?
    #   3. Will you try coding in python (with minecraft)?
    #   4. Come to my workshops later!


#----- MENU ---------------------------------------------------------------

quit_menu = False


def finished():
    global quit_menu
    quit_menu = True


menu_data = [
    (1,   "Countdown",            countdown),
    (2,   "Pre-eval",             eval1),
    (3,   "Sequence",             sequence),
    (4,   "Selection",            selection),
    (5,   "Loops",                loops),
    (6,   "What is Minecraft",    whatis),
    (7,   "Clear space",          clear),
    (8,   "Trampoline",           trampoline),
    (9,   "Build a house",        house),
    (10,  "Build a maze",         maze),
    (11,  "Block friend",         friend),
    (12,  "Detonator button",     detonator),
    (13,  "Where is the maths",   maths),
    (14,  "Other topics",         other_topics),
    (15,  "Quotes",               quotes),
    (16,  "Takeaways",            takeaways),
    (17,  "Microbit",             microbit),
    (18,  "Disaster!",            disasters),
    (19,  "Post evaluation",      eval2),
    ('q', "Finished",             finished)
]


def show_menu(menu=None):
    """Show all items in a menu, in order, labeled with a title"""
    if menu==None: menu=menu_data
    for item in menu:
	label, title, fn = item
        label = str(label)
        print("%s. %s " %(label, title))


def get_choice(menu):
    """Keep getting input until one matches a menu item"""
    while True:
        c = raw_input("? ")
        for i in menu:
            if str(i[0]) == c:
                return i
        print("unknown: " + c)


def menu():
    """Keep showing the menu until keyboard break"""
    global quit_menu
    quit_menu = False
    while not quit_menu:
        show_menu(menu_data)
        item = get_choice(menu_data)
        item[2]()


def reload():
    pass 
    # TODO do a module.reload(me) in case it was edited by programmer.


if __name__ == "__main__":
    print("keynote speech: loaded and ready!")
    connect()

# END


