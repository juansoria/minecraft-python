from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()
while True:
    pos = mc.player.getPos()
    mc.setBlocks(pos.x - 2 , pos.y - 1, pos.z - 2, pos.x + 2, pos.y - 1, pos.z +2, 57)
    mc.setBlocks(pos.x , pos.y, pos.z, pos.x, pos.y + 4, pos.z, 0)


