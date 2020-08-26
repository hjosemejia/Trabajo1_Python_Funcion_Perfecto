def funcion_perfecto(num):
	suma = 0
	for i in range(1, num):
		if (num % (i) == 0):
			suma = suma + i
	if num == suma:
		return True
	else:
		return False
                 

def main():
    num = int(input("DIGITE UN NUMERO: "))
    resul = funcion_perfecto(num)
    if  resul == True:
        print(f"EL NUMERO {num} ES PERFECTO ")
    else:
        print(f"EL NUMERO {num} NO ES PERFECTO ")


if __name__ == "__main__":
    main()