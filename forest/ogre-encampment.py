# ����е��ˣ��򹥻�֮
# ���û�е��ˣ��򹥻��Ʊ���

loop:
    # ʹ��if/else���
    enemy = self.findNearestEnemy()
    if enemy:
        self.attack(enemy)
    else:
        self.attack("Chest")
    
    
