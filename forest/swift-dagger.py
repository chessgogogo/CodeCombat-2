# ����������Ĺ����̾�����ذ��

loop:
    enemy = self.findNearestEnemy()
    if enemy:
        distance = self.distanceTo(enemy)
        if distance < self.throwRange:
            # ����������ذ��
            self.throw(enemy)
        else:
            # ����Ĺ���������
            self.attack(enemy)
            
