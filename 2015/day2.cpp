#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
    ifstream f;
    vector<vector<int>> lwh;
    string x;
    f.open("day2input.txt");
    while(f >> x){
        istringstream iss(x);
        string item;
        vector<int> temp;
        while(getline(iss, item, 'x')){
            temp.push_back(stoi(item));
        }
        lwh.push_back(temp);
        temp.clear();
    }
    f.close();
    int res=0;
    // part 1 loop
    // for(auto value : lwh){
    //     int lw=0, lh=0, wh=0, extra=0;
    //     lw = 2 * value[0] * value[1];
    //     lh = 2 * value[0] * value[2];
    //     wh = 2 * value[1] * value[2];
    //     extra = min({lw/2, lh/2, wh/2});
    //     res += lw + lh + wh + extra;
    // }
    // part 2 loop
    for(auto value : lwh){
        int lw=0, lh=0, wh=0, smallest=0, cubic=0;
        cubic = value[0] * value[1] * value[2];
        res += cubic;
        value.erase(max_element(value.begin(), value.end()));
        for(int v : value){
            res += 2 * v;
        }
    }
    cout << res;
}