def funcion_perfecto(num):
	suma = 0
	for i in range(1,num):
		if (num % (i) == 0):
			suma = suma + i
	if num == suma:
		print(f"EL NUMERO {num} ES PERFECTO ")
	else:
		print(f"EL NUMERO {num} NO ES PERFECTO ")
 

def main():
    num = int(input("DIGITE UN NUMERO: "))
    funcion_perfecto(num)

if __name__ == "__main__":
    main()