import time

import mc_clock
import audio

mc    = None
block = None

def init(presenter):
    global mc
    mc    = presenter.mc
    block = presenter.block


def run(presenter):
    init(presenter)

    pos = mc.player.getTilePos()

    mc_clock.init(mc)
    mc_clock.draw_face(pos)

    for secs in range(30,0,-1):
        mc_clock.draw_secs(secs, mc_clock.SEC_HAND_BLOCKID)
        time.sleep(1)
        mc_clock.draw_secs(secs, block.AIR.id)
        if secs <= 5:
            audio.play("%d.wav" % secs)

    audio.play("bang.wav")
    mc_clock.clear_face()

# END
