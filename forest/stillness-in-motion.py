# ����Խ�һ��if���ŵ���һ��if��䵱�С�
# ���ǣ����������úܸ��ӣ���������ע����Щif�������λ���Ӱ��ġ�
# ��ȷ������������ȷ��
# ��ע����������Ĵ����߼�
# ��һ��if/else����У����������if/else����ע�ͽ�����а�����������ʾ��

loop:
    enemy = self.findNearestEnemy()
    
    # �������һ�����ˣ���...
    if enemy:
        # ����һ����ΪdistanceTo�ı������������
        distance =self.distanceTo(enemy)
        # �����������С��5�׵ľ��룬��ôattack()
        if distance < 5:
            self.attack(enemy)
        # �����������˻����Զ������shield()
        else:
            self.shield()
            
        pass

    # ����û�е���...��
    else:
        # ...�ص�λ��X
        self.moveXY(40, 34)
