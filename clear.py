# clear.py  26/11/2015  D.J.Whale

# CLEAR() clear a load of space to build

# Get the player position
#pos = mc.player.getTilePos()

# Ask the user how big a space to clear
#size = int(raw_input("size of area to clear? "))

# Clear a space size by size*size*size, by setting it to AIR
#mc.setBlocks(pos.x, pos.y, pos.z, pos.x+size, pos.y+size, pos.z+size,
#             block.AIR.id)


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

# END
