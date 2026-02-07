#include <iostream>
#include <string>
using namespace std;

class Robot {
private:
    string name;
    
public:
    Robot(string robot_one) {
    name = robot_one;  
}

    void say_hello() {
        cout << "Hello, I am " << name << ", I am ready for battle!" << endl;
    }
};

int main() {
    Robot warrior_one{"cssgblaster"};
    
    warrior_one.say_hello();
    
    return 0;
}