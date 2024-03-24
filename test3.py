n = 15
ans = 0
for i in range(1,n+1):
  if i % 3 == 0 : ans += 1
  elif i % 5 == 0 : ans += 1
  #elif i % 7 == 0 : ans += 1
  print(i)

print(ans)