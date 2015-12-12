f = open("01.txt")
o = open("_01.txt", "w")
for r in f:
    o.write(r.replace("#","G"))
f.close()
o.close()
