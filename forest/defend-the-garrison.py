# ɱ�����н�����ʳ��ħ
# ʹ������Զ����ЩΣ�յ�ʳ��ħ

loop:
    enemy = self.findNearestEnemy()
    flag = self.findFlag("green")
    if flag:
        self.pickUpFlag(flag)
    if enemy and self.health > 100:
        if self.canElectrocute(enemy):
            self.electrocute(enemy)
        if self.isReady("cleave"):
            self.cleave(enemy)
        if self.isReady("bash"):
            self.bash(enemy)
        else:
            self.attack(enemy)
