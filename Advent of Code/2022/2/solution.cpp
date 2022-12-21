#include <iostream>
#include <string>

typedef unsigned int uint;

#define ROCK_L      'A'
#define PAPER_L     'B'
#define SCISSOR_L   'C'

#define ROCK_V      1
#define PAPER_V     2
#define SCISSOR_V   3

#define LOSS    0
#define DRAW    3
#define WIN     6

uint compute_score_1(const char opponent, const char you) {
    uint my_play = (you == 'X') ? ROCK_V : ((you == 'Y') ? PAPER_V : SCISSOR_V);

    if (opponent == ROCK_L) {
        switch (my_play) {
            case ROCK_V:    return my_play + DRAW;
            case PAPER_V:   return my_play + WIN;
            case SCISSOR_V: return my_play + LOSS;
        }
    } else if (opponent == PAPER_L) {
        switch (my_play) {
            case ROCK_V:    return my_play + LOSS;
            case PAPER_V:   return my_play + DRAW;
            case SCISSOR_V: return my_play + WIN;
        }
    } else if (opponent == SCISSOR_L) {
        switch (my_play) {
            case ROCK_V:    return my_play + WIN;
            case PAPER_V:   return my_play + LOSS;
            case SCISSOR_V: return my_play + DRAW;
        }
    }
}

uint compute_score_2(const char opponent, const char you) {
    uint my_play = (you == 'X') ? LOSS : ((you == 'Y') ? DRAW : WIN);

    if (opponent == ROCK_L) {
        switch (my_play) {
            case LOSS: return my_play + SCISSOR_V;
            case DRAW: return my_play + ROCK_V;
            case WIN:  return my_play + PAPER_V;
        }
    } else if (opponent == PAPER_L) {
        switch (my_play) {
            case LOSS: return my_play + ROCK_V;
            case DRAW: return my_play + PAPER_V;
            case WIN:  return my_play + SCISSOR_V;
        }
    } else if (opponent == SCISSOR_L) {
        switch (my_play) {
            case LOSS: return my_play + PAPER_V;
            case DRAW: return my_play + SCISSOR_V;
            case WIN:  return my_play + ROCK_V;
        }
    }
}

int main(int argc, char *argv[]) {

    uint answer_part_1 = 0;
    uint answer_part_2 = 0;

    std::string line;
    while(std::getline(std::cin, line)) {
        answer_part_1 += compute_score_1(line[0], line[2]);
        answer_part_2 += compute_score_2(line[0], line[2]);
    }

    std::cout << "Answer part 1: " << answer_part_1 << std::endl;
    std::cout << "Answer part 2: " << answer_part_2 << std::endl;

    return 0;
}