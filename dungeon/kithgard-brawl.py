# ��һ������ʳ��ħ�����л�������
# �����Ӯ�ˣ����ػ��ø��ѣ���������Ľ�����
# ��������ˣ�������һ��֮����������ύ��
# ÿ���ύ�������µ�������ӡ�

loop:
    enemy = self.findNearest(self.findEnemies())
    flag = self.findFlag("green")
    item = self.findNearest(self.findItems())
    if flag:
        self.moveXY(flag.pos.x, flag.pos.y)
        self.pickUpFlag(flag)
    if item:
        self.moveXY(item.pos.x, item.pos.y)
    if enemy:
        if self.isReady("bash"):
            self.bash(enemy)
        if self.isReady("cleave"):
            self.cleave(enemy)
        else:
            self.attack(enemy)