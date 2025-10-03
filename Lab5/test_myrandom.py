import myrandom

for i in range(10):
    print(myrandom.myrandom())

print("Test Cycling")

initial = myrandom.myrandom()
count = 0
while myrandom.myrandom() != initial and count < 10000:
    count += 1

if count == 10000:
    print("Went past 10000")
else:
    print("Repeat after",count)
