from mcpi.minecraft import Minecraft as mc
import time 
time.sleep(5)
mcs = mc.create()
x,y,z=mcs.player.getTilePos()
s=40
mc.setBlock(x+s,y-s,z+s,x-s,y,z-s,0)