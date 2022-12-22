#include <iostream>
#include <string>

#include "../common.h"

#define ROPE_LENGTH 10

struct Vec2D {
    int x;
    int y;
};

Vec2D adjust_node_position(Vec2D &tail, Vec2D &head) {
    Vec2D new_position = { tail.x, tail.y };
    Vec2D dist = { head.x - tail.x, head.y - tail.y };
    if (dist.x*dist.x + dist.y*dist.y > 2) {
        new_position.x += (dist.x > 0) ? 1 : ((dist.x < 0) ? -1 : 0);
        new_position.y += (dist.y > 0) ? 1 : ((dist.y < 0) ? -1 : 0);
    }
    return new_position;
}

int main(int argc, char *argv[]) {
    // possible coordinates: x = [-220 : 46], y = [-299 : 64]
    int tail_visited[500][500];
    int rope_visited[500][500];
    for (int i = 0; i < 500; ++i) {
        for (int j = 0; j < 500; ++j) {
            tail_visited[i][j] = 0;
            rope_visited[i][j] = 0;
        }
    }
    Vec2D offset = { 300, 300 };
    
    std::vector<Vec2D> nodes;
    for (int i = 0; i < ROPE_LENGTH; ++i) {
        nodes.push_back({0, 0});
    }

    Vec2D *head = &nodes[0];
    Vec2D *tail = &nodes[1];
    Vec2D *rope = &nodes.back();

    std::string line;
    while (std::getline(std::cin, line)) {
        auto tokens = split(line, " ");
        char direction = tokens[0].at(0);
        int steps = std::stoi(tokens[1]);

        while (steps--) {
            switch (direction) {
                case 'R': head->x++; break;
                case 'L': head->x--; break;
                case 'D': head->y++; break;
                case 'U': head->y--; break;
            }

            for (int i = 1; i < ROPE_LENGTH; ++i) {
                nodes[i] = adjust_node_position(nodes[i], nodes[i-1]);
            }

            tail_visited[tail->y + offset.y][tail->x + offset.x] = 1;
            rope_visited[rope->y + offset.y][rope->x + offset.x] = 1;
        }
    }

    int total_tail_visited = 0;
    int total_rope_visited = 0;
    for (int i = 0; i < 500; ++i) {
        for (int j = 0; j < 500; ++j) {
            total_tail_visited += tail_visited[i][j];
            total_rope_visited += rope_visited[i][j];
        }
    }

    std::cout << "Answer part 1: " << total_tail_visited << std::endl;
    std::cout << "Answer part 2: " << total_rope_visited << std::endl;

    return 0;
}