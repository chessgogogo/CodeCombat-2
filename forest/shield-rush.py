# ��shield���ƺ�cleave˳��ն�����������л�����
# ���cleave˳��նû��׼���ã��������shield���Ƽ��ܡ�
# �㽫����Ҫ����142����ֵ����֤������

loop:
    enemy = self.findNearestEnemy()
    if self.isReady("cleave"):
        self.cleave(enemy)
    elif self.isReady("shield"):
        self.shield()
    else:
        self.attack(enemy)
