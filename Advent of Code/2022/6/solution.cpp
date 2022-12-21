#include <iostream>
#include <string>

std::string print_buffer(char buffer[], std::size_t len, int init) {
    std::string s;
    for (int i = 0; i < len; ++i) {
        s += buffer[(i+init)%len];
    }
    return s;
}

bool check_uniques(char buffer[], std::size_t len) {
    for (int i = 0; i < len - 1; ++i) {
        for (int j = i+1; j < len; ++j) {
            if (buffer[j] == ' ' || buffer[i] == buffer[j]) {
                return false;
            }
        }
    }
    return true;
}

void init_buffer(char buffer[], std::size_t len, char c) {
    for (int i = 0; i < len; ++i) {
        buffer[i] = c;
    }
}

int main(int argc, char *argv[]) {

    char buffer_start[14];
    init_buffer(buffer_start, 14, ' ');
    char buffer_end[4];
    init_buffer(buffer_end, 4, ' ');

    int index_buffer_start = 0;
    int index_buffer_end = 0;

    int total_length = 0;

    int length_start = 0;
    int length_end = 0;

    bool start_found = false;
    bool end_found = false;

    while (char c = std::getchar()) {

        total_length += 1;
        // std::cout << "Received " << c << " (" << total_length << "/4096)" << std::endl;

        if (!start_found) {
            buffer_start[index_buffer_start] = c;
            index_buffer_start = (index_buffer_start + 1) % 14;
            if (check_uniques(buffer_start, 14)) {
                start_found = true;
                length_start = total_length;
            }
            // std::cout << "Start buffer: " << print_buffer(buffer_start, 14, index_buffer_start) << std::endl;
        }

        if (!end_found) {
            buffer_end[index_buffer_end] = c;
            index_buffer_end = (index_buffer_end + 1) % 4;
            if (check_uniques(buffer_end, 4)) {
                end_found = true;
                length_end = total_length;
            }
            // std::cout << "End buffer: " << print_buffer(buffer_end, 4, index_buffer_end) << std::endl;
        }

        if (start_found && end_found) {
            break;
        }
    }

    std::cout << "Answer part 1: " << length_end << std::endl;
    std::cout << "Answer part 2: " << length_start << std::endl;

    return 0;
}