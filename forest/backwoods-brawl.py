# ����һ���ӡ�
# �����Ӯ�ˣ���ؿ������ø��ѣ��Լ����õĽ�������
# ��������ˣ������ȴ�24Сʱ������ٴ���ս��
# �ǵã�ÿһ���ύ�����ò�ͬ�ĵ�ͼ��
loop:
    flag = self.findFlag()
    enemy = self.findNearestEnemy()
    item = self.findNearestItem()

    if flag:
        self.moveXY(flag.pos.x, flag.pos.y)
        self.pickUpFlag(flag)
    if enemy:
        if self.isReady("bash"):
            self.bash(enemy)
        elif self.isReady("cleave"):
            self.cleave(enemy)
        else:
            self.attack(enemy)
