#include <iostream>
using namespace std;

class Dog {
    private:
    int age;
    string name;

    public:
    Dog(string name, int age) {
        this->name = name;
        this->age = age;
    }

    string toString() {
        return name + " is " + to_string(age) + " years old.\n";
    }
};

int main() {
    Dog fido("Fido", 4);
    cout << fido.toString();

    
}