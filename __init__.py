import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import anyio.GPIO as GPIO
import time

class DummyPrompt():
    def say(self, msg):
        print(msg)


    def wait(self):
        raw_input("?") # python2


class Prompt():
    def __init__(self, mc, gpio, pin=4):
        self.mc   = mc
        self.gpio = gpio
        self.pin  = pin
        gpio.setup(pin, gpio.IN)


    def say(self, msg):
        print("SAY:" + str(msg))
        self.mc.postToChat(msg)


    def wait(self):
        print("WAIT...")
        # wait for press
        while self.gpio.input(self.pin) == True:
            time.sleep(0.1)
        print("v") # DEBUG

        # wait for release
        while self.gpio.input(self.pin) == False:
            time.sleep(0.1)
        print("^") # DEBUG


mc = None
prompt = None

def connect():
    global mc, prompt
    mc = minecraft.Minecraft.create()
    prompt = Prompt(mc, GPIO, 4)
    #prompt = DummyPrompt()

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

    audio.play("mc_keynote/countdown.wav")
    for secs in range(30):
        mc_clock.draw_secs(secs, block.GOLD_BLOCK.id)
        time.sleep(1)
        mc_clock.draw_secs(secs, block.AIR.id)

    #audio.play("bang.wav")
    mc_clock.clear_face()

#--------------------------------------------------------------------------------

def eval1():
    prompt.say("EVALUATION")
    prompt.wait()
    
    prompt.say("Put up your hand")
    prompt.wait()

    prompt.say("IF you've never HEARD of minecraft")
    prompt.say("THEN put your hand down")
    prompt.wait()

    prompt.say("IF you've never USED minecraft")
    prompt.say("THEN put your hand down")
    prompt.wait()

    prompt.say("IF you've never CODED in python")
    prompt.say("THEN put your hand down")


#--------------------------------------------------------------------------------

def sequence():
    prompt.say("SEQUENCE")
    prompt.wait()
    
    prompt.say("Put up your left hand")
    prompt.wait()

    prompt.say("Put up your right hand")
    prompt.wait()

    prompt.say("Put down both hands")


#--------------------------------------------------------------------------------

def selection():
    prompt.say("SELECTION")
    prompt.wait()

    prompt.say("IF you are a girl")
    prompt.say("THEN put up your left hand")

    prompt.wait()
    prompt.say("Put down your hand")
    
#--------------------------------------------------------------------------------

def loops():
    prompt.say("LOOPS")
    prompt.wait()

    prompt.say("UNTIL I say STOP")
    prompt.say("    Clap once")
    prompt.say("    wait 1 second")

    time.sleep(3)
    prompt.say("(keep going - this is fun!)")

    prompt.wait()

    prompt.say("STOP!")


#--------------------------------------------------------------------------------

def whatis():
    prompt.say("What is Minecraft?")
    prompt.wait()

    prompt.say("- virtual lego")
    time.sleep(1)
    prompt.say("  never run out of bricks!")
    prompt.wait()

    prompt.say("- survival mode and creative mode")
    time.sleep(1)
    prompt.say("  limited resources you must mine")
    time.sleep(1)
    prompt.say(" vs unlimited resources")
    prompt.wait()

    prompt.say("- you can code it in Python!")
    
     

#--------------------------------------------------------------------------------

def clear():
    prompt.say("Let's clear some space...")
    time.sleep(1)
    prompt.say("Move your player to somewhere")
    prompt.wait()

    pos = mc.player.getTilePos()
    prompt.say("let's clear 10 blocks")

    # in case we are using a 'flat' world, make sure there is a bit of bottom!
    mc.setBlocks(pos.x-5, pos.y-2, pos.z-5, pos.x+5, pos.y-10, pos.z+5, block.STONE.id)
    mc.setBlocks(pos.x-5, pos.y-1, pos.z-5, pos.x+5, pos.y+10, pos.z+5, block.AIR.id)
    mc.postToChat("BANG!")    


#--------------------------------------------------------------------------------

def trampoline():
    prompt.say("What about a trampoline?")
    time.sleep(1)

    pos = mc.player.getTilePos()
    mc.setBlock(pos.x, pos.y-1, pos.z, block.WOOL.id, 14)

    mc.player.setTilePos(pos.x, pos.y, pos.z-2)
    prompt.say("Stand on the wool mat for some magic!")

    while True:
        time.sleep(0.1)
        pos = mc.player.getTilePos()
        b = mc.getBlock(pos.x, pos.y-1, pos.z)
        if b == block.WOOL.id:
            mc.player.setTilePos(pos.x, pos.y+20, pos.z)
            mc.postToChat("YIPPEE!!")


#--------------------------------------------------------------------------------

def house():
    prompt.say("How about a house to keep you safe?")
    prompt.wait()
    
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

    prompt.say("There you go - have a walk around your new house!")
    time.sleep(2)
    prompt.say("Did I tell you that you owe me 500 thousand pounds?!")
    time.sleep(2)
    prompt.say("(payment in mcpi.block.GOLD_BLOCK's please!)")

    prompt.wait()
    pos = mc.player.getTilePos()
    mc.setBlocks(pos.x+2, pos.y, pos.z+10, pos.x+10, pos.y+10, pos.z+20, block.GOLD_BLOCK.id)
    mc.postToChat("KER-CHING!")
    

    
