# ʹ��ըҩ�ɵ�ʳ��ħ
# Ȼ������Ĺ��ɵ�����

loop:
    enemy = self.findNearestEnemy()
    if enemy:
        if self.isReady("throw"):
            distance = self.distanceTo(enemy)
            # ���ʳ��ħ�������15�׵�ʱ����ըҩը��
            # ʹ�� if ���ȽϾ����15
            if distance > 15:
                self.throw(enemy)
            # ʹ�� else ������������㲻�ܹ�ը��
            else self.attack(enemy)
        else:
            self.attack(enemy)
