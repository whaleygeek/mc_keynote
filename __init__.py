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
    pass

#--------------------------------------------------------------------------------

def sequence():
    pass

#--------------------------------------------------------------------------------

def selection():
    pass

#--------------------------------------------------------------------------------

def loops():
    pass

#--------------------------------------------------------------------------------

def whatis():
    pass

#--------------------------------------------------------------------------------

def clear():
    pass

#--------------------------------------------------------------------------------

def trampoline():
    pass

#--------------------------------------------------------------------------------

def house():
    pass

#--------------------------------------------------------------------------------

def maze():
    pass

#--------------------------------------------------------------------------------

def friend():
    pass

#--------------------------------------------------------------------------------

def detonator():
    pass

#--------------------------------------------------------------------------------

def maths():
    pass

#--------------------------------------------------------------------------------

def other_topics():
    pass

#--------------------------------------------------------------------------------

def quotes():
    pass

#--------------------------------------------------------------------------------

def takeaways():
    pass

#--------------------------------------------------------------------------------

def microbit():
    pass

#--------------------------------------------------------------------------------

def eval2():
    pass


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


def reload():
    pass 
    # TODO do a module.reload(me) in case it was edited by programmer.


if __name__ == "__main__":
    print("keynote speech: loaded and ready!")
    connect()

# END


