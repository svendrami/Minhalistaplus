import time
class MinhaLista:

    def __init__(self):
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)

    def apresentar(self):
        for i in self.itens:
          print(i, end="\n")
    
umaLista = MinhaLista()

while True:
    # exibir o menu de opções
    print("--- menu ---")
    print("1 - listar itens")
    print("2 - cadastrar itens")
    print("3 - limpar a lista")
    print("4 - sair")
    print("opção: ")
    # solicitar o que o usuário quer fazer
    op = input()

    if op == '1': # usuário deseja listar pessoas?
        print("Listagem de itens")
        umaLista.apresentar()
        time.sleep(5)
        #for p in pessoas: # percorre a lista de pessoas
            # exibe os dados da pessoa
         #   print("=>", p.nome, p.email, p.telefone)

    elif op == '2': # usuário quer cadastrar algum item?
        print("Cadastro de itens") 
        # solicita o item
        item = input("Informe o nome do item: ")
        # cria o item
        #umaLista = MinhaLista()
        umaLista.adicionar(item) #nova = Pessoa(nome, email, telefone)
        # adiciona na lista
        #pessoas.append(nova)
        #print("A pessoa foi cadastrada.")
    elif op =='3':
      umaLista = MinhaLista()
      print("A lista está vazia agora!")
      time.sleep(10)
    elif op == '4': # encerrar o sistema?
        break # sai do while
    else: # usuário escolheu outra coisa?
        print("Opção inválida") # usuário cabeção



#umaLista = MinhaLista()

#umaLista.adicionar("a")
#umaLista.adicionar(10)
#umaLista.adicionar("teste")
#umaLista.adicionar(2010)

#umaLista.apresentar()