from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getPos()

mc.setBlock(x-50,y-50,z-50,x+50,y+50,z+50,95)
mc.setBlock(x-49,y-49,z-49,x+49,y+49,z+49,0)
