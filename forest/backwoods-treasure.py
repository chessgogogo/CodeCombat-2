# ��2~3�������� �ռ�100�����
# �����Ӯ�ˣ����ø��ѣ������и��ཱ����
# ��������ˣ���Ҫ�ȴ�һ���ٴ���ս
# ��ס��ÿ���ύ����õ��µ�������ӡ�
loop:
    item = self.findNearestItem()
    enemy = self.findNearestEnemy()
    flag = self.findFlag("green")
    if flag:
        self.pickUpFlag(flag)
    if item:
        self.moveXY(item.pos.x, item.pos.y)
    if enemy:
        if self.isReady("bash"):
            self.bash(enemy)
        elif self.isReady("cleave"):
            self.cleave(enemy)
        else:
            self.attack(enemy)
