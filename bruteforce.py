import itertools
import string
import time

# Solicita ao usuário criar uma senha alfanumérica de 4 dígitos
senha_usuario = input("Digite uma senha alfanumérica de 4 dígitos: ")

# Verifica se a senha tem 4 dígitos
if len(senha_usuario) != 4:
    print("Senha inválida. Deve ter 4 dígitos.")
    exit()

# Define o conjunto de caracteres alfanuméricos
caracteres = string.ascii_letters + string.digits

# Inicia o contador de tentativas
tentativas = 0

# Inicia o tempo de início do ataque
inicio = time.time()

# Inicia o ataque de força bruta
for senha_tentativa in itertools.product(caracteres, repeat=4):
    tentativas += 1
    senha_tentativa = ''.join(senha_tentativa)
    print('.', end='', flush=True)  # Imprime um ponto a cada tentativa
    if senha_tentativa == senha_usuario:
        print(f"\nSenha encontrada! {senha_usuario}")
        print(f"Tentativas: {tentativas}")
        print(f"Tempo: {time.time() - inicio:.2f} segundos")
        break
else:
    print("\nSenha não encontrada.")