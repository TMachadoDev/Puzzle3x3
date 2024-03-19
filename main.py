#Importar bibliotecas
import random 
import pyconio
import time

#Função que vai permitir baralhar os nossos numeros em uma matrix
def CriarMatriz():
    num = 0 #o numero que vamos sortear
    lista = [] #lista unidimensional com todos os números aleatorios
    for i in range(9): #fazer 9 vezes
        num = random.randint(0,8) #atribuir um número aleatorio entre 0 e 8
        while num in lista: #se esse número estiver na nossa lista
            num = random.randint(0,8) #atribuir um novo número entre 0 e 8
        lista += [num] #adicionar o novo número a lista unidimensional, desta forma terei sempre os 9 numeros contando com o 0
    return [lista[k:k+3] for k in range(0, 9, 3)] #tornar a lista unidimensional em uma matriz de 3x3

started = 0 #váriavel que vai conter a "Hora" (timestamp) que iniciei o jogo
finished = 0 #váriavel que vai conter a "Hora" (timestamp) que finalizei o jogo
contagem = 0 #váriavel contagem de movimentos feitos
Joguinho = CriarMatriz() #Chamar a função para criar a matriz de 3x3
posiDoZero = [] #váriavel que vai conter uma lista com linha e coluna onde se encontra o espaço vazio na matriz

#Este procedimento verifica a diferença entre um jogo completo e o que eu tenho e transforma-o em percentagem
def CalcularPercentagem(matriz):
    percent = 0 #váriavel o numero de igualdades
    alvo = [[1,2,3], [4,5,6], [7,8,0]] #o nosso alvo/modelo que queremos atingir (jogo completo)
    for linha in range(3): #para cada linha
        for coluna in range(3): #para cada coluna
            if alvo[linha][coluna] == matriz[linha][coluna]: #se em ambas as posições da lista do jogo e da lista do alvo o elemento for o mesmo 
                percent += 1 #incrementar a nossa contagem 
    MostrarResultados((percent/9)*100) #Chamar a função de mostrar resultados, com um quociente entre as igualdades e todos os números multiplicado por 100 para nos dar uma percentagem

#Este procedimento permite imprimir várias caracteristicas do nosso jogo, como tempo decorrido progresso, movimentos
def MostrarResultados(percentagem):
    #defenimos as váriaveis globais que precisamos usar
    global finished
    global started
    global contagem

    finished = int(time.time()) #finalizamos o tempo para poder calcular
    tempo = finished - started #tempo decorrido em segundos
    pyconio.gotoxy(20,5) #Ir para determinada posição
    print("Movimentos: ", contagem) #Imprimir o número de movimentos
    pyconio.gotoxy(20,7) #Ir para determinada posição
    print("Tempo Decorrido", tempo, "segundos") #Imprimir o tempo decorrido em segundos
    pyconio.gotoxy(20,9) #Ir para determinada posição
    print("Progresso:", int(percentagem), "%") #Imprimir o progresso em valor inteiro
    pyconio.gotoxy(20,11) #Ir para determinada posição
    if percentagem == 100: #se a percentagem for de 100% significa que o jogo está concluido
        pyconio.textcolor(pyconio.Green) #Texto para cor Verde
        print("Parabéns! Concluis-te com sucesso") #Imprimir mensagem de sucesso
        pyconio.gotoxy(pyconio.gettermsz()[0],pyconio.gettermsz()[1]) #Ir para o fim do terminal
        exit() #Sair
    if percentagem == -1: #O progresso pode ser 0 então para poder controlar eu coloquei -1
        pyconio.textcolor(pyconio.Red) #Texto para cor Vermelha
        print("Sempre podes tentar novamente!") #Imprimir mensagem de sem exîto
        pyconio.gotoxy(pyconio.gettermsz()[0],pyconio.gettermsz()[1]) #Ir para o fim do terminal
        exit() #Sair
    
