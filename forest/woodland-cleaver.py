# �����ܾ���ʹ������¼��ܡ�cleave��

self.moveXY(23, 23)
loop:
    enemy = self.findNearestEnemy()
    if self.isReady("cleave"):
        # ��Cleave�������ˣ�
        self.cleave(enemy)
    else:
        # ���������cleave����û׼���ã������������ͨ����
        self.attack(enemy)