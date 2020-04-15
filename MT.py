print('Bem vindo à Máquina de Turing.')
cadeia = input('Digite a cadeia de símbolos desejada: ')
print('A cadeia digitada foi ', cadeia)
num_cadeia = len(cadeia) #conta a quantidade de caracteres que foi digitado
print(num_cadeia)
estado = 'q2'
#simbolo = 0
movimento = 'S'
#num_linha = 0

cad=0 #contador para percorrer a cadeia de símbolos digitada
lin=2 #contador para percorrer as linhas do arquivo de texto
alf=0 #contador para percorrer o alfabeto do arquivo de texto
est=1 #contador para percorrer os estado do arquivo de texto

dados = open("configuracoes.txt", "r") #abre o arquivo de texto em modo leitura
linhas = dados.readlines()
linha0 = linhas[0]
num_estados = len(linha0)//3
linha1 = linhas[1]
num_alfabeto = len(linha1)//2
print('qnt estados; ', num_estados, ' | qnt alfabeto: ', num_alfabeto)

while cad < num_cadeia: #percorre todos os símbolos da cadeia digitada
    simbolo = cadeia[cad] #recebe o o símbolo da cadeia referente a posição que será analizada
    ########################### DEFINE O NOVO ESTADO
    num_estado = linha0[est]
    while estado[1]!=num_estado:
        print('q', estado[1], ' | estado atual: q', num_estado)
        est = est+3
        lin = lin+num_alfabeto
        num_estado = linha0[est]
    num_alfabetos = linha1[alf]
    while simbolo!=num_alfabetos:
        alf = alf+2
        num_alfabetos = linha1[alf]
    #print('estado atual q', num_estado, 'linha ', lin)
    linha = linhas[lin]
    print(linha, end="")
    #print(sim_cadeia)
