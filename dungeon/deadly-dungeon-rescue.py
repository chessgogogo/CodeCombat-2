# ����ȳ��ܿ��̵�ũ����ӳ����Ρ�
# ����Բ��ڵ�ˮ�޺��档
# ɱ�˾�����õ���ϣ���Ľ����
# ������Ӷ������еı��أ���õ������Ľ�����

loop:
    flag =self.findFlag("green")
    enemies = self.findEnemies()
    enemy = self.findNearest(enemies)
    item = self.findNearest(self.findItems())
    
    if flag:
        self.moveXY(flag.pos.x, flag.pos.y)
        self.pickUpFlag(flag)
    if item:
        self.moveXY(item.pos.x, item.pos.y)
    if enemy :
        distance = self.distanceTo(enemy)
        if distance < 8:
            self.attack(enemy)
    


