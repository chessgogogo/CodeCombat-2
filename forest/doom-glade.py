# һ��ʳ��ħ������ʹ������Ӯ��ս�ۣ�

loop:
    enemy =self.findNearestEnemy()
    flag = self.findFlag("green")
    if flag:
        self.moveXY(flag.pos.x, flag.pos.y)
        self.pickUpFlag(flag)
    if enemy:
        if self.isReady("bash"):
            self.bash(enemy)
        elif self.isReady("cleave"):
            self.cleave(enemy)
        else:
            self.attack(enemy)
            
