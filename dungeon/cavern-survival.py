# ����ʱ��ȵ��˵�Ӣ�۳���

loop:
    # �ƶ��Լ���ս�ԡ��д���!
    enemies = self.findEnemies()
    enemy = self.findNearest(enemies)
    if enemy:
        if self.isReady("bash"):
            self.bash(enemy)
        else:
            self.attack(enemy)