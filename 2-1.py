from mcpi.minecraft import Minecraft
mc = Minecraft.create()
a = input('你是誰')

postToChat('Hello'+a+',今天天氣真好,我家門前有小河後面有山坡')
x,y,z = mc.player.getTilePos()
mc.setBlocks(x,y,z,x+10,y+15,z+10,100)
mc.setBlocks(x+1,y+1,z+1,x+9,y+14,z+9,0)
mc.setBlocks(x+6,y+1,z,+6,y+2,z,0)