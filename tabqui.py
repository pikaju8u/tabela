# Dicionário contendo informações dos elementos químicos
elementos = {
    'H': {'numero_atomico': 1, 'nome': 'Hidrogênio', 'massa': 1.008},
    'He': {'numero_atomico': 2, 'nome': 'Hélio', 'massa': 4.0026},
    'Li': {'numero_atomico': 3, 'nome': 'Lítio', 'massa': 6.94},
    'Be': {'numero_atomico': 4, 'nome': 'Berílio', 'massa': 9.0122},
    'B': {'numero_atomico': 5, 'nome': 'Boro', 'massa': 10.81},
    # Adicione outros elementos aqui
}

# Função para buscar informações do elemento
def buscar_elemento(sigla):
    if sigla in elementos:
        elemento = elementos[sigla]
        return elemento['numero_atomico'], elemento['nome'], elemento['massa']
    else:
        return None, None, None

# Função principal
def main():
    sigla = input("Insira a sigla do elemento químico: ").capitalize()  # Garante que a sigla seja capitalizada
    numero_atomico, nome, massa = buscar_elemento(sigla)
    if numero_atomico is not None:
        print(f"Número Atômico: {numero_atomico}")
        print(f"Nome: {nome}")
        print(f"Massa: {massa} u")
    else:
        print("Elemento não encontrado.")

# Chamada da função principal
if __name__ == "__main__":
    main() 