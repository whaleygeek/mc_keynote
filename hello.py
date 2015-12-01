import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
mc.postToChat("hello Anya")

pos = mc.player.getTilePos()
mc.setBlock(pos.x, pos.y-1, pos.z, block.WOOL.id, 7)

while True:
    pos = mc.player.getTilePos()
    b = mc.getBlock(pos.x, pos.y-1, pos.z)
    if b == block.WOOL.id:
        mc.player.setTilePos(pos.x, pos.y+20, pos.z)
        mc.postToChat("YIPPEE!!!")
        
