otxobiti = "23"
atobiti = 0
for i, digit in enumerate(reversed(otxobiti)):
    #როგორც ფორმულა MNOPQ = QxB^0 + PxB^1 + O x B^2 + N x B^3 + M x B^4 B=რომელ სისტემაშიც გადადის
    atobiti += int(digit) * 4 ** i
print(atobiti) # Output: 11
