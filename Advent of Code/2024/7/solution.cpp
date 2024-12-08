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
    std::vector<size_t> numbers;
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
        while (!file.eof()) {        
            std::getline(file, line);
            std::vector<std::string> elems = split(line, " :");
            Equation eq;
            eq.result = std::stoull(elems.at(0));
            for (auto it = std::next(elems.begin()); it != elems.end(); ++it)
                eq.numbers.push_back(std::stoull(*it));
            equations.push_back(eq);
        }
    }
    
    size_t sol_1 = solve_part_1(equations);
    std::cout << "Answer part 1: " << sol_1 << std::endl;
    size_t sol_2 = solve_part_2(equations);
    std::cout << "Answer part 2: " << sol_2 << std::endl;

    return 0;
}

enum Operation
{
    ADD, MULT, PIPE
};

bool cycle_operations_rec(std::vector<int>& ops, const Operation max_op, const int i)
{
    if (i == ops.size())
        return false;

    if (ops[i] < max_op) 
    {
        ++ops[i];
        return true;
    }

    ops[i] = Operation::ADD;
    return cycle_operations_rec(ops, max_op, i + 1);
}

inline bool cycle_operations(std::vector<int>& ops, const Operation max_op)
{
    return cycle_operations_rec(ops, max_op, 0);
}

inline size_t concat_numbers(size_t num_1, size_t num_2)
{
    size_t pten = 10; 
    while ( pten <= num_2 )
        pten *= 10;
    return num_1 * pten + num_2;
}

size_t composite_operation(const std::vector<size_t>& nums, const std::vector<int> ops)
{
    size_t value = nums[0];
    for (int i = 1, len = nums.size(); i < len; ++i)
    {
        int number = nums[i];
        switch (ops[i - 1])
        {
        case ADD:
            //std::cout << " + " << number;
            value += number;
            break;            
        case MULT:
            //std::cout << " * " << number;
            value *= number;
            break;
        case PIPE:
            //std::cout << " | " << number;
            value = concat_numbers(value, number);
            break;
        }
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
        std::vector<int> op_combo(eq.numbers.size() - 1, Operation::ADD);

        while (true)
        {
            size_t value = composite_operation(eq.numbers, op_combo);

            if (value == eq.result)
            {
                cumul += value;
                break;
            }

            if (cycle_operations(op_combo, Operation::MULT) == false)
            {
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
        std::vector<int> op_combo(eq.numbers.size() - 1, Operation::ADD);

        while (true)
        {
            size_t value = composite_operation(eq.numbers, op_combo);

            if (value == eq.result)
            {
                cumul += value;
                break;
            }

            if (cycle_operations(op_combo, Operation::PIPE) == false)
            {
                break;
            }
        }

        print_progress_bar((float)(++count) / equations.size());
    }

    print_progress_bar(1.f);
    std::cout << std::endl;

    return cumul;
}