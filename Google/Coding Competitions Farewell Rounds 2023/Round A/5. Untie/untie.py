# NO FAREWELL: KEEP GOOGLE COMPETITIONS ALIVE

def run(people):
    people = [x for x in people]

    starting_pos = 0
    for i in range(len(people)):
        if people[i] != people[i-1]:
            starting_pos = i
            break
    else:
        return str((len(people)+1) // 2)

    changes = 0
    run = 1
    for i in range(starting_pos, starting_pos + len(people)):
        if people[i % len(people)] == people[(i+1) % len(people)]:
            run += 1
        else:
            if run > 1:
                changes += run // 2
                run = 1
    changes += run // 2
            
    return str(changes)

if __name__ == "__main__":

    TEST = int(input())

    for case_n in range(TEST):
        people = input()

        result = run(people)
        print(f"Case #{case_n+1}: {result}")
