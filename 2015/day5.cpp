#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <utility>
using namespace std;
int main() {
    ifstream f;
    vector<string> strings;
    string line;
    f.open("day5input.txt");
    vector<char> vowels = {'a', 'e', 'i', 'o', 'u'};
    vector<string> bad = {"ab", "cd", "pq", "xy"};
    bool ok = true;
    bool adjacent = false;
    int vowel = 0;
    char last = 0;
    int good = 0;
    while (f >> line) {
        for (string p : bad) {
            if(line.find(p) != line.npos) {
                ok = false;
                break;
            }
        }
        if (ok) {
            for(char &c : line){
                if (last && !adjacent && c == last) {
                    adjacent = true;
                } 
                vector<char>::iterator it = find(vowels.begin(), vowels.end(), c);
                if (it != vowels.end()) {
                    vowel++;
                }
                last = c;
            }
            if (adjacent && vowel >= 3) {
                good++;
            }
            ok = true;
            adjacent = false;
            vowel = 0;
            last = 0;
        } else {
            ok = true;
            continue;
        }
    }
    cout << good;
}