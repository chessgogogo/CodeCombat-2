# ����ǰ�ߡ�
# ����κ�����Ż�һ�����ӡ�

loop:
    enemy = self.findNearestEnemy()
    flag = self.findFlag("green")
    if flag:
        self.moveXY(flag.pos.x, flag.pos.y)
        self.pickUpFlag(flag)
    if enemy:
        if self.isReady("bash"):
            self.bash(enemy)
        else:
            self.attack(enemy)