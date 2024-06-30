
#DESAFIO
#para cada produto incluir o saldo do produto
#para cada produto incluir o saldo inadimplente
#se maior, pedir pra digitar novamente
lista_de_produtos = ['CDC',
                         'Cartão de crédito',
                         'Financiamento Imobiliário',
                         'Financiamento de Veículo',
                         'Custeio',
                         'Giro']

def escolher_produto():
    #funcao para o usuario escolher o produto a ser cadastrado de uma lista
    lista_de_produtos = [0,'CDC',
                         'Cartão de crédito',
                         'Financiamento Imobiliário',
                         'Financiamento de Veículo',
                         'Custeio',
                         'Giro']
    print('--------------------------------------------------------------')
    print ('(1) CDC (2) Cartão de crédito (3) Financiamento Imobiliário')
    print ('(4) Financiamento de veículo  (5) Custeio (6) Giro')
    print('--------------------------------------------------------------')
    produto_escolhido = int(input('Escolha qual produto será cadastrado: '))
    while produto_escolhido <=0 or produto_escolhido > 6:
      produto_escolhido = int(input('Escolha qual produto será cadastrado: '))
    print(f'O produto escolhido foi: {lista_de_produtos[(produto_escolhido)]}')
    print('--------------------------------------------------------------')
    return (lista_de_produtos[(produto_escolhido)])


def cadastra_produto():
  #função para coletar input do cliente, retorna dois valores
  saldo_produto = int(input('Insira o saldo do produto: '))
  saldo_produto_inadimplente = int(input('Insira o saldo inadimplente: '))
  #verificar se o saldo inadimplente é menor ou maior que o saldo do produto
  while saldo_produto_inadimplente > saldo_produto:
    saldo_produto_inadimplente = int(input(f'Saldo inadimplente não pode ser maior que o saldo do produto( R$ {saldo_produto}): '))
  print('--------------------------------------------------------------')
  return saldo_produto, saldo_produto_inadimplente

def deseja_repetir():
  lista_sim = ['S', 's', 'Sim', 'sim']
  lista_nao = ['N', 'n', 'Não', 'não', 'nao', 'Nao']
  
  repetir = input('Deseja cadastrar outro produto? (S/N): ')
  if repetir in lista_sim:
    return True
  elif repetir in lista_nao:
    return False
  else:
    return True

print('**************************************************************')
print('**********Bem vindo ao controlador de inadimplência!**********')
print('**************************************************************')
#Solicitar ao usuário informar quantos cliente serão cadastrados
quantidade_de_clientes = int(input("Insira o número de clientes a serem cadastrados: "))

for i in range(quantidade_de_clientes):

  #Solicitar usuário incluir nome do cliente
  nome_do_cliente = input("Insira o nome do cliente: ")
  nome_do_cliente = nome_do_cliente.upper()
  #Solicitar usuário incluir quantos produtos possui(até 3)
  
  #Variáveis são zeradas no início de cada iteração do loop

  saldo_total = 0
  saldo_total_inadimplente = 0
  maior_valor_de_saldo = 0
  maior_valor_inadimplente = 0
  produto_com_maior_valor_de_saldo = ' '
  produto_com_maior_valor_inadimplente = ' '
  dicionario_produto={}
  dicionario_produto_inadimplente={}
  quantidade_de_produtos = 0
  
  for i in lista_de_produtos:
    dicionario_produto[i] = 0
    dicionario_produto_inadimplente[i] = 0

  #pode ser feito de outra forma?? versão onde o cliente vai cadastrado até o teto maximo (3)
  cadastrando_produto = True
  while cadastrando_produto:
    #escolhe produto de uma lista
    produto = escolher_produto()
    saldo_produto, saldo_produto_inadimplente = cadastra_produto()
    #oque fazer se o cliente possuir dois produtos iguais? Obviamente somar os saldos
    dicionario_produto[produto] += saldo_produto
    if dicionario_produto[produto] > maior_valor_de_saldo:
        maior_valor_de_saldo = dicionario_produto[produto]
        produto_com_maior_valor_de_saldo = produto #ainda não sei oque fazer quando dois produtos com saldos são iguais
    dicionario_produto_inadimplente[produto] += saldo_produto_inadimplente
    if dicionario_produto_inadimplente[produto] > maior_valor_inadimplente:
        maior_valor_inadimplente = dicionario_produto_inadimplente[produto]
        produto_com_maior_valor_inadimplente = produto
    quantidade_de_produtos +=1
    print('A quantidade atual de produtos é: ',quantidade_de_produtos, '... max 3.')

    #falta arrumar essa parte
    if quantidade_de_produtos < 3:
      cadastrando_produto = deseja_repetir()
    else:
      cadastrando_produto = False
  
  saldo_total = sum(dicionario_produto.values())
  saldo_total_inadimplente = sum(dicionario_produto_inadimplente.values())
  #teste abaixo
  print('teste', dicionario_produto, dicionario_produto_inadimplente)
  ##após capturar os dados apresentar para cada cliente cadastrado a mensagem
  palavra_produto = 'produto' if quantidade_de_produtos == 1 else 'produtos'
  palavra_totaliza = 'totaliza' if quantidade_de_produtos == 1 else 'totalizam'
  print(f'{nome_do_cliente} possui {quantidade_de_produtos} {palavra_produto}, que {palavra_totaliza} R$ {saldo_total} de saldo e \n {saldo_total_inadimplente} de saldo inadimplente.')
  print(f'O produto de maior valor de saldo é o "{produto_com_maior_valor_de_saldo}" e o com maior valor inadimplente é o "{produto_com_maior_valor_inadimplente}"')
  print('--------------------------------------------------------------')
  print('--------------------------------------------------------------')
  #apenas após a mensagem acima cadastrar os dados do próximo cliente, se houver
print('FIM')