#--------------------------------------------------------------------------------

def maze():
    prompt.say("Mazes use data files (CSV)")
    prompt.wait()
    
    # Define some constants for the different blocks you will use
    # to build your maze out of. This allows you to experiment with
    # different blocks and create interesting mazes
    GAP   = block.AIR.id
    WALL  = block.GOLD_BLOCK.id
    FLOOR = block.GRASS.id

    # This is the name of the file to read maze data from.
    # It is a constant, so that you can change it easily to read from
    # other data files in the future
    FILENAME = "mc_keynote/maze1.csv"

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
        data = line.strip()
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

    prompt.say("Can you solve the maze?")
    time.sleep(2)
    prompt.say("Remember you can fly - double tap space!")
    time.sleep(2)
    prompt.say("...but that is CHEATING!")
    

#--------------------------------------------------------------------------------

def friend():
    prompt.say("How about an intelligent block?")
    prompt.wait()
    
    prompt.say("Let me introduce you to Kevin... he's shiney!")
    
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
                mc.postToChat("<block> Awww thanks. Lets go!")

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
    prompt.say("But where is the maths?")
    prompt.wait()

    prompt.say("- coordinates (3D x/y/z)")
    prompt.wait()

    prompt.say("- variables (algebra)")
    prompt.wait()

    prompt.say("- pythagoras - distance between points")
    time.sleep(1)
    
    prompt.say("def distanceBetweenPoints(point1 point2):")
    time.sleep(0.25)
    prompt.say("    xd = point2.x - point1.x")
    time.sleep(0.25)
    prompt.say("    yd = point2.y - point1.y")
    time.sleep(0.25)
    prompt.say("    zd = point2.z - point1.z")
    time.sleep(0.25)
    prompt.say("    return math.sqrt((xd*xd)+(yd*yd)+(zd*zd))")
    
    
#--------------------------------------------------------------------------------

def other_topics():
    prompt.say("What about other topics?")
    prompt.say("Electronics?")
    prompt.wait()

    prompt.say("Social interaction?")
    time.sleep(1)
    prompt.say("Rule 1: Don't burn down someone's house")
    prompt.wait()
    
    prompt.say("History? Archaeology?")
 

#--------------------------------------------------------------------------------

def quotes():
    prompt.say("What do people say about it...")
    prompt.wait()

    prompt.say("my kids *WANT* to do screen dumps")
    prompt.wait()

    prompt.say("180 children came to your assembly...")
    time.sleep(1)
    prompt.say("next day 45 were knocking on my door")
    prompt.say("they wanted to set up minecraft coding club!")
    time.sleep(1)
    prompt.say("Yes that's ONE QUARTER!!")
    prompt.wait()

    prompt.say("I set assignments in minecraft")
    prompt.say("I mark the kids homework in minecraft")
    time.sleep(1)
    prompt.say("[SEN School in Bedfordshire]")
    prompt.wait()

    prompt.say("Never underestimate how much attention you get from kids")
    prompt.say("when you say the word MINECRAFT!")
    time.sleep(1)
    prompt.say("[workshop leader from Cheshire]")
    

#--------------------------------------------------------------------------------

def takeaways():
    prompt.say("What can you take away from this talk?")
    prompt.wait()

    prompt.say("1. Minecraft is a platform")
    prompt.wait()

    prompt.say("2. Children WANT to use it")
    prompt.wait()

    prompt.say("3. You can learn coding with it")
    prompt.wait()

    prompt.say("4. Children will bring their own ideas")
    prompt.wait()

    prompt.say("5. It's free and pre-installed on Raspberry Pi")
    prompt.wait()

    prompt.say("6. School site licences for use on PC/Mac ")


#--------------------------------------------------------------------------------

def microbit():
    prompt.say("Has anyone heard about the BBC micro:bit??")
    time.sleep(2)
    prompt.say("... 12 year old Jamie built one in Minecraft!!")

    print("DO: python    import mc_minecraft as m")

    
#--------------------------------------------------------------------------------

def disasters():
    prompt.say("Oh no it's a disaster....")
    time.sleep(1)
    prompt.say("Look what a 10 year old built with code...")

    print("DO: python    import natural_disasters")
    print("meteor_shower, geyser, earthquake, eruption")


#--------------------------------------------------------------------------------

def eval2():
    prompt.say("Let's check again...")
    prompt.say("Have you heard of minecraft?")
    prompt.wait()

    prompt.say("Will you try minecraft?")
    prompt.wait()

    prompt.say("Will you try coding in Python?")
    time.sleep(2)
    prompt.say("P.S. Come to my workshops later!")

    print("DO: Play closing video")

    
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
    (12,  "Where is the maths",   maths),
    (13,  "Other topics",         other_topics),
    (14,  "Quotes",               quotes),
    (15,  "Takeaways",            takeaways),
    (16,  "Microbit",             microbit),
    (17,  "Disaster!",            disasters),
    (18,  "Post evaluation",      eval2),
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


if __name__ == "__main__":
    print("keynote speech: loaded and ready!")
    connect()

# END


