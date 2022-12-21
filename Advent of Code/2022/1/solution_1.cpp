#include <iostream>
#include <string>

/* only for part one */

typedef unsigned int uint;

int main(int argc, char *argv[]) {

    uint single_elf_calories = 0;
    uint max_calories = 0;

    std::string line;
    while (std::getline(std::cin, line)) {

        if (line.empty()) {
            if (single_elf_calories > max_calories) {
                max_calories = single_elf_calories;
            }
            single_elf_calories = 0;
        } else {
            single_elf_calories += std::stoi(line);
        }
    }

    std::cout << "Answer: " << max_calories << std::endl;

    return 0;
}