import sys

cr = float(sys.argv[1])

psi = float(0)

vol = float(sys.argv[2])

comp = float(vol / cr)
print("volume=", vol, "liter(s)","compressed volume =", comp) 
while (psi <= 35):
	eff = float(cr * (1 + (psi / 14.7)))
        eff2 = float(cr * (vol * (1 + (psi / 14.7))))
        eff3 = float(cr * psi)
        print(eff, "    ", eff2, "    ", eff3)
	psi += 1
