# �ڶ̾������ͷ���ġ���ȡ���������ܡ�
# ʹ����ķ�����Զ���빥����

loop:
    enemy = self.findNearestEnemy()
    if enemy:
        distance = self.distanceTo(enemy)
        if distance < 15:
            # �ڵ������ͷš���ȡ���������ܡ�
            self.cast("drain-life", enemy)
        else:
            # ʹ��������ѹ������ˡ�
            self.attack(enemy)
            
