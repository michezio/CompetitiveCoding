#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

/* Both for part one and part two: for part one use the result at
   #1 or pass 1 as argument when calling the executable */

typedef unsigned int uint;

int main(int argc, char *argv[]) {

    // default to 3 but allow for custom values if passed as argument
    uint top_n = argc > 1 ? std::stoi(argv[1]) : 3;

    uint single_elf_calories = 0;
    std::vector<uint> elves;

    std::string line;
    while (std::getline(std::cin, line)) {

        if (line.empty()) {
            elves.push_back(single_elf_calories);
            single_elf_calories = 0;
        } else {
            single_elf_calories += std::stoi(line);
        }
    }

    /*
    The lambda version below does the same as these two lines but faster
    std::sort(elves.begin(), elves.end());
    std::reverse(elves.begin(), elves.end());
    */
    std::sort(elves.begin(), elves.end(), [](const uint &a, const uint &b){return a > b;});
    
    uint sum = 0;
    for (int i = 0; i < top_n; ++i) {
        //std::cout << "#" << i+1 << ":\t" << elves[i] << std::endl;
        sum += elves[i];
    }

    std::cout << "Answer part 1: " << elves[0] << std::endl;
    std::cout << "Answer part 2: " << sum << std::endl;

    return 0;
}