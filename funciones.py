

def es_primo(num):
    if num <= 1:
        return False
        for i in range (2,int(num ** 0.5)+ 1)
        if num % i ==0 
        return False
    return true 

def encontrar_primos_gemelos(limit)
 primos_gemelos[]
 for num in range (2, limit-1)
  if es_primo(num) and es_primo(num+2):
    primos_gemelos.append((num, num+2))
    return primos_gemelos 


def es_palindromo (num)
return str(num)== str(num)[::-1]

def encontrar_palindromo_primo(limit)
palindromo_primo:[]
for num in range(10, limit +1 ):
    if es_primo(num) and es_palindromo(num):
        palindromo_primo.append(num)
        return palindromo_primo


def main():
    while True:
        print("selecciona una opcion: ")
        print("1: Encontrar y mostrar pares de números primos gemelos en un rango dado: ")
        print("2: Encontrar y mostrar números primos palindrómicos en un rango dado: ")
        print("3: Salir del programa")
        opcion = input("> ")
        if opcion=="1":
            limite=int(input("ingrese el limite superior: "))
            primos_gemelos= encontrar_primos_gemelos(limit)
            print("coincidencia de pares primos gemelos: "+ primos_gemelos)
            elif option=="2":
                limit=int(input("ingrese el limite superior"))
                palindromo_primo= encontrar_palindromo_primo(limit)
                print("coincidencia de palindricos primos: "+ palindromo_primo)
                elif opcion=="3":
                    print("saliendo del programa")
                    break
                    else:
                        print("opcion no valida intente de nuevo") 
                        if __name__=="__main__":
                            main()