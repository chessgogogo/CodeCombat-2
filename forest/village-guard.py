# �ڴ��Ѳ�ߡ�
# ������ֵ��ˣ���ɱ���ǡ�

loop:
    self.moveXY(35, 34)
    leftEnemy = self.findNearestEnemy()
    if leftEnemy:
        self.attack(leftEnemy)
        self.attack(leftEnemy)
    # �����ƶ����Ҳࡣ
    # ʹ��ifָ���ж��Ƿ��е��ˣ��еĻ�����ɱ���ǡ�
    self.moveXY(60, 31)
    rightEnemy = self.findNearestEnemy()
    if rightEnemy:
        self.attack(rightEnemy)
        self.attack(rightEnemy)
