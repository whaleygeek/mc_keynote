# clock.py - reusable module version  D.J.Whale  25/11/2015

import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff

import time
import datetime
import math


CLOCK_RADIUS      = 20
HOUR_HAND_LENGTH  = 10
MIN_HAND_LENGTH   = 18
SEC_HAND_LENGTH   = 20

FACE_BLOCKID      = block.DIAMOND_BLOCK.id
HOUR_HAND_BLOCKID = block.DIRT.id
MIN_HAND_BLOCKID  = block.WOOD_PLANKS.id
SEC_HAND_BLOCKID  = block.STONE.id


mcdrawing   = None
clockMiddle = None


def findPointOnCircle(cx, cy, radius, angle):
    x = cx + math.sin(math.radians(angle)) * radius
    y = cy + math.cos(math.radians(angle)) * radius
    x = int(round(x, 0))
    y = int(round(y, 0))
    return(x,y)


def draw_face(pos):
    """Draw the basics of the clock"""

    global clockMiddle

    #create clock face above the player
    clockMiddle = pos
    clockMiddle.y = clockMiddle.y + 25

    #use mc drawing object to draw the circle of the clock face
    mcdrawing.drawCircle(clockMiddle.x, clockMiddle.y, clockMiddle.z,
                     CLOCK_RADIUS, FACE_BLOCKID)


def clear_face():
    """Clear the clock face when finished with it"""

    mcdrawing.drawCircle(clockMiddle.x, clockMiddle.y, clockMiddle.z,
                     CLOCK_RADIUS, block.AIR.id)



def draw_hours(hours, blockid):

    # what angle would a hour hand point to
    hourHandAngle = (360 / 12) * hours

    hourHandX, hourHandY = findPointOnCircle(clockMiddle.x, clockMiddle.y,
                                             HOUR_HAND_LENGTH, hourHandAngle)

    mcdrawing.drawLine(clockMiddle.x, clockMiddle.y, clockMiddle.z,
                       hourHandX, hourHandY, clockMiddle.z,
                       blockid)


def draw_mins(minutes, blockid):

    # what angle would a minute hand point to
    minHandAngle = (360 / 60) * minutes

    minHandX, minHandY = findPointOnCircle(clockMiddle.x, clockMiddle.y,
                                           MIN_HAND_LENGTH, minHandAngle)

    mcdrawing.drawLine(clockMiddle.x, clockMiddle.y, clockMiddle.z - 1,
                       minHandX, minHandY, clockMiddle.z-1,
                       blockid)


def draw_secs(seconds, blockid):

    # what angle would a second hand point to
    secHandAngle = (360 / 60) * seconds

    secHandX, secHandY = findPointOnCircle(clockMiddle.x, clockMiddle.y,
                                           SEC_HAND_LENGTH, secHandAngle)

    mcdrawing.drawLine(clockMiddle.x, clockMiddle.y, clockMiddle.z+1,
                       secHandX, secHandY, clockMiddle.z+1,
                       blockid)


def draw_hands(hours, minutes, seconds):
    """Draw hands of the clock"""

    draw_hours(hours,  HOUR_HAND_BLOCKID)
    draw_mins(minutes, MIN_HAND_BLOCKID)
    draw_secs(seconds, SEC_HAND_BLOCKID)


def clear_hands(hours, minutes, seconds):
    """clear the time by drawing over the hands with AIR"""

    draw_hours(hours,  block.AIR.id)
    draw_mins(minutes, block.AIR.id)
    draw_secs(seconds, block.AIR.id)


def init(mc):
    global mcdrawing
    mcdrawing = minecraftstuff.MinecraftDrawing(mc)


def run(mc):
    init(mc)

    pos = mc.player.getTilePos()
    draw_face(pos)

    try:
        while True:
	    timeNow = datetime.datetime.now()
    	    hours = timeNow.hour
            if hours >= 12:
                hours = timeNow.hour - 12
            minutes = timeNow.minute
            seconds = timeNow.second
    
            draw_hands(hours, minutes, seconds)
            time.sleep(1)
            clear_hands(hours, minutes, seconds)

    except KeyboardException:
        clear_hands(hours, minutes, seconds)
        clear_face()
        print("Clock stopped")

# END



