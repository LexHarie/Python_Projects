P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281]


for p in P:
  qr = [ x**2 % p for x in range(1, int((p-1)/2) + 1)]
  
  list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, p - 2, p - 3, p - 5, p- 7, p- 11, p - 13, p- 17, p- 19, p-23 , p-29]
  
  qc = []
  
  
      
  for items in list:
      if items in qr:
          qc.append(1)
      else:
          qc.append(-1)
  
  
  
  print(qc)