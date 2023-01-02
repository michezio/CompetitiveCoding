#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#include "../common.h"

#define DEBUG false

typedef unsigned long long ull_t;

class Monkey {

private:
    void (*m_op)(ull_t &);          // operation to apply for each monkey (lambda)
    ull_t m_test;                   // divisibility test value
    ull_t m_true;                   // monkey to throw to when check is passed
    ull_t m_false;                  // monkey to throw to when check fails
    ull_t m_inspections;            // total number of inspection made by the monkey
    std::vector<ull_t> m_objects;   // current object list (only the current worry level of each object)

public:
    static ull_t worry_division;
    static ull_t modulo;

    Monkey(void(*operation)(ull_t &), ull_t worry_test, ull_t monkey_true, ull_t monkey_false)
        : m_op(operation), m_test(worry_test), m_true(monkey_true), m_false(monkey_false), m_inspections(0)
        {
            // each added monkey updates the LCM for the modulo arithmetic with its m_test value
            // it doesn't check for common prime factors but only checks if modulo is already
            // divisible by the new m_test value to avoid prime factors repetition.
            // it may be larger than the real LCM if non prime numbers are use as m_test
            // since some of their prime factors may have been already added, but
            // the modulo arithmetics applyes the same way (just with a larger modulo)
            // since it's only used for divisibility checks
            modulo *= (modulo % m_test == 0) ? 1 : m_test;
        }

    ull_t inspect(ull_t index)
    {   
        // run inspection on object at index
        m_inspections++;
        if (DEBUG) std::cout << "  Monkey inspects an item with worry level " << m_objects[index] << std::endl;

        // execute the operation on the worry level
        m_op(m_objects[index]);
        if (DEBUG) std::cout << "    New worry level " << m_objects[index] << std::endl;

        // reduce worry level if worry_division is not 1 else use modular arithmetic
        if (worry_division != 1)
        {
            m_objects[index] /= Monkey::worry_division;
            if (DEBUG) std::cout << "    Monkey gets bored, new worry level is " << m_objects[index] << std::endl;
        }
        else
        {
            m_objects[index] %= modulo;
            if (DEBUG) std::cout << "    New worry level (modulo) is " << m_objects[index] << std::endl;
        }

        // run divisibility test and throw to the chosen monkey
        if (m_objects[index] % m_test == 0)
        {
            if (DEBUG) std::cout << "    Current worry level is divisible by " << m_test << std::endl;
            if (DEBUG) std::cout << "    Item with worry level " << m_objects[index] << " is thrown to monkey " << m_true << std::endl;
            return m_true;
        }
        else {
            if (DEBUG) std::cout << "    Current worry level is not divisible by " << m_test << std::endl;
            if (DEBUG) std::cout << "    Item with worry level " << m_objects[index] << " is thrown to monkey " << m_false << std::endl;
            return m_false;
        }
    }

    void receive(ull_t object) {
        m_objects.push_back(object);
    }

    void add_items(std::vector<int> objects) {
        for (auto num : objects)
        {
            m_objects.push_back(num);
        }
    }

    void exec(std::vector<Monkey> &monkeys) {
        for (ull_t index = 0; index < m_objects.size(); ++index) {
            ull_t new_monkey = inspect(index);
            monkeys[new_monkey].receive(m_objects[index]);
        }
        m_objects.clear();
    }

    ull_t get_inspections() {
        return m_inspections;
    }

    std::string print_objects() {
        std::string s;
        s += "[ ";
        for (ull_t o : m_objects) {
            s += o + " ";
        }
        s += "]";
        return s;
    }
};

ull_t Monkey::worry_division = 1;
ull_t Monkey::modulo = 1;

