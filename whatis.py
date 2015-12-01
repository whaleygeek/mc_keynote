# whatis.py  26/11/2015  D.J.Whale

#WHATIS()
#    virtual Lego, never run out of bricks - it's a platform to build on
#    survival mode, creative mode*
#    moving (WASD space)
#    building (E, left click, right click)
#    coding...

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

