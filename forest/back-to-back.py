# �����м����

loop:
    enemy = self.findNearestEnemy()
    if enemy:
        # ��������
       self.attack(enemy) 
        
    else:
        # �ص������ط���
        self.moveXY(40, 37)