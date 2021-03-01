import math
import collections
def cosine_similarity(v1,v2):
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x**2
        sumyy += y**2
        sumxy += x*y
    if not sumxx or not sumyy:
        return 0.00
    return sumxy/(math.sqrt(sumxx)*math.sqrt(sumyy))
def round_2(n):
    return ((int)(n*100)/100)
input_query = input("").strip()
d = int(input("").strip())
data = []
for i in range(d):
    data.append(input("").strip())
# Generate dict
vocab = collections.defaultdict(int)
for s in data:
    for word in s.split():
        vocab[word] += 1
leng = len(vocab)
A = [0 for _ in range(leng)]
keys = vocab.keys()
dict = { v:u for (u, v) in enumerate(keys)}
for word in input_query.split():
    if word in dict:
        A[dict[word]] += 1
results = []
for s in data:
    B = [0 for _ in range(leng)]
    for word in s.split():
        if word in dict:
            B[dict[word]] += 1
    results.append((s, cosine_similarity(A,B)))
results.sort(key=lambda x: x[1], reverse=True)
# print(results)
for r in results:    
    print("%s (%.2f)"%(r[0], round_2(r[1])))