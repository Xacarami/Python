def tem_sete_letras(palavra):
    if len(palavra) == 7:
        return True
    else:
        return False


if tem_sete_letras("12345678"):
    print("Confia que tem 7")
else:
    print("não tem não")