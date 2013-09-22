import minecraft
import block
import time
import random
import dots

d=0
mc = minecraft.Minecraft.create()
#Gives an intro
mc.postToChat("Pac-Man")
time.sleep(1.5)
mc.postToChat("Made By Robert Nelson")
time.sleep(1.5)
mc.postToChat("Building Course...")
#Creates the box
for x in xrange(15, 64):
    for y in xrange(4, 9):
        for z in xrange(-1, 65):
            if(x==15 or x==63 or y==4 or y==9 or z==-1 or z==64):    
                mc.setBlock(x, y, z, block.OBSIDIAN)
#Creates the doorway and stairs
for x in xrange(39, 41):
    for y in xrange(5, 8):
        mc.setBlock(x, y, -1, block.AIR)
for x in xrange(38, 42):
    for y in xrange(4, 5):
        for z in xrange(-2, -1):
            mc.setBlock(x, y, z, block.STONE_SLAB)
#Tells the player what's happening
mc.postToChat("Building Obstacles")
#Creates the blocks in the first row of the course
for x in xrange(44, 60):
    for y in xrange(5, 8):
        for z in xrange(3, 5):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(48, 50):
    for y in xrange(5, 8):
        for z in xrange(5, 11):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(19, 35):
    for y in xrange(5, 8):
        for z in xrange(3, 5):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(31, 33):
    for y in xrange(5, 8):
        for z in xrange(3, 5):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(39, 41):
    for y in xrange(5, 8):
        for z in xrange(3, 10):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(35, 45):
    for y in xrange(5, 8):
        for z in xrange(9, 11):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(29, 31):
    for y in xrange(5, 8):
        for z in xrange(5, 11):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)
#Creates second row
for x in xrange(58, 63):
    for y in xrange(5, 8):
        for z in xrange(8, 10):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(16, 21):
    for y in xrange(5, 8):
        for z in xrange(8, 10):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(24, 26):
    for y in xrange(5, 8):
        for z in xrange(8, 15):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(19, 26):
    for y in xrange(5, 8):
        for z in xrange(13, 15):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(53, 55):
    for y in xrange(5, 8):
        for z in xrange(8, 15):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(54, 60):
    for y in xrange(5, 8):
        for z in xrange(13, 15):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)
#Creates third row
for x in xrange(44, 50):
    for y in xrange(5, 8):
        for z in xrange(14, 16):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(36, 30):
    for y in xrange(5, 8):
        for z in xrange(14, 16):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(39, 41):
    for y in xrange(5, 8):
        for z in xrange(14, 19):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(35, 45):
    for y in xrange(5, 8):
        for z in xrange(19, 21):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(29, 36):
    for y in xrange(5, 8):
        for z in xrange(14, 16):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)
#Creates fourth row
for x in xrange(53, 63):
    for y in xrange(5, 8):
        for z in xrange(19, 21):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(53, 55):
    for y in xrange(5, 8):
        for z in xrange(21, 34):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(55, 63):
    for y in xrange(5, 8):
        for z in xrange(32, 34):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(48, 50):
    for y in xrange(5, 8):
        for z in xrange(19, 29):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(30, 32):
    for y in xrange(5, 8):
        for z in xrange(19, 29):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(16, 27):
    for y in xrange(5, 8):
        for z in xrange(19, 21):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(25, 27):
    for y in xrange(5, 8):
        for z in xrange(21, 34):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(16, 25):
    for y in xrange(5, 8):
        for z in xrange(32, 34):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)
#Creates the ghost box           
for x in xrange(35, 45):
    for y in xrange(5, 8):
        for z in xrange(27, 35):
            if (x==35 or x==44 or y==4 or y==8 or z==27 or z==34):
                mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(39, 41):
    for y in xrange(4, 8):
        for z in xrange(34, 35):
            mc.setBlock(x, y, z, block.AIR)

for x in xrange(39, 41):
    for y in xrange(4, 5):
        for z in xrange(34, 35):
            mc.setBlock(x, y, z, block.WOOL)
            
#Creates the fourth row
for x in xrange(53, 63):
    for y in xrange(5, 8):
        for z in xrange(37, 39):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(53, 55):
    for y in xrange(5, 8):
        for z in xrange(39, 49):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(55, 63):
    for y in xrange(5, 8):
        for z in xrange(47, 49):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(16, 27):
    for y in xrange(5, 8):
        for z in xrange(37, 39):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(25, 27):
    for y in xrange(5, 8):
        for z in xrange(38, 49):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(16, 25):
    for y in xrange(5, 8):
        for z in xrange(47, 49):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(30, 32):
    for y in xrange(5, 8):
        for z in xrange(32, 49):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(32, 36):
    for y in xrange(5, 8):
        for z in xrange(38, 40):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(48, 50):
    for y in xrange(5, 8):
        for z in xrange(32, 49):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(44, 48):
    for y in xrange(5, 8):
        for z in xrange(38, 40):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)
