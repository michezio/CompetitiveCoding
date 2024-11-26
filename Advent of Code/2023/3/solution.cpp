#include <map>
#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <string>

struct Solutions
{
    size_t sol_1;
    size_t sol_2;
};

Solutions solve_part_1_and_2(const std::vector<std::string>& lines);

int main()
{
    std::ifstream file("input.txt", std::fstream::in);

    std::vector<std::string> lines;

    while (!file.eof())
    {
        std::string line;
        std::getline(file, line);
        if (line.empty())
            break;
        std::stringstream ss;
        ss << '.' << line << '.'; // add left-right padding
        lines.push_back(ss.str());
    }

    file.close();

    // add top-bottom padding
    lines.emplace(lines.begin(), lines.at(0).size(), '.');
    lines.emplace_back(lines.at(0).size(), '.');

    Solutions s = solve_part_1_and_2(lines);
    std::cout << "Answer part 1: " << s.sol_1 << std::endl;
    std::cout << "Answer part 2: " << s.sol_2 << std::endl;

    return 0;
}

Solutions solve_part_1_and_2(const std::vector<std::string>& lines)
{
    size_t cum_sum_1 = 0;
    size_t cum_sum_2 = 0;

    std::map<int, std::vector<int>> gears_map;

    // solve for part 1 and build gear map for part 2

    for (int i = 1; i < lines.size() - 1; ++i)
    {
        int pos = 1;
        while(pos < lines[i].size() - 1)
        {
            while(pos < lines[i].size() - 1 && !std::isdigit(lines[i][pos]))
                ++pos;

            if (pos == lines[i].size() - 1)
                continue;

            int len = 1;

            while(pos + len < lines[i].size() && std::isdigit(lines[i][pos + len]))
                ++len;

            int number = std::stoi(lines[i].substr(pos, len));

            bool is_part = false;
            for (int y = i-1; y <= i+1; ++y)
            {
                for (int x = pos - 1; x <= pos + len; ++x)
                {
                    char c = lines[y][x];

                    is_part |= !std::isdigit(c) && c != '.';

                    // if next to a * append the number to the gear map for this * location
                    if (c == '*')
                    {
                        int gear_key = y * 1000 + x;
                        gears_map[gear_key].push_back(number);
                    }
                }
            }

            if (is_part)
            {
                cum_sum_1 += std::stoi(lines[i].substr(pos, len));
            }

            pos += len + 1;
        }
    }


    // solve part 2 with gear map built in part 1

    for (auto gears : gears_map)
    {
        if (gears.second.size() == 2)
        {
            cum_sum_2 += gears.second[0] * gears.second[1];
        }
    }

    return { cum_sum_1, cum_sum_2 };
}
