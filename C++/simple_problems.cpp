#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    int total = 0;
    int temp;
    for (int i=0;i<n;i++) {
        cin >> temp;
        if (temp < 0)
            total++;
    }
}