#Apesar do nome não ser muito sugestivo, este procedimento permite receber a seta que clicamos e faz todas as verificações, e posteriormente efetua as alterações necessárias na nossa matriz, por fim chama uma função para poder atualizar na tela as mudanças efetuadas.    
def FazerAcontecer(arrow):
    #Defenir váriaveis globais
    global posiDoZero 
    global Joguinho

    #Caso a posição do Zero não existir por qualquer razão eu acabo com o procedimento
    if posiDoZero == []:
        return
    

    if arrow == "^": #Seta para Cima
        if posiDoZero[0]+1 <= 2: #Verificar se o index que quero verificar não estára "out of range", que no caso é entre 0 e 2
            if Joguinho[posiDoZero[0]+1][posiDoZero[1]] != 0: #Se o número que estiver "em baixo" do espaço vazio for um número
                Joguinho[posiDoZero[0]][posiDoZero[1]] = Joguinho[posiDoZero[0]+1][posiDoZero[1]] #Atualizamos a nossa matriz para que o número passe a estar no lugar do 0
                Joguinho[posiDoZero[0]+1][posiDoZero[1]] = 0 #Atualizamos o lugar do número para que passe a ficar lá o 0
                posiDoZero[0] += 1   #Incrementamos mais 1 valor a posição 0 que corresponde às linhas á váriavel que contém a posição do zero
    if arrow == "v": #Seta para Baixo
        if posiDoZero[0]-1 >= 0: #Verificar se o index que quero verificar não estára "out of range", que no caso é entre 0 e 2
            if Joguinho[posiDoZero[0]-1][posiDoZero[1]] != 0: #Verificar se o número que está "em cima" do espaço vazio é de facto um número
                Joguinho[posiDoZero[0]][posiDoZero[1]] = Joguinho[posiDoZero[0]-1][posiDoZero[1]] #Atualizamos a nossa matriz para que o número passe a estar no lugar do 0
                Joguinho[posiDoZero[0]-1][posiDoZero[1]] = 0 #Atualizamos o lugar do número para que passe a ficar lá o 0
                posiDoZero[0] -= 1 #Incrementamos menos um valor no que corresponde as linhas na nossa váriavel que contém a posição do zero

    #O mesmo aplica-se nas duas setas anteriores, só muda que seta para a direito eu ando uma coluna para trás do espaço vazio e seta para a esquerda eu ando uma coluna para a frente do espaço vazio
    if arrow == "<":
        if posiDoZero[1]+1 <= 2:
            if Joguinho[posiDoZero[0]][posiDoZero[1]+1] != 0:
                Joguinho[posiDoZero[0]][posiDoZero[1]] = Joguinho[posiDoZero[0]][posiDoZero[1]+1]
                Joguinho[posiDoZero[0]][posiDoZero[1]+1] = 0
                posiDoZero[1] += 1       
    if arrow == ">":
        if posiDoZero[1]-1 >= 0:
            if Joguinho[posiDoZero[0]][posiDoZero[1]-1] != 0:
                Joguinho[posiDoZero[0]][posiDoZero[1]] = Joguinho[posiDoZero[0]][posiDoZero[1]-1]
                Joguinho[posiDoZero[0]][posiDoZero[1]-1] = 0
                posiDoZero[1] -= 1
    AtualizarMatriz(Joguinho) #Chama um procedimento que vai atualizar a nossa matriz no terminal com as alterações.

#Procedimento que permite construir inicialmente a matriz com o telhado e chão e os separadores                
def MostrarMatriz(matriz):
      #Defino váriaveis globais
      global posiDoZero

      for i in range(3): #Para cada linha
        for k in range(3): #Para cada coluna
            print("┌───┐", end=" ") #Faço um telhado deixo o end vazio para poder escrever os outros telhados
        print("\n") #Quebra de Linha
        for k in range(3): #Para cada coluna
            if matriz[i][k] == 0: #Verifico sempre se o elemonto é 0 
                print("│", " ", "│", end=" ") #Imprimir o espaço vazio e os separadores, contendo o end para poder escrever mais
                posiDoZero = [i,k] #Declarar posição do zero
            else:
                print("│", matriz[i][k], "│", end=" ") #Imprimir o elemento  e os separadores , contendo o end para poder escrever mais

        print("\n") #Quebra de linha
        for k in range(3): #Para cada coluna
            print("└───┘", end=" ") #Faço o chão deixo o end vazio para poder escrever mais chãos
        print("\n") #Quebra de linha
    
#Procedimento que permite atualizar a matriz no terminal, ao usar o pyconio consigo ir a cada quadrado e modificar o valor para o novo    
def AtualizarMatriz(matriz):
    for l in range(3): #Para cada linha
        for c in range(3): #Para cada coluna
            if matriz[l][c] == 0: #Se o elemento for 0
                pyconio.gotoxy(3+(6*c), 5+(6*l)) #O meu primeiro elemento (0,0) ele começa no (3,5) e o "step" de um quadrado para o outro é de 6 no y e no x, ao encontrar este padrão foi possivel realizar isto de forma fácil
                print(" ") #Imprimir espaço vazio
            else:
                pyconio.gotoxy(3+(6*c), 5+(6*l)) #O meu primeiro elemento (0,0) ele começa no (3,5) e o "step" de um quadrado para o outro é de 6 no y e no x, ao encontrar este padrão foi possivel realizar isto de forma fácil
                print(matriz[l][c]) #Imprimir o elemento novo
    CalcularPercentagem(matriz) #Sempre que houver atualização de matriz, vai chamar o procedimento de calcular a percentagem com a nova matriz

#Função cuja única função é lidar com a seta que é premida, só verifica qual é a seta e passa essa informação para o FazerAcontecer
def Movimentacao(seta): #Recebe o parâmetro getch() do pyconio
    if seta == "H": #seta para cima
        return "^"
    else:
        if seta == "M": #seta para a direita
            return ">"
        else:
            if seta == "P": #seta para baixo
                return "v"
            else:   
                return "<" #seta para esquerda

option = "" #Inicializar a váriavel opção que vai conter a tecla que precionamos
# pyconio.clrscr() #Limpar o terminal
MostrarMatriz(Joguinho) #Mostrar pela primeira vez a matriz
started = int(time.time()) #Iniciar a contagem do tempo

while not option.lower() == "x": #Vai verificar sempre se a tecla é a nossa tecla de saída no caso o X, para ser mais semântico não é Case Sensitive
    option = pyconio.getch() #Buscamos o caracter precissonado
    if option == "à": #Se for do "tipo tecla", que é peculiar porque recebe 2 caracteres
        arrow = Movimentacao(pyconio.getch()) #então atribuiu a váriavel a tecla que será identificada por outra função
        contagem += 1 #Incrementamos a contagem de movimentos
        FazerAcontecer(arrow) #Chamamos a função que faz tudo acontecer com a tecla que foi pressionada

MostrarResultados(-1) #Caso o x tenha sido pressionado iremos retornar os resultados com a mensagem de não êxito, pois se o jogo é completado ele já acaba automaticamente não há necessidade de usar o x
