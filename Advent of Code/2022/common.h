#ifndef COMMON_H
#define COMMON_H

#include <string>
#include <vector>

std::vector<std::string> split(const std::string& line, const std::string& separators) {
    std::size_t pos = 0;
    std::size_t next = 0;
    std::vector<std::string> fields;
    while ( next != std::string::npos ) {
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

std::string indent(int number) {
    std::string s;
    while (number--) {
        s += "\t";
    }
    return s;
}

#endif // COMMON_H