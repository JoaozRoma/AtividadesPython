popA, popB, anos = 80000, 200000, 0
cresA, cresB = 0.03, 0.015 # Crescimentos de 3% e 1,5% ao ano
while (popA < popB):
anos += 1
popA = popA + (popA * cresA)
popB = popB + (popB * cresB)
print("Após %i anos o país A ultrapassou o país B em número de habitantes." % anos)
print("País A: %.0f" % popA)
print("País B: %.0f" % popB)