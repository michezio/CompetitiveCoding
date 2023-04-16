# NO FAREWELL: KEEP GOOGLE COMPETITIONS ALIVE

# test = ""
# for i in range(300):
#     for let in range(26):
#         test += chr(ord('A')+let) * (i+1)

def run(position):
    #print(f"TEST: {test[position-1]}")
    init = 26
    mod = 1
    while position > init:
        position -= init
        init += 26
        mod += 1

    letter = chr(ord('A') + ((position-1) // mod))
    return letter
    


if __name__ == "__main__":

    TEST = int(input())

    for case_n in range(TEST):
        n = int(input())

        result = run(n)
        print(f"Case #{case_n+1}: {result}")
