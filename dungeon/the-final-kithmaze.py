# ʹ��loopѭ���ƶ�������Ŀ��

loop:
    self.moveRight()
    self.moveUp()
    enemy = self.findNearestEnemy()
    self.attack(enemy)
    self.attack(enemy)
    self.moveRight()
    self.moveDown(2)
    self.moveUp()