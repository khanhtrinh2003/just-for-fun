N = int(input('So chu so: '))
S = int(input('Tong cac chu so'))
Dau = 9
Tong = 0
while N != 0 : 
	Num = Dau * (10**(N-1))
	if Num/(10**(N-1)) < S:
		Tong += Num
		S -= Dau
		N -= 1
		Dau = 9
		if N == 0 :
			print(-1)
			break
		else : continue

	elif Num/(10**(N-1)) > S:
		Dau -= 1
		continue

	elif Num/(10**(N-1)) == S:
		Tong += Num
		print(Tong)
		break