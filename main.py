print('Codigo de: [Alexandre Santos]')
print('='*35)

#Ola Agora vamos aprender usar o (for in) com string modificando palavras e colocando espaço entre elas, para da um visual diferente.
#Nesse código para um visual mais dinâmico vamos usar letras maiúsculas para a palavra, observando essa logica eu poderia fazer o código assim como o professor fez na aula como no exemplo a baixo.

#for spaco in palavra:
    #Print(f’ {spaco}’  , end=’’) 

#Dessa forma e o código iria se executado conforme vc mudasse o objeto palavra, porem quem não pratica não aprende, vamos melhorar isso, colocando input para o usuário colocar a palavra que quiser e vamos colocar o comando obrigando transforma toda a palavra digitada em letras maiúsculas 

#dessa forma em baixo.

palavra = input('Digite uma Palavra: ')

for spaco in (palavra.upper()):
  print(f' {spaco}' , end='')
  

#aqui está o código praticar e tudo sei isso hoje rsrrsrsr
