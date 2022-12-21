#include <iostream>
#include <vector>
#include <string>
#include <stack>

std::vector<std::string> split(const std::string& line, const std::string& separators) {
    std::size_t pos = 0;
    std::size_t next = 0;
    std::vector<std::string> fields;
    while ( next != std::string::npos ) {
        /* FIX_ME: works but not very efficiently, it's better to do the opposite:
           for each char in the remaining string check if it's one of the separators
           and set next to its position. */
        next = UINT32_MAX;
        for (const char sep : separators) {
            std::size_t found = line.find_first_of(sep, pos);
            if (found < next) {
                next = found;
            }
        }
        std::string field = (next == std::string::npos) ? line.substr(pos) : line.substr(pos,next-pos);
        fields.push_back(field);
        pos = next + 1;
    }
    return fields;
}

int main(int argc, char *argv[]) {

    bool status_creating_stack = true;

    std::vector<std::stack<char>> containers_9000;
    std::vector<std::stack<char>> containers_9001;

    std::string line;
    while (std::getline(std::cin, line)) {
        
        if (line == "#") {
            status_creating_stack = false;
            continue;
        }

        if (status_creating_stack) {

            containers_9000.emplace_back(std::stack<char>());
            containers_9001.emplace_back(std::stack<char>());

            std::vector<std::string> elements = split(line, " ");

            for (const std::string &s : elements) {
                containers_9000.back().push(s[0]);
                containers_9001.back().push(s[0]);
            }

        } else {

            std::vector<std::string> operations = split(line, " ");

            std::stack<char> temp_storage_9001;

            int number = std::stoi(operations[0]);
            int origin = std::stoi(operations[1]) - 1;
            int target = std::stoi(operations[2]) - 1;

            while (number--) {
                containers_9000[target].push(containers_9000[origin].top());
                containers_9000[origin].pop();

                temp_storage_9001.push(containers_9001[origin].top());
                containers_9001[origin].pop();
            }

            while (temp_storage_9001.size()) {
                containers_9001[target].push(temp_storage_9001.top());
                temp_storage_9001.pop();
            }
        }
    }

    std::string answer1;
    std::string answer2;

    for (std::stack<char> const& stack : containers_9000) {
        answer1 += stack.top();
    }

    for (std::stack<char> const& stack : containers_9001) {
        answer2 += stack.top();
    }

    std::cout << "Answer part 1: " << answer1 << std::endl;
    std::cout << "Answer part 2: " << answer2 << std::endl;

    return 0;
}