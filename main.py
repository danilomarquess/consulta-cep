import requests
def main():
    print("Bem Vindo a Central de Buscas CEPs ")

    cep = input("Digite um CEP: ")

    if len(cep) != 8:
        print("Cep Inválido")
        exit()

    requisicao = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    nova_requisicao = requisicao.json()

    if 'erro' not in nova_requisicao:
        print("CEP Encontrado")
        print("======================================================")
        print('CEP: {}'.format(nova_requisicao['cep']))
        print('Logradouro: {}'.format(nova_requisicao['logradouro']))
        print('Complemento: {}'.format(nova_requisicao['complemento']))
        print('Bairro: {}'.format(nova_requisicao['bairro']))
        print('Cidade: {}'.format(nova_requisicao['localidade']))
        print('Estado: {}'.format(nova_requisicao['uf']))
        print("======================================================")
    else:
        print('{}: CEP Inválido'.format(cep))

    opcao = int(input("Deseja realizar uma nova consulta?\n1 - Sim\n2 - Não\nSua opção: "))
    if opcao == 1:
        main()
    else:
        print("Saindo...")

if __name__ == '__main__':
    main()