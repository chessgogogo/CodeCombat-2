loop:
    enemy = self.findNearestEnemy()
    distance = self.distanceTo(enemy)
    if distance < 12:
        # ���������ũ��̫�����͹�������
        if self.isReady("cleave"):
           self.cleave(enemy)
        else:
           self.attack(enemy) 
        
    # ����Ļ�������ũ���Աߣ�
    else:
        self.moveXY(39, 36)
    
