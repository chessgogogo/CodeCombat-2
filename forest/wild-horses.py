loop:
    # ����ôѰ��������Ѻõ�λ��
    # ��=��
    friends = self.findFriends()
    horse = self.findNearest(friends)
    if horse:
        x1 = horse.pos.x - 7
        x2 = horse.pos.x + 7
        
        if x1 >= 1:
            self.moveXY(x1, horse.pos.y)
            
        elif x2 <= 79:
            self.moveXY(x2, horse.pos.y)
            
        distance = self.distanceTo(horse)
        if distance <= 10:
            self.say("Whoa")
            # �Ƶ�����ɫ��x��ʹ����ũ����
            self.moveXY(28, 54)
            # �ƻ�������ʼѰ����һƥ��
            
            
