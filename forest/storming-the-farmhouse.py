# ʿ���������������ʳ��ħ����û���ǡ�
# �����Ĺ���ѭ���ǲ��ܹ������������

loop:
    flag = self.findFlag()
    enemy = self.findNearestEnemy()
    
    if flag:
        self.moveXY(flag.pos.x, flag.pos.y)
        self.pickUpFlag(flag)
    if enemy:
        distance = self.distanceTo(enemy)
        if self.isReady("cleave"):
            self.cleave(enemy)
        elif self.isReady("bash"):
            self.bash(enemy)
        else:
            self.attack(enemy)
            
