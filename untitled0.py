from mcpi.minecraft import Minecraft
mc = Minecraft.create()

The_man = []
Neil = []
Liang = []

for i in range(1,4):
    The_man.append(2*i)
for i in range(1,4):
    Neil.append(3*i)
for i in range(1,4):
    Liang.append(4*i)

x,y,z = mc.player.getPos()
mc.setSign(x,y,z,63,8,str(The_man),str(Neil),str(Liang))