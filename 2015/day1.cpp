#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main(){
    ifstream f;
    string paras;
    f.open("day1input.txt");
    f >> paras;
    f.close();

    // part 1
    int res = 0;
    for(char const &c : paras){
        if (c == '('){
            res++;
        } else {
            res--;
        }
    }
    cout << res << "\n";

    // part 2
    res = 0;
    int i = 0;
    for(char const &c : paras){
        if (c == '('){
            res++;
        } else {
            res--;
        }
        i++;
        if(res < 0){
            cout << i;
            break;
        }
    }
}