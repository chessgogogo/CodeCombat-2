# ʹ�� if �� else if �������κ����
# ���������������ˣ��ռ����
# ȷ�������Ʒ�̵���ΰ��Ŀ��ף�����400�����ϵĽ�����

loop:
    flag = self.findFlag()
    enemy = self.findNearestEnemy()
    item = self.findNearestItem()

    if flag:
        # ���ҷ������ӵ�ʱ������ʲô��
        self.moveXY(flag.pos.x, flag.pos.y)
        self.pickUpFlag(flag)
    elif enemy:
        # �����ҵ����˵�ʱ������ʲô��
        self.attack(enemy)
    elif item:
        # �����ҵ�һ����Ʒ��ʱ�򣬷�����ʲô��
        self.moveXY(item.pos.x, item.pos.y)
        
