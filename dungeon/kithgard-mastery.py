# ʹ���ƶ�������Թ����յ㡣
# �������ռ����ı�ʯ������Ȼ���ڵ����������ʱͨ��˵����ǰ�ı�ʯ������ʹ����ʧЧ��
# �����ĵط�����һֻ��ѻ������һ�����롣���ŵĸ���˵�������������š�
# ���㿿��ʳ��ħʱɱ������
# ���������Ҫ��ʱ��ʹ��loop���ظ����е�ָ�
# �����ͨ��������ؿ�����Ϳ���ֱ��������Զ������ɭ�֣�
x = 0
loop:
    self.moveUp()
    self.moveRight(3)
    self.moveUp()
    x += 1
    self.moveDown()
    self.moveRight()
    self.say("Friend")
    self.moveRight(2)
    self.moveUp()
    self.say(x)
    self.moveUp(2)
    enemy = self.findNearestEnemy()
    self.attack(enemy)
    self.attack(enemy)
    self.moveLeft(4)
    self.moveUp(2)