# microbit.py  26/11/2015  D.J.Whale

#MICROBIT()
#extension:
#   Here is something we built with a 12 year old at computer club
#   show Jamie's minecraft microbit
#   hit button A, scrolls 'Hello' on the screen
#   hit button B, scrolls 'Fun?" on the screen
#   hit pad 0, scrolls 'THE END' on the screen.

mc     = None
prompt = None

def init(presenter):
    global mc, prompt
    mc     = presenter.mc
    prompt = presenter.prompt


def run(presenter):
    init(presenter)
    # TODO script here


# END