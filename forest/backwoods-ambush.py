# �ƶ��������ڵ㣬������ÿһ��ʳ��ħ��
self.moveXY(24, 42)
enemy1 = self.findNearestEnemy()
# �ڹ���֮ǰ��ʹ��if�����ȷ����ǰ�е��˴��ڡ�
if enemy1:
	self.attack(enemy1)
	self.attack(enemy1)

self.moveXY(27, 60)
enemy2 = self.findNearestEnemy()
if enemy2:
	self.attack(enemy2)
	self.attack(enemy2)

self.moveXY(42, 50)
# ��ʹ��һ��if��䲢������
enemy3 = self.findNearestEnemy()
if enemy3:
	self.attack(enemy3)
	self.attack(enemy3)

# �ƶ�����һ���ڵ㲢����ʣ���ʳ��ħ��
self.moveXY(39, 24)
enemy4 = self.findNearestEnemy()
if enemy4:
	self.attack(enemy4)
	self.attack(enemy4)
self.moveXY(55, 29)
enemy5 = self.findNearestEnemy()
if enemy5:
	self.attack(enemy5)
	self.attack(enemy5)
