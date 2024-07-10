#4th program
a, b = 13.42, 42.13
aq, bq = int (a), int (b)
aw, bw =  int ((a - aq) * 100), int ((b - bq) * 100)
print (aq == bw or bq == aw)

