# �ռ�ÿƬ�ݵص����н�ҡ�
# ʹ�������ڲݵؼ��ƶ���
# ����׼���÷�������ʱ������ύ��

loop:
    flag = self.findFlag()
    if flag:
        pass  # ��pass����һ��ռλ������û���κ�����
        # Pick up the flag.
        self.pickUpFlag(flag)
    else:
        # Automatically move to the nearest item you see.
        item = self.findNearestItem()
        if item:
            position = item.pos
            x = position.x
            y = position.y
            self.moveXY(x, y)