#Creates fifth row
for x in xrange(39, 41):
    for y in xrange(5, 8):
        for z in xrange(40, 47):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(35, 45):
    for y in xrange(5, 8):
        for z in xrange(47, 49):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(53, 60):
    for y in xrange(5, 8):
        for z in xrange(52, 54):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(17, 25):
    for y in xrange(5, 8):
        for z in xrange(54, 52):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(38, 40):
    for y in xrange(5, 8):
        for z in xrange(54, 64):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(53, 60):
    for y in xrange(5, 8):
        for z in xrange(57, 61):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)


for x in xrange(43,  50):
    for y in xrange(5, 8):
        for z in xrange(54, 61):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(19, 25):
    for y in xrange(5, 8):
        for z in xrange(57, 61):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(28, 35):
    for y in xrange(5, 8):
        for z in xrange(54, 61):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

for x in xrange(19, 25):
    for y in xrange(5, 8):
        for z in xrange(52, 54):
            mc.setBlock(x, y, z, block.LAPIS_LAZULI_BLOCK)

mc.postToChat("Placing Dots...")
time.sleep(1)
mc.postToChat("Takes about 5 minutes")
time.sleep(1)
#Places Dots using my dots module
for x in range(19, 38, 2):
    d=dots.dots(x, 1, d)
for x in range(42, 59, 2):
    d=dots.dots(x, 1, d)

d=dots.dots(42, 3, d)
d=dots.dots(42, 5, d)
d=dots.dots(44, 6, d)
d=dots.dots(46, 6, d)
d=dots.dots(46, 8, d)
d=dots.dots(46, 10, d)
d=dots.dots(37, 3, d)
d=dots.dots(37, 5, d)
d=dots.dots(35, 6, d)
d=dots.dots(33, 6, d)
d=dots.dots(33, 8, d)
d=dots.dots(33, 10, d)
d=dots.dots(61, 3, d)
d=dots.dots(61, 5, d)
d=dots.dots(17, 3, d) 
d=dots.dots(17, 5, d)

for x in range(19, 27, 2):
    d=dots.dots(x, 6, d)
for x in range(60, 51, -2):
    d=dots.dots(x, 6, d)
for z in range(8, 15, 2):
    d=dots.dots(51, z, d)
for z in range(8, 15, 2):
    d=dots.dots(27, z, d)
for x in range(30, 49, 2):
    d=dots.dots(x, 12, d)

d=dots.dots(56, 8, d)
d=dots.dots(57, 10, d)
d=dots.dots(56, 11, d)
d=dots.dots(59, 11, d)
d=dots.dots(61, 12, d)
d=dots.dots(61, 14, d)
d=dots.dots(61, 16, d)

for x in range(60, 44, -2):
    d=dots.dots(x, 17, d)

d=dots.dots(42, 16, d)
d=dots.dots(42, 14, d)
d=dots.dots(22, 8, d)
d=dots.dots(22, 10, d)
d=dots.dots(20, 11, d)
d=dots.dots(17, 12, d)
d=dots.dots(17, 14, d)
d=dots.dots(17, 16, d)

for x in range(20, 37, 2):
    d=dots.dots(x, 17, d)

d=dots.dots(37, 16, d)
d=dots.dots(37, 14, d)

for z in range(20, 49, 2):
    d=dots.dots(51, z, d)
for z in range(20, 49, 2):
    d=dots.dots(28, z, d)
for z in range(19, 34, 2):
    d=dots.dots(46, z, d)
for z in range(19, 34, 2):
    d=dots.dots(33, z, d)

d=dots.dots(37, 40, d)
d=dots.dots(37, 42, d)
d=dots.dots(37, 44, d)
d=dots.dots(35, 45, d)
d=dots.dots(33, 46, d)
d=dots.dots(33, 48, d)
d=dots.dots(42, 40, d)
d=dots.dots(42, 42, d)
d=dots.dots(42, 44, d)
d=dots.dots(44, 45, d)
d=dots.dots(46, 45, d)
d=dots.dots(46, 47, d)

