#include <iostream>
#include <vector>
#include <string>
#include "../common.h"

void draw_pixel(char* crt, int index, int regX, int width) {
    int ind = index % width;
    if (ind == regX-1 || ind == regX || ind == regX+1) {
        crt[index] = '#';
    }
    else {
        crt[index] = ' ';
    }
}

std::string draw_crt(char* crt, int width, int height) {
    std::string rendered;
    for (int i = 0; i < height*width; ++i) {
        if (i % width == 0 && i != 0) {
            rendered += '\n';
        }
        rendered += crt[i];
    }
    return rendered;
}

int main(int argc, char *argv[]) {

    int total = 0;

    int clock = 0;
    int regX = 1;

    char crt[6*40];

    std::string line;
    while (std::getline(std::cin, line)) {
        auto tokens = split(line, " ");

        int clocks_to_go = 0;

        if (tokens[0] == "noop") {
            clocks_to_go = 1;
        }
        else if (tokens[0] == "addx") {
            clocks_to_go = 2;
        }

        while (clocks_to_go--) {


            clock += 1;

            draw_pixel(crt, clock-1, regX, 40);

            if ((clock - 20) % 40 == 0) {
                total += (regX * clock);
            }            
        }

        if (tokens[0] == "addx") {
            regX += std::stoi(tokens[1]);
            // std::cout << "Adding " << std::stoi(tokens[1]) << " -> " << regX << " (CLK: " << clock << ")" << std::endl;
            draw_pixel(crt, clock, regX, 40);
        }
    }

    std::cout << "Answer part 1: " << total << std::endl;
    std::cout << "Answer part 2:" << std::endl << draw_crt(crt, 40, 6) << std::endl;

    return 0;
}