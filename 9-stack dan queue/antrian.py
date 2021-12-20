from collections import deque

antrian = deque([1,2,3,4,5])

print(antrian)

antrian.append(6)

out = antrian.popleft()
print(antrian)