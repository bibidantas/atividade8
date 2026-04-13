#Pesquisa de satisfação do cliente - TudoWeb

#Contadores
Excelente = 0
Ruim = 0

#Estrutura de repetição para 50 entrevistados
for i in range(1, 11):
    print(f"\n---Entrevistado {i}---")
    print("Olá! Seja bem vindo(a) a nossa pesquisa de atendimento ao cliente! Queremos saber sua opnião e experiência com nossa plataforma.")

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    avaliação = int(input("Como você avalia nosso atendimento, sendo: 1 - EXCELENTE, 2 - BOM, 3 - RUIM "))

    #Estrutura de decisão para avaliação do cliente
    if avaliação == 1:
        print(f"Obrigado por sua avaliação EXCELENTE, {nome}, esperamos continuar atendendo suas expectativas!")
        Excelente += 1

    elif avaliação == 2: 
        print(f"Agradecemos sua avaliação BOM, {nome}, estamos sempre buscando melhorar para oferecer um atendimento EXCELENTE!")
   
    elif avaliação == 3:
        print(f"Lamentamos que sua experiência tenha sido RUIM, {nome}. Agradecemos seu feedback e trabalharemos para melhorar nosso atendimento.")
        Ruim += 1

    else:
        print("Opção inválida. Por favor, avalie usando os números 1, 2 ou 3.")

#Resultado final

print("\n=====Resultado da Pesquisa de Satisfação=====")
print(f"Total de avaliações EXCELENTE: {Excelente}")
print(f"Total de avalições RUIM: {Ruim}")

