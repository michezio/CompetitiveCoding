/*
    GOOD SOLUTION TO THE WRONG PROBLEM >_<

    I misread part 2 and was thinking that there could only be 1 pipe 
    operator and it merged left and right parts together, eg.

    6 8 6 15 -> (6 * 8) || (6 * 15) -> 48 || 90 -> 4890

    Of course I didn't bother to check the examples where that same operation
    yields 7290 and moreover, nowhere is mentioned that there could be only
    one pipe operator. Well, not too bad, due to illness I was not competing
    for any leaderboard today since I woke up pretty late. 

    Anyway, I think this solution is nice nonetheless so I'd like to keep it :)
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <string>

static void print_progress_bar(float progress_0_1)
{
	static constexpr int bar_size = 40;
	static char progress_bar[(size_t)bar_size + 1];

	int bar_pos = (int)floor(progress_0_1 * (bar_size - 1));
	float bar_perc = 100.f * progress_0_1;

    memset(progress_bar, '=', bar_pos);
	progress_bar[bar_pos] = '>';
	progress_bar[bar_pos + 1] = '\0';

	printf("\r[%-*s] %.1f%%  ", bar_size, progress_bar, bar_perc);
}

static std::vector<std::string> split(const std::string& line, const std::string& separators)
{
    size_t pos = 0;
    std::vector<std::string> fields;
    while ( pos != std::string::npos ) 
    {
        size_t next = std::min(line.find_first_of(separators, pos), std::string::npos);
        std::string field = line.substr(pos, next - pos);
        pos = std::max(next, next + 1); // next + 1 oveflows to 0 if next == std::string::npos
        if (field.empty() == false) 
        {
            fields.push_back(field);
        }
    }
    return std::move(fields);
}

struct Equation
{
    size_t result;
    std::vector<int> numbers;
};

size_t solve_part_1(const std::vector<Equation>& equations);
size_t solve_part_2(const std::vector<Equation>& equations);

int main()
{
    std::vector<Equation> equations;
    
    {
        std::cout << "Parsing input file..." << std::endl;
        std::ifstream file("input.txt", std::fstream::in);
        std::string line;
        while (!file.eof()) 
        {        
            std::getline(file, line);
            std::vector<std::string> elems = split(line, " :");
            Equation eq;
            eq.result = std::stoull(elems.at(0));
            for (auto it = std::next(elems.begin()); it != elems.end(); ++it)
                eq.numbers.push_back(std::stoul(*it));
            equations.push_back(eq);
        }
    }
    
    size_t sol_1 = solve_part_1(equations);
    std::cout << "Answer part 1: " << sol_1 << std::endl;
    size_t sol_2 = solve_part_2(equations);
    std::cout << "Answer part 2: " << sol_2 << std::endl;

    return 0;
}

inline size_t concat_numbers(size_t num_1, size_t num_2)
{
    size_t pten = 10; 
    while ( pten <= num_2 )
        pten *= 10;
    return num_1 * pten + num_2;
}

using const_it = std::vector<int>::const_iterator;

size_t composite_operation(const_it begin, const_it end, size_t op_bitfield)
{
    int len = (int)std::distance(begin, end);
    
    if (len == 0) return 0;

    size_t value = *begin;

    if (len == 1) 
    {
        //std::cout << value;
        return value;
    }

    //std::cout << value;
    for (int i = 1; i < len; ++i)
    {
        size_t op = op_bitfield & (1ull << (i-1));
        int number = *std::next(begin, i);
        //std::cout << (op ? " + " : " * ") << number;
        value = op ? value + number : value * number;
    }

    return value;
}

size_t solve_part_1(const std::vector<Equation>& equations)
{
    std::cout << "Running part 1..." << std::endl;

    size_t cumul = 0;

    int count = 0;

    print_progress_bar(0.f);

    for (const Equation& eq : equations)
    {
        int operands = eq.numbers.size() - 1;
        int bitfield = (1 << operands);
        
        while (bitfield > 0)
        {
            --bitfield;
            size_t value = composite_operation(
                eq.numbers.begin(), eq.numbers.end(), bitfield
            );

            if (value == eq.result)
            {
                cumul += value;
                break;
            }
        }

        print_progress_bar((float)(++count) / equations.size());
    }

    print_progress_bar(1.f);
    std::cout << std::endl;

    return cumul;
}


size_t solve_part_2(const std::vector<Equation>& equations)
{
    std::cout << "Running part 2..." << std::endl;

    size_t cumul = 0;

    int count = 0;

    print_progress_bar(0.f);

    for (const Equation& eq : equations)
    {
        int operands = eq.numbers.size();

        bool found_valid = false;

        //std::cout << "\nTesting " << eq.result << ':';
        //for (int n : eq.numbers)
        //    std::cout << ' ' << n << ',';
        //std::cout << "\b " << std::endl;

        for (int i = 0; i < operands; ++i)
        {
            size_t bitfield_first = std::max(1ull, (1ull << i) >> 1);
            
            while (!found_valid && bitfield_first-- > 0)
            {
                //std::cout << "P1( ";
                size_t value_1 = composite_operation(
                    eq.numbers.begin(), std::next(eq.numbers.begin(), i), bitfield_first
                );
                //std::cout << " ) ";

                if (value_1 > eq.result)
                {
                    //std::cout << value_1 << " TOO HIGH" << std::endl;
                    continue;
                }

                //std::cout << value_1 << std::endl;
                
                int bitfield_second = 1 << (operands - i);

                while (!found_valid && bitfield_second-- > 0)
                {
                    //std::cout << "P2( ";
                    size_t value_2 = composite_operation(
                        std::next(eq.numbers.begin(), i), eq.numbers.end(), bitfield_second
                    );
                    //std::cout << " ) ";

                    if (value_2 > eq.result)
                    {
                        //std::cout << value_2 << " TOO HIGH" << std::endl;
                        continue;
                    }

                    size_t res = concat_numbers(value_1, value_2);
                    
                    //std::cout << value_1 << " || " << value_2 << " = " << res << std::endl;

                    if (res == eq.result)
                    {
                        cumul += res;
                        found_valid = true;
                        break;
                    }
                }
            }

            if (found_valid)
                break;
        }
        
        print_progress_bar((float)(++count) / equations.size());
    }

    print_progress_bar(1.f);
    std::cout << std::endl;

    return cumul;
}