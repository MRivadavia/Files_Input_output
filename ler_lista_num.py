""""Este arquivo le o conteúdo de dados apenas numéricos de um arquivo txt
    identificando o inteiro no arquivo, lembrando que os dados estão em formato string,
    lendo os espaços em branco distinguindo dos números e retornando em tipo inteiro na saída.
    """

file=open('numeros.txt','r') #Abre arquivo para formato leitura
linhas=file.read() # arquivo armazenado na variável linhas, tipo string.
num=''             # variável de inicialização para receber por concatenação "strings numéricas".
for l in linhas:   #loop for em que uma variável de contagem le a variável linhas string por string.
    if l!=' ':     #Se a variável l for diferente da string "espaço em branco", então
        num=num+l  #acumulador por concatenação.
    else:          #Senão, pára a concatenação, converte a variável num em INTEIRO E a esvazia  num.
        print(int(num),end=' ')
        num=''
    file.close()   #fecha arquivo em disco.