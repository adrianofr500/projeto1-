def menu():
    print('SISTEMA DE GESTÃO DE PRODUTOS\n')
    print('O que você quer fazer?')
    print('A - Cadastrar produto')
    print('B - Consultar produto\n')
    opcao = input('Digite a opção a ser executada: ')

    if opcao.lower() == 'a':
        cadastrar_produto()
        input('Digite qualquer tecla para continuar... ')
    elif opcao == 'b':
        print('Função a ser implementada...')
    else:
        print('Opção inválida!')
        input('Digite qualquer tecla para continuar... ')

def cadastrar_produto():
  banco = retornar_banco('ler')
  produtos = banco.readlines()
  banco.close()
  codigo = len(produtos)+1

  print('CADASTRO DE PRODUTO\n')
  nome = input('Digite o nome do produto: ')
  qtde = input('Digite a quantidade do produto em estoque: ')
  preco = input('Digite o preço do produto')

  banco = retornar_banco('adicionar')
  banco.write('%i,%s,%s,%s\n' %(codigo, nome, qtde, preco))
  banco.close()

  print('Produto cadastrado com sucesso!')

  if input('Deseja cadastrar um novo produto? S/N: ').lower() == 's':
    cadastrar_produto()

def retornar_banco(operacao):
  if operacao == 'adicionar':
    return open('banco.txt', 'a')
  elif operacao == 'ler':
    try:
      return open('banco.txt', 'r')
    except:
      banco = open('banco.txt', 'w')
      banco.close()
      return open('banco.txt', 'r')

    
while True:
  menu()