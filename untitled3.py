

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from random import randrange

answer = randrange(0,16)
myID = mc.getPlayerEntityId("benny0331")

while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
        hit = hits[0]
        
        block = mc.getBlockWithData(hit.pos)
        data = block.data
        
        if data>answer :
            mc.postToChat('猜錯了雪莉')
        elif data<answer :
            mc.postToChat('猜錯了珍妮佛羅培茲')
        else :
            mc.setBlock(hit.pos,57)
            mc.postToTitle(myID,"你剛剛攻擊我的村莊?")
            break