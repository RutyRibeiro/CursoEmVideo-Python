print('          \033[4;34mPyHELP\033[m ')

esc=input('Digite uma funcionalidade: ' ).lower()
while True:
    if esc=='fim':
        break
    else:
        help(esc)
        esc=input('Digite uma funcionalidade: ' ).lower()
