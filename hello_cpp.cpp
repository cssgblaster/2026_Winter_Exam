#include <iostream>
#include <string>
using namespace std;

void say_hello(string name);

int main() {
    string name = "cssgblaster";

    say_hello(name);
    
    return 0;
}

void say_hello(string name) {
    std::cout << "Hello, I am " << name << ", I am ready for battle!" << endl;
}