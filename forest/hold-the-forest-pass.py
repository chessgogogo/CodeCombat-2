# ʹ�����Ӽ���ս�����߳��ˡ�
# If you fail, press Submit again for new random enemies and try again!
# You'll want at least 300 health, if not more.

loop:
    enemy = self.findNearestEnemy()
    flag = self.findFlag()
    if flag:
        # �������ӡ�
        pass
        self.pickUpFlag(flag)
    elif enemy:
        # ��
        pass
        self.attack(enemy)