void generate_monkeys(std::vector<Monkey> &monkeys, ull_t worry_division) {

    // generates the monkeys based on the input file (manually parsed)

    Monkey::worry_division = worry_division;
    Monkey::modulo = 1;

    /* Monkey 0 */
    monkeys.emplace_back([](ull_t &a){a*=7;}, 5, 1, 6);
    monkeys.back().add_items({ 74, 64, 74, 63, 53 });

    /* Monkey 1 */
    monkeys.emplace_back([](ull_t &a){a*=a;}, 17, 2, 5);
    monkeys.back().add_items({ 69, 99, 95, 62 });
    
    /* Monkey 2 */
    monkeys.emplace_back([](ull_t &a){a+=8;}, 7, 4, 3);
    monkeys.back().add_items({ 59, 81 });

    /* Monkey 3 */
    monkeys.emplace_back([](ull_t &a){a+=4;}, 13, 0, 7);
    monkeys.back().add_items({ 50, 67, 63, 57, 63, 83, 97 });

    /* Monkey 4 */
    monkeys.emplace_back([](ull_t &a){a+=3;}, 19, 7, 3);
    monkeys.back().add_items({ 61, 94, 85, 52, 81, 90, 94, 70 });

    /* Monkey 5 */
    monkeys.emplace_back([](ull_t &a){a+=5;}, 3, 4, 2);
    monkeys.back().add_items({ 69 });
    
    /* Monkey 6 */
    monkeys.emplace_back([](ull_t &a){a+=7;}, 11, 1, 5);
    monkeys.back().add_items({ 54, 55, 58 });

    /* Monkey 7 */
    monkeys.emplace_back([](ull_t &a){a*=3;}, 2, 0, 6);
    monkeys.back().add_items({ 79, 51, 83, 88, 93, 76 });
}

void generate_example_monkeys(std::vector<Monkey> &monkeys, ull_t worry_division) {

    // generates the monkeys based on the example on the website

    Monkey::worry_division = worry_division;
    Monkey::modulo = 1;

    /* Monkey 0 */
    monkeys.emplace_back([](ull_t &a){a*=19;}, 23, 2, 3);
    monkeys.back().add_items({ 79, 98 });

    /* Monkey 1 */
    monkeys.emplace_back([](ull_t &a){a+=6;}, 19, 2, 0);
    monkeys.back().add_items({ 54, 65, 75, 74 });

    /* Monkey 2 */
    monkeys.emplace_back([](ull_t &a){a*=a;}, 13, 1, 3);
    monkeys.back().add_items({ 79, 60, 97 });

    /* Monkey 3 */
    monkeys.emplace_back([](ull_t &a){a+=3;}, 17, 0, 1);
    monkeys.back().add_items({ 74 });
}

void run_keep_away(std::vector<Monkey> &monkeys, ull_t turns, ull_t print_debug_every = 1000) {
    for (ull_t turn = 0; turn < turns; ++turn) {
        for (ull_t i = 0; i < monkeys.size(); ++i) {
            if (DEBUG) std::cout << "Monkey " << i << ":" << std::endl;
            monkeys[i].exec(monkeys);
        }

        if (print_debug_every > 0 && (turn+1) % print_debug_every == 0) {
            std::cout << std::endl << "Status after turn " << turn + 1 << std::endl;
            for (ull_t i = 0; i < monkeys.size(); ++i) {
                std::cout << "Monkey " << i << ": " /*<< monkeys[i].print_objects()*/ << " (" << monkeys[i].get_inspections() << " inspections)" << std::endl; 
            }
            std::cout << std::endl;
        }
    }
}

ull_t compute_monkey_business(std::vector<Monkey> &monkeys) {
    std::vector<ull_t> inspections;
    for (Monkey monk : monkeys) {
        inspections.push_back(monk.get_inspections());
    }
    std::sort(inspections.begin(), inspections.end(), [](ull_t a, ull_t b){return a > b;});
    return inspections[0] * inspections[1];
}


int main(int argc, char *argv[]) {

    // For this problem the input is treated as a "build guide", see generate functions

    std::vector<Monkey> monkeys;

    generate_monkeys(monkeys, 3);
    run_keep_away(monkeys, 20, 0);
    std::cout << "Answer part 1: " << compute_monkey_business(monkeys) << std::endl;

    monkeys.clear();

    generate_monkeys(monkeys, 1);
    run_keep_away(monkeys, 10000, 0);
    std::cout << "Answer part 2: " << compute_monkey_business(monkeys) << std::endl;

    return 0;
}