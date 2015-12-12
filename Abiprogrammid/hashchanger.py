f = open("03.txt")
o = open("_03.txt", "w")
for r in f:
    r = r.replace("I","G").replace("i", "G")
    o.write(r)
    
f.close()
o.close()
