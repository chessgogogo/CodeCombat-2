# ͵͵����ɭ�֣�����������
# ����ָ�ӹ�Craig С�Ľӽ��еĵ��ˡ�
# �������Ӻ󣬰��ύ��

loop:
    flag = self.findFlag()
    enemy = self.findNearestEnemy()
    if flag:
        self.moveXY(flag.pos.x, flag.pos.y)
        self.pickUpFlag(flag)
        
    elif enemy:
        # ������Ұ�ڵĵ��ˡ�
        if enemy:
            self.attack(enemy)
        
