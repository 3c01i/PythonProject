f = open("optfore.txt")
l = open("Sell_base_2600_1.txt","w")
for i in f:
    i = i.split(" | ", maxsplit=1)[0].strip()
    i = i.split("|", maxsplit=1)[0].strip()
    i = i.split("Telegram id", maxsplit=1)[0].strip()
    i = i + '\n'
    l.write(i)
f.close()
l.close()
    
