self.moveDown()

# �����ܶ���˵�����Ե����ڵ������ҵ���Ģ����

self.moveRight()
self.moveDown()
self.moveUp()
self.moveLeft()
self.moveDown(2)
self.moveRight(4)
self.moveUp()
self.moveLeft()
self.moveUp()
self.moveRight()
self.moveUp()
self.moveLeft()
self.moveDown()

# �ҵ���ȥ���������ߵ�·��

loop:
    enemy = self.findNearest(self.findEnemies())
    if enemy:
        self.attack(enemy)