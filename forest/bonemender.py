# �������ѵ�ʿ����ͻΧ
loop:
    if self.canCast("regen"):
        bernardDistance = self.distanceTo("Bernard")
        if bernardDistance < 10:
            # Bernard��Ҫ���ƣ�
            self.cast("regen", "Bernard")
        
        # ʹ�á�if���͡�distanceTo�������� Chandra
        # �����С��10�׵ľ��롣
        chandraDistance =self.distanceTo("Chandra")
        if chandraDistance < 10:
            # Chandra��Ҫ���ƣ�
            self.cast("regen", "Chandra")
    else:
        # �����û��ִ�� regen��ʹ�� if �� distanceTo 
        # ��������ЩС��һ������ĵ��� self.attackRange.
        enemy = self.findNearestEnemy()
        if enemy:
            edistance = self.distanceTo(enemy)
            if edistance < 20:
                self.attack(enemy)
