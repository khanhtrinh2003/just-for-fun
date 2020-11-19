mfilter = []
giatri = []
so_qua = int(input('Enter the number of gift: '))
so_nguoi = int(input('Enter the number of people: '))
dem = 0
tong = 0
sumt = 0
for i in range(0, so_qua):
	x = int(input('enter the value: '))
	giatri.append(x)

print(giatri)

for i in range(0, so_qua):
	if giatri[i] not in mfilter:
		mfilter.append(giatri[i])
print(mfilter)
print(len(giatri))
for i in range(0, so_nguoi):
	dau = int(input('Start: '))
	sau = int(input('End: '))

	for j in range(0, len(mfilter)):
		for m in range(dau-1, sau):
			if mfilter[j] == giatri[m]:
				dem += 1
			else: continue
		tong += dem * dem * mfilter[j]
		sumt += tong
		tong = 0
		dem = 0
	print('Nguoi', i+1,'nhan qua co gia tri la ', sumt)
	sumt =0 
