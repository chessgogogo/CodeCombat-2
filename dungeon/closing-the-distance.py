self.moveRight()

# ͨ����һ���ؿ�����Ӧ������ʶ�����
enemy1 = self.findNearestEnemy()
# ���ڣ������Ǹ�������

self.attack(enemy1)
self.attack(enemy1)
self.moveRight(2)
self.moveUp()
enemy2 = self.findNearestEnemy()
self.attack(enemy2)
self.moveDown()
self.moveRight()