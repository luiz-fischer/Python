def Verbo_To_Be(Pronome):

    Excecao = ["I"]
    Plural = ["You", "They", "We"]
    Singular = ["He", "She", "It"]

    if(Pronome in Excecao):
        print(Pronome + " am")
    elif(Pronome in Singular):
        print(Pronome  + " is")
    elif(Pronome in Plural):
        print(Pronome + " are")
    else:
        print("Pronome Desconhecido")

    Verbo_To_Be("I")
    Verbo_To_Be("You")
    Verbo_To_Be("He")