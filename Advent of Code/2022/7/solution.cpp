#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <memory>
#include <algorithm>

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

class File {
private:
    std::string m_name;
    int m_size;

public:
    File(std::string name, int size)
        : m_name(name), m_size(size) {
    }

    std::string name() { return m_name; }

    int size() { return m_size; }

    void print(int ind) {
        std::cout << indent(ind) << m_name << " (" << m_size << " B)" << std::endl; 
    }
};

class Folder {
private:
    std::string m_name;
    Folder *m_parent;
    std::unordered_map<std::string, std::shared_ptr<Folder>> m_child_folders;
    std::unordered_map<std::string, std::shared_ptr<File>> m_child_files;

public:
    Folder(Folder *parent, std::string name)
        : m_parent(parent), m_name(name) {
    }

    std::string name() { return m_name; }

    void add_folder(std::string name) {
        m_child_folders.insert(std::make_pair(name, std::make_shared<Folder>(this, name)));
    }
    
    void add_file(std::string name, int size) {
        m_child_files.insert(std::make_pair(name, std::make_shared<File>(name, size)));
    }

    std::shared_ptr<Folder> enter(std::string name) {
        return m_child_folders.at(name);
    }

    Folder* up() {
        return m_parent;
    }

    void print(int ind) {
        std::cout << indent(ind) << m_name << " (dir):" << std::endl;
        for (auto file = m_child_files.begin(); file != m_child_files.end(); ++file) {
            file->second->print(ind+1);
        }
        for (auto folder = m_child_folders.begin(); folder != m_child_folders.end(); ++folder) {
            folder->second->print(ind+1);
        }
    }

    int get_size(std::vector<int> &container) {
        int size = 0;
        for (auto file : m_child_files) {
            size += file.second->size();
        }
        for (auto folder : m_child_folders) {
            size += folder.second->get_size(container);
        }
        container.push_back(size);
        return size;
    }
};

std::vector<int> compute_recursive_folder_sizes(Folder *root) {
    std::vector<int> sizes;

    root->get_size(sizes);

    return sizes;
}


int main(int argc, char *argv[]) {

    // Building file system

    Folder root(nullptr, "/");

    Folder *current = &root;

    std::string line;
    while (std::getline(std::cin, line)) {
        std::vector<std::string> tokens = split(line, " ");
        if (tokens[0] == "$") {
            if (tokens[1] == "cd") {
                if (tokens[2] == "..") {
                    current = current->up();
                }
                else if (tokens[2] == "/") {
                    current = &root;
                }
                else {
                    current = current->enter(tokens[2]).get();
                }
            } else if (tokens[1] == "ls") {
                continue;
            }
        }
        else if (tokens[0] == "dir") {
            current->add_folder(tokens[1]);
        }
        else {
            // tokens[0] is a number
            current->add_file(tokens[1], std::stoi(tokens[0]));
        }
    }

    // analyzing the file system

    // root.print(0);

    std::vector<int> sizes = compute_recursive_folder_sizes(&root);

    std::sort(sizes.begin(), sizes.end());

    int total_size = sizes.back();

    int required_space = 30000000 - (70000000 - total_size);
    int space_to_be_deleted = 0;
    long total_size_under_100k = 0;

    for (auto it = sizes.begin(); it != sizes.end(); ++it) {
        if (*it <= 100000) {
            total_size_under_100k += *it;
        }
        else {
            break;
        }
    }

    for (auto it = sizes.begin(); it != sizes.end(); ++it) {
        if (*it > required_space) {
            space_to_be_deleted = *it;
            break;
        }
    }

    std::cout << "Answer part 1: " << total_size_under_100k << std::endl;
    std::cout << "Answer part 2: " << space_to_be_deleted << std::endl;

    return 0;
}