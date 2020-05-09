TEST = int(input())

answers = []
for _ in range(TEST):
    num = int(input())
    arr = [int(x) for x in input().split()]
    alice_total = 0
    bob_total = 0
    alice_last = 0
    bob_last = 0
    turns = 0
    mmt = 0
    left = 0
    right = len(arr)-1

    while left <= right:
        if mmt == 0:
            alice_last = 0
            mmt = 1
            while alice_last <= bob_last:
                alice_last += arr[left]
                left += 1
                if left > right:
                    break
            alice_total += alice_last
        else:
            bob_last = 0
            mmt = 0
            while bob_last <= alice_last:
                bob_last += arr[right]
                right -= 1
                if left > right:
                    break
            bob_total += bob_last
        turns += 1

    answers.append([turns, alice_total, bob_total])

for ans in answers:
    print(*ans)
