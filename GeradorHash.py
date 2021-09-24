import hashlib

string= input('Digite o texto a ser convertido em Hash:')
resultado = hashlib.md5(string.encode('utf-8'))

print('O hash da string é: ', resultado.hexdigest())
