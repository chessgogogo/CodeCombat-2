# ֻ������Сʳ��ħ��Ͷ����ʳ��ħ��
# �𹥻���������ʳ��ħ���ܡ�

loop:
    enemy = self.findNearestEnemy()
    
    # ��ס���𹥻�����burl��
    if enemy.type is "burl":
        self.say("�Ҳ���������burl��")

    # type ���Ը���������ʲô���������
    if enemy.type is "munchkin":
        self.attack(enemy)
    
    # ʹ�á�if��������Ͷ���ߡ�thrower��
    if enemy.type is "thrower":
        self.attack(enemy)
    
    # �������һ��ʳ��ħ��ogre�����ܵ����ȥ��
    if enemy.type is "ogre":
        self.moveXY(40, 47)
    
