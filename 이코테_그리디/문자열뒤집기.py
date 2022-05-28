
n = input()
counter = 0
for i in range(1,len(n)):
    if n[i] == n[i-1]:
        continue
    else:

        counter += 1
print((counter+1)//2) # 이거만 이해하고싶다..