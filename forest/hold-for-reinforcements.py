# ʳ��ħ����������
# Ϊ���������֯�����㹻��ʱ���ũ��
loop:
    flag = self.findFlag()
    enemy = self.findNearestEnemy()
    if flag:
        # ������
        self.moveXY(flag.pos.x, flag.pos.y)
    
    elif enemy:
        # ���򣬹�����
        # ʹ�������ƶ���ָ��λ�ã�����ո����ȴ����ʹ���ո�ܡ�
        if self.isReady("cleave"):
            self.cleave(enemy)
        else:
            self.attack(enemy)
        
