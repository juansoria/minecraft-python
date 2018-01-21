# Good seed (Seed: 4307913003093348390) 
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()
while True:
    pos = mc.player.getPos()
    mc.setBlocks(pos.x - 2 , pos.y - 1, pos.z - 2, pos.x + 2, pos.y - 1, pos.z +2, 1)
    mc.setBlocks(pos.x , pos.y, pos.z, pos.x + 3, pos.y + 4, pos.z + 3, 0)
    mc.setBlock(pos.x - 2 , pos.y , pos.z - 2, 89)
    mc.setBlock(pos.x + 2 , pos.y , pos.z + 2, 89)