for x in range(62, 16, -2):
    d=dots.dots(x, 50, d)
for x in range(26, 51, 2):
    d=dots.dots(x, 52, d)
for z in range(51, 60, 2):
    d=dots.dots(17, z, d)
for x in range(20, 35, 2):
    d=dots.dots(x, 62, d)
for z in range(62, 53, -2):
    d=dots.dots(36, z, d)
for x in range(18, 25, 2):
    d=dots.dots(x, 55, d)
for z in range(60, 52, -2):
    d=dots.dots(26, z, d)
for z in range(52, 61, 2):
    d=dots.dots(61, z, d)
for x in range(58, 41, -2):
    d=dots.dots(x, 62, d)
for z in range(61, 54, -2):
    d=dots.dots(41, z, d)
for z in range(54, 61, 2):
    d=dots.dots(51, z, d)
for x in range(53, 60, 2):
    d=dots.dots(x, 55, d)
    
d=dots.bigdot(61, 1, d)
d=dots.bigdot(17, 1, d)
d=dots.bigdot(61, 62, d)
d=dots.bigdot(17, 62, d)
d=dots.bigdot(34, 42, d)
d=dots.bigdot(45, 42, d)
d=dots.bigdot(43, 22, d)
d=dots.bigdot(36, 25, d)

mc.postToChat("And the Cherry on top")

mc.setBlock(40, 5, 24, block.TNT)
mc.setBlock(39, 5, 24, block.TNT)
mc.setBlock(40, 5, 23, block.TNT)
mc.setBlock(39, 5, 23, block.TNT)
mc.setBlock(40, 5, 25, block.TNT)
mc.setBlock(41, 5, 24, block.TNT)
mc.setBlock(41, 5, 23, block.TNT)
mc.setBlock(39, 5, 25, block.TNT)
mc.setBlock(38, 5, 24, block.TNT)
mc.setBlock(38, 5, 23, block.TNT)
mc.setBlock(39, 5, 22, block.TNT)
mc.setBlock(40, 5, 22, block.TNT)

mc.player.setPos(40.5, 5, 1.5)
mc.postToChat("Ready?")
time.sleep(1)
mc.postToChat("3")
time.sleep(1)
mc.postToChat("2")
time.sleep(1)
mc.postToChat("1")
time.sleep(1)
mc.postToChat("GO")

t=0
d = d + 48

mc.postToChat("You have " + str(int(t)) + " out of " + str(int(d)) + " dots")

while t < d:
    if 77 < mc.player.getPos().x < 79 and 43 < mc.player.getPos().z < 45 and 4 < mc.player.getPos().y < 7:
        mc.player.setPos(34.5, 5, 44.5)
    if 31 < mc.player.getPos().x < 33 and 43 < mc.player.getPos().z < 45 and 4 < mc.player.getPos().Y < 7:
        mc.player.setPos(76.5, 5, 44.5)
    if 77 < mc.player.getPos().x < 79 and 44 < mc.player.getPos().z < 46 and 4 < mc.player.getPos().y < 7:
        mc.player.setPos(34.5, 5, 45.5)
    if 31 < mc.player.getPos().x < 33 and 44 < mc.player.getPos().z < 46 and 4 < mc.player.getPos().y < 7:
        mc.player.setPos(76.5, 5, 45.5)
    if 77 < mc.player.getPos().x < 79 and 45 < mc.player.getPos().z < 47 and 4 < mc.player.getPos().y < 7:
        mc.player.setPos(34.5, 5, 46.5)
    if 31 < mc.player.getPos().x < 33 and 45 < mc.player.getPos().z < 47 and 4 < mc.player.getPos().y < 7:
        mc.player.setPos(76.5, 5, 46.5)
    hits = mc.events.pollBlockHits()
    for hit in hits:
        blockType = mc.getBlockWithData(hit.pos.x, hit.pos.y, hit.pos.z)
        if (blockType == block.WOOL):
            t = t + 1
            mc.setBlock(hit.pos.x, hit.pos.y, hit.pos.z, block.AIR)
            mc.postToChat("Added +1 to score you now have " + str(int(t)) + " out of " + str(int(d)) + " dots")                                                            
        if (blockType == block.TNT):
            t = t + 4
            mc.setBlock(hit.pos.x, hit.pos.y, hit.pos.z, block.AIR)
            mc.postToChat("Added +4 to score you now have " + str(int(t)) + " out of " + str(int(d)) + " dots")
        
mc.postToChat("You Win!!!")
time.sleep(1)
mc.postToChat("Good Game")

