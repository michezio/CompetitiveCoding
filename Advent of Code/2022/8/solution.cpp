#include <iostream>
#include <string>
#include <vector>


int main(int argc, char *argv[]) {

    // Building file system

    int forest[99][99];
    int visibility[99][99];

    for (int i = 0; i < 99; ++i) {
        for (int j = 0; j < 99; ++j) {
            visibility[i][j] = 0;
        }
    }
    
    int row = 0;

    std::string line;
    while (std::getline(std::cin, line)) {
        if (row == 99) {
            break;
        }
        
        int col = 0;
        for (char c : line) {
            forest[row][col++] = (int)(c - '0');
        }
        ++row;
    }

    // left to right
    for (int i = 0; i < 99; ++i) {
        int height = -1;
        for (int j = 0; j < 99; ++j) {
            if (forest[i][j] > height) {
                visibility[i][j] = 1;
                height = forest[i][j];
                if (height == 9) {
                    break;
                }
            }
        }
    }

    // right to left
    for (int i = 0; i < 99; ++i) {
        int height = -1;
        for (int j = 98; j >= 0; --j) {
            if (forest[i][j] > height) {
                visibility[i][j] = 1;
                height = forest[i][j];
                if (height == 9) {
                    break;
                }
            }
        }
    }

    // up to down
    for (int j = 0; j < 99; ++j) {
        int height = -1;
        for (int i = 0; i < 99; ++i) {
            if (forest[i][j] > height) {
                visibility[i][j] = 1;
                height = forest[i][j];
                if (height == 9) {
                    break;
                }
            }
        }
    }

    // down to up
    for (int j = 0; j < 99; ++j) {
        int height = -1;
        for (int i = 98; i >= 0; --i) {
            if (forest[i][j] > height) {
                visibility[i][j] = 1;
                height = forest[i][j];
                if (height == 9) {
                    break;
                }
            }
        }
    }

    int visible_trees = 0;
    for (int i = 0; i < 99; ++i) {
        for (int j = 0; j < 99; ++j) {
            visible_trees += visibility[i][j];
            // std::cout << visibility[i][j];
        }
        // std::cout << std::endl;
    }

    std::cout << "Answer part 1: " << visible_trees << std::endl;

    int max_scenic_score = 0;

    for (int si = 0; si < 99; ++si) {
        for (int sj = 0; sj < 99; ++sj) {
            int height = forest[si][sj];
            int right_dist = 1;
            for (int j = sj+1; j < 98; ++j) {
                if (forest[si][j] < height) {
                    ++right_dist;
                } else break;
            }
            int left_dist = 1;
            for (int j = sj-1; j >= 1; --j) {
                if (forest[si][j] < height) {
                    ++left_dist;
                } else break;
            }
            int down_dist = 1;
            for (int i = si+1; i < 98; ++i) {
                if (forest[i][sj] < height) {
                    ++down_dist;
                } else break;
            }
            int up_dist = 1;
            for (int i = si-1; i >= 1; --i) {
                if (forest[i][sj] < height) {
                    ++up_dist;
                } else break;
            }
            int scenic_score = right_dist * left_dist * down_dist * up_dist;
            if (scenic_score > max_scenic_score) {
                max_scenic_score = scenic_score;
            }
        }
    }

    std::cout << "Answer part 2: " << max_scenic_score << std::endl;

    return 0;
}