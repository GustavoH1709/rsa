import os
import base64

#chave publica 4653899
#chave privada 2255579
#numeros primos 2027 e 2957
#expoente 5993839

def check_valid_path(path):
    return os.path.isfile(path)

def string_to_base64(string):
    string_bytes = string.encode('ascii')
    base64_bytes = base64.b64encode(string_bytes)
    base64_string = base64_bytes.decode('ascii')
    return base64_string

n = 2027 * 2957

file_path_public_key = str(input("Insira o caminho da pasta com a chave pública e privada: "))

if(check_valid_path(file_path_public_key) is False):
    raise SystemError('Caminho para arquivo com a chave pública é inválido')

file_input_path = str(input("Insira o caminho do arquivo do texto que vai ser criptografado: "))

if(check_valid_path(file_input_path) is False):
    raise SystemError('Caminho para arquivo de entrada é inválido')

file_output_path = str(input("Insira o caminho do arquivo de saída: "))

message = '';

with open(file_input_path, 'r') as file:
    message = file.read().replace('\n', '')

message_to_64 = string_to_base64(message);

with open(file_path_public_key, 'r') as file:
    input_encryption_lines = file.readlines()

public_key = int(input_encryption_lines[0]);
private_key = int(input_encryption_lines[1]);

message_encoded = [ord(c) for c in message_to_64]
ciphertext = [pow(c, public_key, n) for c in message_encoded]

f = open(file_output_path, 'w')
f.writelines(str(line) + '\n' for line in ciphertext)
f.close()

message_encoded = [pow(c, private_key, n) for c in ciphertext]

