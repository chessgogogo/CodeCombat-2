# ��������������Сʳ��ħ
# ȷ�������㹻�Ļ��ס�

loop:
    enemy = self.findNearestEnemy()
    if self.isReady("cleave"):
        self.cleave(enemy)
    else:
        self.shield()
        
