def calculoDeNotas():
  print('Olá Professor, lance a baixo o nome e as notas do seu aluno, referente ao primeiro semestre.')
  aluno1 = input ("Nome do aluno: ")
  if (aluno1 == ""):
    nome = input("O nome do aluno não pode estar em branco.\nPor favor digite novamente:")
    nome = aluno1
  notaA1 = float (input ("Digite a nota do(a) " +aluno1+", referente a 1ª atividade:"))
  while (notaA1 < 0):
    notaRedigitada = float (input ("A nota do aluno não pode ser menor que 0 (Zero).\nPor favor digite novamente: "))
    if(notaRedigitada >= 0):
      notaRedigitada = notaA1
      break
  while (notaA1 > 10):
    notaRedigitadaA1 = float (input ("A nota do aluno não pode ser maior que 10 (Dez).\nPor favor digite novamente: "))
    if (notaRedigitadaA1 <= 10):
      notaRedigitadaA1 = notaA1
      break
  notaP1 = float(input("Digite a nota da 1ª prova: "))
  while (notaP1 < 0):
    notaRedigitadaP1 = float (input ("A nota do aluno não pode ser menor que 0 (Zero)\nPor favor digite novamente: "))
    if (notaRedigitadaP1 >= 0):
      notaRedigitadaP1 = notaP1
      break
  while (notaP1>10):
    notaRedigitadaP1= float (input ("A nota do aluno não pode ser maior que 10 (Dez).\nPor favor digite novamente: "))
    if (notaRedigitadaP1 <= 10):
      notaRedigitadaP1 = notaP1
      break
  print ("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
  print ("|     Agora as notas referente ao segundo semestre         |\n")
  print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
  notaA2 = float (input ("Digite a nota da 2ª atividade: "))
  while (notaA2 < 0):
    notaRedA2 = float (input ("A nota do aluno não pode ser menor que 0 (Zero)\nPor favor digite novamente a nota do aluno: "))
    if (notaRedA2 >= 0):
      notaRedA2 = notaA2
      break
  while (notaA2 > 10):
    notaRedA2 = float (input ("A nota do aluno não pode ser maior que 10 (Dez).\nPor favor digite novamente a nota do aluno: "))
    if (notaRedA2 <= 10):
      notaRedA2 = notaA2
      break
  notaProva2 = float (input ("Digite a nota da 2ª prova: "))
  while (notaProva2 < 0):
    notaRedigitadaP2 = float (input ("A nota do aluno não pode ser menor que 0 (Zero)\nPor favor digite novamente a nota do aluno: "))
    if (notaRedigitadaP2 >= 0):
      notaRedigitadaP2 = notaProva2
      break
  while (notaProva2 > 10):
   notaRedigitadaP2 = float (input ("A nota do aluno não pode ser maior que 10 (Dez).\nPor favor digite novamente a nota do aluno: "))
   if (notaRedigitadaP2 <= 10):
     notaRedigitadaP2 = notaProva2
     break
  notaFinal1S = (float(notaA1 + notaP1)/2)
  notaFinal2S = (float(notaA2 + notaProva2)/2)
  total = (float(notaFinal1S+notaFinal2S)/2)
  print ("Lembrando que a media para aprovação é 7.0")
  if (total >= 7.0):
    print ("PARABÉNS O(A)"+aluno1+"\nVOCÊ ESTÁ APROVADO")
    print ("Esta foi a sua nota:")
    print (total)
  else:
    print ("Poxa "+aluno1+" não foi desta vez.\nMas não desista a vida é cheia de altos e baixos")
    print ("esta foi a sua nota")
    print (total)
calculoDeNotas ()
menu = int (input ("O que você deseja agora?\n 1 - Verificar a média de outro aluno\n 2 - Encerrar por hoje\n"))
if (int (menu == 1)):
  calculoDeNotas()
else:
  print ("Até a proxima!")