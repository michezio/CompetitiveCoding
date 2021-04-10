def compute(word, K):
  score = 0
  for i in range(len(word)//2):
    if (word[i] != word[-i-1]):
      score += 1
  return abs(K - score)
  
results = []

cases_num = int(input())

for i in range(cases_num):
  siz, K = [int(s) for s in input().split(" ")]
  word = input().strip()
  results.append(compute(word, K))

case = 1
for num in results:
  print("Case #{}: {}".format(case, num))
  case += 1
