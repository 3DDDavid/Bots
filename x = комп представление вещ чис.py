ch = input('НФЗ, порядок ').replace(",", ".")
x = float(ch[0:-2])
poriadok = int(ch[-2:])
print(1, "{:05d}".format(int(bin(15+poriadok)[2:])), str(x)[3:12], '0' * (10-len(str(x)[3:])), sep='', end='') if x < 0 else print(0, "{:05d}".format(int(bin(15+poriadok)[2:])), str(x)[2:12], '0' * (10-len(str(x)[2:])), sep='', end='')
input()