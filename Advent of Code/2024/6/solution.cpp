#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <set>

struct Direction {
    int dx, dy;
};

constexpr Direction dirs[4] = {
    { 0, -1 }, { 1, 0 }, { 0, 1 }, { -1, 0 }
};

struct Field
{
    std::vector<char> cell;
    size_t width = 0;
    size_t height = 0;
    size_t start_x = 0;
    size_t start_y = 0;

    char& at(size_t x, size_t y) noexcept { 
        return cell[y * width + x];
    }

    bool addRow(const std::string& row) noexcept {
        if (width == 0)
            width = row.size();
        else if (width != row.size())
            return false;
        for (size_t i = 0, len = row.size(); i < len; ++i) {
            if (row[i] == '^') {
                start_x = i;
                start_y = height;
                break;
            }
        }
        cell.insert(cell.end(), row.begin(), row.end());
        ++height;
        return true;
    }
};

struct Solutions
{
    size_t sol_1;
    size_t sol_2;
};

Solutions solve_part_1_and_2(Field& field);

int main()
{
    Field field;
    
    {
        std::ifstream file("input.txt", std::fstream::in);
        std::string line;
        while (!file.eof()) {        
            std::getline(file, line);
            if (!field.addRow(line)) {
                std::cout << "Something went wrong!!" << std::endl;
                exit(1);
            }
        }
    }
    
    Solutions s = solve_part_1_and_2(field);
    std::cout << "Answer part 1: " << s.sol_1 << std::endl;
    std::cout << "Answer part 2: " << s.sol_2 << std::endl;

    return 0;
}

using VisitPos = std::tuple<int16_t, int16_t>;

std::set<VisitPos> just_visit(Field& field)
{
    std::set<VisitPos> visited;
    int16_t angle = 0;
    int16_t x = field.start_x;
    int16_t y = field.start_y;
    Direction dir = dirs[angle];

    while (true) 
    {
        visited.emplace(x, y);

        int nx = x + dir.dx; 
        int ny = y + dir.dy;

        if (!(0 <= nx && nx < field.width) || !(0 <= ny && ny < field.height))
            break;

        if (field.at(nx, ny) == '#') 
        {
            angle = (angle + 1) % 4;
            dir = dirs[angle];
        } 
        else 
        {
            x = nx;
            y = ny;
        }
    }   

    return std::move(visited);
}

using VisitPosAngle = std::tuple<int16_t, int16_t, int8_t>;

static size_t iters = 0;

bool detect_loop(Field& field) 
{
    std::set<VisitPosAngle> visited;
    int16_t angle = 0;
    int16_t x = field.start_x;
    int16_t y = field.start_y;
    Direction dir = dirs[angle];

    while (true) 
    {
        ++iters;

        auto st = visited.emplace(x, y, angle);
        if (!st.second)
            return true; // already visited with same angle, loop detected

        int nx = x + dir.dx; 
        int ny = y + dir.dy;

        if (!(0 <= nx && nx < field.width) || !(0 <= ny && ny < field.height))
            break;

        if (field.at(nx, ny) == '#') 
        {
            angle = (angle + 1) % 4;
            dir = dirs[angle];
        } 
        else 
        {
            x = nx;
            y = ny;
        }
    }   

    return false;
}

Solutions solve_part_1_and_2(Field& field)
{
    std::cout << "Running..." << std::endl;

    Solutions s;

    std::set<VisitPos> visited = just_visit(field);

    s.sol_1 = visited.size();
    s.sol_2 = 0;

    for (const VisitPos& v : visited)
    {
        char& c = field.at(std::get<0>(v), std::get<1>(v));
        c = '#';
        s.sol_2 += detect_loop(field);
        c = '.';
    }
    
    std::cout << "Iterations: " << iters << std::endl;

    return s;
}