#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <set>

size_t solve_part_1(const std::vector<std::string>& topomap);
size_t solve_part_2(const std::vector<std::string>& topomap);

int main()
{
    std::vector<std::string> topomap;
    
    {
        std::cout << "Parsing input file..." << std::endl;
        std::ifstream file("input.txt", std::fstream::in);
        std::string line;
        while (!file.eof()) {        
            std::getline(file, line);
            topomap.push_back(line);
        }
    }
    
    size_t sol_1 = solve_part_1(topomap);
    std::cout << "Answer part 1: " << sol_1 << std::endl;
    size_t sol_2 = solve_part_2(topomap);
    std::cout << "Answer part 2: " << sol_2 << std::endl;

    return 0;
}

int walk_rec(const std::vector<std::string>& topomap, int x, int y, std::set<std::pair<int, int>>& visited, bool tops_only)
{
    int h = topomap.size();
    int w = topomap[0].size();

    if (tops_only)
    {
        auto p = std::make_pair(x, y);
        auto it = visited.find(p);
        if (it != visited.end())
            return 0;
        visited.insert(it, p);
    }
    
    int next_height = topomap[y][x] + 1;

    if (next_height == '9' + 1)
        return 1;

    int res = 0;

    if (x > 0 && topomap[y][x-1] == next_height)
        res += walk_rec(topomap, x-1, y, visited, tops_only);
    if (x < w-1 && topomap[y][x+1] == next_height)
        res += walk_rec(topomap, x+1, y, visited, tops_only);
    if (y > 0 && topomap[y-1][x] == next_height)
        res += walk_rec(topomap, x, y-1, visited, tops_only);
    if (y < h-1 && topomap[y+1][x] == next_height)
        res += walk_rec(topomap, x, y+1, visited, tops_only);

    return res;
}

inline int walk(const std::vector<std::string>& topomap, int x, int y, bool tops_only)
{
    std::set<std::pair<int, int>> visited;
    return walk_rec(topomap, x, y, visited, tops_only);
}

size_t solve_part_1(const std::vector<std::string>& topomap)
{
    std::cout << "Running part 1..." << std::endl;

    size_t cumul = 0;

    for (int y = 0, height = topomap.size(); y < height; ++y)
    {
        for (int x = 0, width = topomap[0].size(); x < width; ++x)
        {
            if (topomap[y][x] == '0')
            {
                int reachable_tops = walk(topomap, x, y, true);
                cumul += reachable_tops;
            }  

        }
    }

    return cumul;
}


size_t solve_part_2(const std::vector<std::string>& topomap)
{
    std::cout << "Running part 2..." << std::endl;

    size_t cumul = 0;

    for (int y = 0, height = topomap.size(); y < height; ++y)
    {
        for (int x = 0, width = topomap[0].size(); x < width; ++x)
        {
            if (topomap[y][x] == '0')
            {
                int distinct_trails = walk(topomap, x, y, false);
                cumul += distinct_trails;
            }  
        }
    }

    return cumul;
}