import minecraft
import block
import time

mc=minecraft.Minecraft.create()

def dots(x,z,d):
    mc.setBlock(x, 11, z, block.SAND)
    time.sleep(1.2)
    mc.setBlock(x, 5, z, block.WOOL)
    mc.setBlock(x, 6, z, block.AIR)
    mc.setBlock(x, 6, z, block.AIR)
    d=d + 1
    return d
    
def bigdot(a, b, d):
           mc.setBlock(a, 5, b, block.WOOL)
           mc.setBlock(a, 6, b, block.WOOL)
           mc.setBlock(a, 7, b, block.WOOL)
           mc.setBlock(a+1, 6, b, block.WOOL)
           mc.setBlock(a-1, 6, b, block.WOOL)
           mc.setBlock(a, 6, b+1, block.WOOL)
           mc.setBlock(a, 6, b-1, block.WOOL)
           d=d+7
           return d
