def singleNumber(A):
  answer = 0
  for i in range(32):
    count = 0
    for num in A:
      if num & (1 << i):
        count +=1
    if (count % 3) != 0:
      answer |= (1<<i)
  return answer
A = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
print(singleNumber(A))