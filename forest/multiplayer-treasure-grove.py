# ����һ���ռ�100����ҵ��ˣ�
# ��������ˣ�������ʱ��ֻ��ԭ����ҵ�67%

loop:
    # �ҵ���Ҳ���������
    # ʹ�����Ӻ�������ƶ�������Ӯ�ñ�����
    
    flag = self.findFlag()
    enemy = self.findNearestEnemy()
    item = self.findNearestItem()
    if flag:
        self.moveXY(flag.pos.x, flag.pos.y)
        self.pickUpFlag(flag)
    if enemy:
        distance1 = self.distanceTo(enemy)
        if distance1 < 1:
            self.attack(enemy)
    if item:
        distance2 = self.distanceTo(item)
        if distance2 < 5:
            self.moveXY(item.pos.x, item.pos.y)
    
