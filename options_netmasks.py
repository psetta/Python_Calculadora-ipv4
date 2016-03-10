valores = [128,64,32,16,8,4,2,1]

def mascaras_posibles():
	mascaras = []
	bits = [0 for x in range(32)]
	for b in range(len(bits)):
		bits[b] = 1
		mascaras.append(bits[:])
	return mascaras
	
def decimal(mascara):
	formato_puntos = []
	formato_decimal_puntos = []
	for i in range(0,32,8):
		formato_puntos.append(mascara[i:i+8])
	for d in formato_puntos:
		res = 0
		for b,v in zip(d,valores):
			if b == 1:
				res += v
		formato_decimal_puntos.append(res)
	return formato_decimal_puntos
	
v = 1
for mask in mascaras_posibles():
	print ".".join(map(str,decimal(mask)))+"\t-> "+"".join(map(str,mask))+" /"+str(v)
	v = v+1
	
			