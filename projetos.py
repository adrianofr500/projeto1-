def programa():
    opcao = menu()
    if opcao.lower() == 'a':
        print('cadastrada produto\n')
    else:
        print('opção invalida\n')    
    
     
   
  

def menu():
    print('=-='*14)
    print('     SISTEMA DE GESTÃO DE PRODUTOS')
    print('=-='*14)
    print('\n')
    print('     <!> Seja bem vindo(a)!\n')
    print('     >>> Operações desponíveis:\n')
    print('     <A> Cadastrar produto')
    print('     <B> Consulta simples')
    print('     <C> Consulta geral')
    print('     <D> Deletar produto')
    print('     <E> informações do produto')
    print('     <F> Informação do sistema')
    print('     <G> Sair do sitema\n')
    print('     <?> o que você deseja fazer?')
    entrada = input(' digite a opção')
    return entrada

while True:
    programa()    
    
