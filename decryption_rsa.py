import os
import base64

#chave publica 4653899
#chave privada 2255579
#expoente 5993839

#n = 2027 * 2957

def check_valid_path(path):
    return os.path.isfile(path)

def base64_to_string(base64_string):
    base64_bytes = base64_string.encode('ascii')
    string_bytes = base64.b64decode(base64_bytes)
    original_string = string_bytes.decode('ascii')
    return original_string

private_key_and_power_file_path = str(input("Insira o caminho do arquivo com a chave privada e o expoente: "))

if(check_valid_path(private_key_and_power_file_path) is False):
    raise SystemError('Caminho para arquivo com as chave privada é inválido')

encoded_message_file_path = str(input('Insira o caminho do arquivo de com a mensagem criptografada: '))

if(check_valid_path(encoded_message_file_path) is False):
    raise SystemError('Caminho para arquivo com a mensagem criptografada é inválido')

decoded_output_file_path = str(input("Insira o caminho do arquivo de saída"))

private_key = 0;
power = 0;

with open(private_key_and_power_file_path, 'r') as file:
    keys_lines = file.readlines()
    private_key = int(keys_lines[0]);
    power = int(keys_lines[1]);

output_file_lines = []

with open(encoded_message_file_path, 'r') as file:
    for item in file:
        if(item != '\n' and item != ''):
            output_file_lines.append(int(item.replace('\n', '').replace(' ', '')))
    file.close()

message_encoded = [pow(c, private_key, power) for c in output_file_lines]
message_translate = "".join(chr(ch) for ch in message_encoded)
message_64_to_string = base64_to_string(message_translate)

with open(decoded_output_file_path, 'w') as file:
    file.write(message_64_to_string)
    file.close();