# �ھ����л��ܵ��˵�Ӣ�ۣ�

loop:
    enemy = self.findNearestEnemy()
    if self.isReady("cleave"):
        self.cleave(enemy)
    else:
        self.attack(enemy)
