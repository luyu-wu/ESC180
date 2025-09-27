sum = 0
for i in range(1000):
    sum += ((-1)**i)/(2*i+1)

print(sum*4)
sum = 0

i = 0
while i < 1000:
    sum += ((-1)**i)/(2*i+1)
    i += 1
print(sum*4)
