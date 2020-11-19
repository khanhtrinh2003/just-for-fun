nui = []
lol = int(input('Enter the length of list: '))
for m in range(0, lol):
	x = int(input('value: '))
	nui.append(x)
energy = 0;
start = nui[0]
print(nui)

for i in range(1,len(nui)-1):
	if nui[i] < nui[i+1]:
		if nui[i+1] > start:
			energy += nui[i+1] - nui[i]
			if i < len(nui) - 2:
				if nui[i+1] > nui[i+2]:
					start = nui[i+1]
			else: continue
		else: continue
	elif start < nui[i]:
		energy += nui[i] - nui[i-1]
		if nui[i] > nui[i+1]:
			start = nui[i]
		else: continue
	else: continue
print(energy)
