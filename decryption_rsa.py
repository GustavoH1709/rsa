import os

#chave publica 4653899
#chave privada 2255579

private_key = 2255579
n = 2027 * 2957

def check_valid_path(path):
    return os.path.isfile(path)

output_file_path = str(input('Insira o caminho do arquivo de saída: '))

if(check_valid_path(output_file_path) is False):
    raise SystemError('Caminho para arquivo de saida é inválido')

output_file_lines = []

with open(output_file_path, 'r') as file:
    for item in file:
        if(item != '\n' and item != ''):
            output_file_lines.append(int(item.replace('\n', '')))

message_encoded = [pow(c, private_key, n) for c in output_file_lines]
message_translate = "".join(chr(ch) for ch in message_encoded)

print(message_translate)