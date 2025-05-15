import pandas as pd  # Importa a biblioteca Pandas para manipulação de dados
import re  # Importa a biblioteca de expressões regulares para validação dos números de cartão

# Criando um DataFrame com as bandeiras e seus padrões de número inicial usando expressões regulares
dados_bandeiras = {
    "Bandeira": ["Visa", "MasterCard", "Elo", "American Express", "Discover", "Hipercard"],  # Lista das bandeiras de cartões
    "Regex": [  # Lista de padrões de números de cartões, baseados nos prefixos das bandeiras
        r"^4\d{15}$",  # Visa: começa com 4 e tem 16 dígitos
        r"^(5[1-5]|222[1-9]|22[3-9]\d|2[3-6]\d{2}|27[0-2]\d|2720)\d{12}$",  # MasterCard: começa com 51-55 ou 2221-2720 e tem 16 dígitos
        r"^(4011|4312|4389|4576|5041|5067|5090|6277|6362|6504|6505|6506|6507|6509|6516|6550)\d*$",  # Elo: começa com vários prefixos
        r"^(34|37)\d{13}$",  # American Express: começa com 34 ou 37 e tem 15 dígitos
        r"^(6011\d{12}|65\d{14}|64[4-9]\d{13})$",  # Discover: começa com 6011, 65 ou no intervalo 644-649 e tem 16 dígitos
        r"^6062\d*$"  # Hipercard: começa com 6062
    ]
}

# Criando um DataFrame com os dados das bandeiras
df_bandeiras = pd.DataFrame(dados_bandeiras)

def identificar_bandeira(numero_cartao):
    """Função que identifica a bandeira do cartão de crédito com base no número fornecido."""
    
    for _, row in df_bandeiras.iterrows():  # Percorre cada linha do DataFrame para verificar os padrões
        if re.match(row["Regex"], numero_cartao):  # Compara o número do cartão com a regex correspondente
            return f"A bandeira do cartão é: {row['Bandeira']}"  # Retorna a bandeira identificada
    
    return "Bandeira não identificada"  # Caso nenhuma bandeira seja encontrada, retorna essa mensagem

# Lista de números de cartão para teste
numeros_teste = [
    "4111111111111111",  # Visa
    "2221000000000009",  # MasterCard
    "374562349812345",  # American Express
    "6011123456789012",  # Discover
    "6062123456789012"  # Hipercard
]

# Testa a função identificando a bandeira dos cartões da lista de teste
for numero in numeros_teste:
    print(identificar_bandeira(numero))  # Exibe a bandeira correspondente ao número testado
