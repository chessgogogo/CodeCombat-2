# �ռ����ʹ����������������
# �����⴦����Щʳ��ħ

loop:
    flag = self.findFlag()
    
    if flag:
        self.buildXY("fire-trap", flag.pos.x, flag.pos.y)
        self.pickUpFlag(flag)
    else:
        item = self.findNearestItem()
        if item:
            
            self.moveXY(item.pos.x, item.pos.y)
        
