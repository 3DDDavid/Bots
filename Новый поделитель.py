l, a = map(int,input("����� �� � ��: ").split())
answer = l
do = 0
if answer == 0 or l <= a:
    print("�� ��, ����??")
while answer > a:
    do += 1
    if (answer % 2 == 0):
        answer //= 2
        print("/2")
    else:
        answer += 1
        print("+1")
    if answer < a:
        print("ERROR")
        print("����� ���!")
        
#    if answer <= a:
 #       print("��������:", do)
print("��������:", do)