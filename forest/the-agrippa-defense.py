loop:
    enemy = self.findNearestEnemy()
    if enemy:
        pass  # �����Լ��Ĵ����滻����
        # �� distanceTo ��ȡ����˵ľ��롣
        distance = self.distanceTo(enemy)
        # �������С��5��...
        if distance < 5:
            # ...��� ��cleave������׼�����ˣ��͡�cleave�������ǣ�
            if self.isReady("cleave"):
                self.cleave(enemy)
            # ...���򣬽���������ͨ������
            else:
                self.attack(enemy)
