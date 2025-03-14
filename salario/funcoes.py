custos = [700, 350, 400, 1100]
ganhos = [5500 , 2300]

def somatoria(lista):
    contador = 0
    soma = 0
    while (contador < len(lista)):
        soma = soma + lista[contador]
        contador = contador + 1
    return soma

somacusto = somatoria(custos)
print("Soma dos custos:" , somacusto)

somaganho = somatoria(ganhos)
print("Soma dos ganhos:", somaganho)

print("Saldo final:" , somaganho - somacusto )