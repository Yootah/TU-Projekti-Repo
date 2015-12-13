f = open("06.txt")
o = open("_06.txt", "w")
for r in f:
    r = r.replace("G","M").replace("g", "m").replace("S", "Z").replace("s", "z").replace("L", "N")
    o.write(r)
    
f.close()
o.close()
