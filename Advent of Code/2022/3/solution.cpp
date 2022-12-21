#include <iostream>
#include <string>
#include <bitset>
#include <vector>

typedef unsigned int uint;

uint priority(char item) {
    if (std::isupper(item)) {
        return (uint)item - (uint)'A' + 27;
    } else {
        return (uint)item - (uint)'a' + 1;
    }
}

std::bitset<52> generate_bitset(std::string str) {
    std::bitset<52> bitset;

    for (auto c = str.begin(); c != str.end(); ++c) {
        bitset[priority(*c) - 1] = 1;
    }

    return bitset;
}

int find_set_bit(std::bitset<52> bitset) {
    for (uint i = 0; i < 52; ++i) {
        if (bitset.test(i)) return i;
    }
    return -1;
}

int find_duplicated_item(std::string rucksack) {

    std::string first = rucksack.substr(0, rucksack.length()/2);
    std::string second = rucksack.substr(rucksack.length()/2);

    auto comp_1 = generate_bitset(first);
    auto comp_2 = generate_bitset(second);

    auto duplicated = comp_1 & comp_2;

    return find_set_bit(duplicated) + 1;
}

int find_badge(std::string first, std::string second, std::string third) {

    auto comp_1 = generate_bitset(first);
    auto comp_2 = generate_bitset(second);
    auto comp_3 = generate_bitset(third);

    auto badge = comp_1 & comp_2 & comp_3;

    return find_set_bit(badge) + 1;
}

int main(int argc, char *argv[]) {

    uint duplicates_priorities = 0;
    uint badges_priorities = 0;

    std::vector<std::string> group;

    std::string line; 
    while (std::getline(std::cin, line)) {
        duplicates_priorities += find_duplicated_item(line);

        group.push_back(line);
        if (group.size() == 3) {
            badges_priorities += find_badge(group[0], group[1], group[2]);
            group.clear();
        }
    }

    std::cout << "Answer part 1: " << duplicates_priorities << std::endl;
    std::cout << "Answer part 2: " << badges_priorities << std::endl;

    return 0;
}