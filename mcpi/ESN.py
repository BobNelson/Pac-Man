import minecraft
import block
import time

mc = minecraft.Minecraft.create()

for y in range(0,10):
    mc.setBlock(0, y, 0, block.WATER)
    mc.setBlock(1, y, 0, block.STONE)
    mc.setBlock(-1, y, 0, block.STONE)
    mc.setBlock(0, y, 1, block.STONE)
    mc.setBlock(0, y, -1, block.STONE)

mc.postToChat("Your spawn is a Stone Pillar")

time.sleep(5)

for x in range(0,10):
    mc.setBlock(1, y, 0, block.AIR)
    mc.setBlock(-1, y, 0, block.AIR)
    mc.setBlock(0, y, 1, block.AIR)
    mc.setBlock(0, y, -1, block.AIR)

mc.postToChat("RELEASE THE WATER")
