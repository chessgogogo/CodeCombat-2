self.moveXY(55, 14)
self.moveXY(92, 9)

# �ں�ɫ�� X λ�ý���һ����������
# ���˵�ľ�� X λ�ã��������˺���
# �ȹ�Ӷ�����������Ļ�������
# ����Ӫ�أ����û��������ں�ɫ�� X λ��
# ����Ĳ��Ӻ����ˣ���ʾ��ʹ�� say ����, "Retreat!"��
# �ӻص���ߵ�ľ�� X λ��

self.buildXY("fire-trap", 94, 20)
self.moveXY(79, 6)
self.moveXY(92, 9)
self.moveXY(60, 63)
self.buildXY("fire-trap", 60, 63)
self.moveXY(90, 53)
self.buildXY("fire-trap", 90, 53)
self.moveXY(94, 20)
self.moveXY(5, 14)
self.say("Retreat")
self.moveXY(-16, 39)
