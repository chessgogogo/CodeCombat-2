# Help your friends beat the minions that Thoktar sends against you.
# ����Ҫ���õ�װ���Ͳ���ȥӮ��ս����
# ��ǿ������ã������������������Ҫ�д�����Ŷ��



loop:
    flag = self.findFlag()
    enemy = self.findNearestEnemy()
    item = self.findNearestItem()
    if flag:
        self.moveXY(flag.pos.x, flag.pos.y)
        self.pickUpFlag(flag)
    if enemy:
        if self.isReady("cleave"):
            self.cleave(enemy)
        else:
                self.attack(enemy)


    
