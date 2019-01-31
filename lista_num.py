""""Este programa em Python cria um arquivo em disco e o prepara para escrever.
 Arquivo criado para armazenar uma lista de inteiros em formato txt."""

file=open('numeros.txt','w')   #cria e abre arquivo para formato txt para gravação armazenando na variável file.
for x in range(0,150):         #a variável x percorre pela faixa de valores de 0 a 149.
    file.write(str(x)+' ')     #a variável file recebe o valor x convertido em string mais o espaço em branco gravando no arquivo txt
file.close()                   #fecha arquivo.


