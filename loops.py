# loops.py  26/11/2015  D.J.Whale

#LOOPS()
#  minecraft chat:
#    until I say stop, delay
#      clap once
#      wait 1 second
#    (3 times) STOP!

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