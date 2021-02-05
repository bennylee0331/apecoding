from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

x,y,z = mc.player.getPos()
mc.setBlock(x,y,z,8)