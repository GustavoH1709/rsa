import os

#chave publica 4653899
#chave privada 2255579

def check_valid_path(path):
    return os.path.isfile(path)

private_key = 2255579
n = 2027 * 2957

file_path_public_key = str(input("Insira o caminho da pasta com a chave pública: "))

if(check_valid_path(file_path_public_key) is False):
    raise SystemError('Caminho para arquivo com a chave pública é inválido')

file_input_path = str(input("Insira o caminho do arquivo de entrada: "))

if(check_valid_path(file_input_path) is False):
    raise SystemError('Caminho para arquivo de entrada é inválido')

file_output_path = str(input("Insira o caminho do arquivo de saída: "))

message = '';

with open(file_input_path, 'r') as file:
    message = file.read().replace('\n', '')

public_key = '';

with open(file_path_public_key, 'r') as file:
    public_key = int(file.read().replace('\n', ''))

print(public_key)

message_encoded = [ord(c) for c in message]
ciphertext = [pow(c, public_key, n) for c in message_encoded]

f = open(file_output_path, 'w')
f.writelines(str(line) + '\n' for line in ciphertext)
f.close()


message_encoded = [pow(c, private_key, n) for c in ciphertext]

print("".join(chr(ch) for ch in message_encoded))

