# ������Ҫ���������λ�ò���
# ����û���ڽ��������ʱ���ռ���ң�

loop:
    flag = self.findFlag()
    if flag:
        # ���Ǹ����ͨ�����ӵ�λ�õõ� fx �� fy �أ�
        # �����¿���εõ���Ʒ�� x �� y��
        
        
        self.buildXY("fire-trap", flag.pos.x, flag.pos.y)
        self.pickUpFlag(flag)
    else:
        item = self.findNearestItem()
        if item:
            itemPos = item.pos
            itemX = itemPos.x
            itemY = itemPos.y
            self.moveXY(itemX, itemY)
