#include <iostream>
#include <vector>
#include <string>

#include "../common.h"

typedef unsigned long uint;

std::vector<int> str2int(const std::vector<std::string> strvec) {
    std::vector<int> intvec;
    for (const std::string& str : strvec) {
        intvec.push_back(std::stoi(str));
    }
    return intvec;
}

bool total_overlap(uint r0, uint r1, uint r2, uint r3) {
    return ((r0 <= r2) && (r1 >= r3)) || ((r2 <= r0) && (r3 >= r1));
}

bool partial_overlap(uint r0, uint r1, uint r2, uint r3) {
    return ((r0 >= r2) && (r0 <= r3)) || ((r1 >= r2) && (r1 <= r3)) || ((r2 >= r0) && (r2 <= r1)) || ((r3 >= r0) && (r3 <= r1));
}

int main(int argc, char *argv[]) {

    uint num_total_overlaps = 0;
    uint num_partial_overlaps = 0;

    std::string line;
    while (std::getline(std::cin, line)) {

        std::vector<int> ranges = str2int(split(line, ",-"));

        if (total_overlap(ranges[0], ranges[1], ranges[2], ranges[3])) {
            num_total_overlaps += 1;
        }

        if (partial_overlap(ranges[0], ranges[1], ranges[2], ranges[3])) {
            num_partial_overlaps += 1;
        }
    }   

    std::cout << "Answer part 1: " << num_total_overlaps << std::endl;
    std::cout << "Answer part 2: " << num_partial_overlaps << std::endl;

    return 0;
}