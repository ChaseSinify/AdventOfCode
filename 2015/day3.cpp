#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <utility>
using namespace std;

pair<int, int> step(char dir, int xpos, int ypos){
    int x=0, y=0;
    if (dir == '^') {
        y++;
    } else if (dir == 'v') {
        y--;
    } else if (dir == '>') { 
        x++;
    } else if (dir == '<') {
        x--;
    }
    return make_pair(xpos + x, ypos + y);
}

int main() {
    set<pair<int, int>> points;
    string directions;
    ifstream f;
    f.open("day3input.txt");
    f >> directions;
    f.close();
    int xpos=0, ypos=0;
    int roboxpos=0, roboypos=0;
    
    // part 1
    for (char &c : directions) {
        pair<int, int> newPoint = step(c, xpos, ypos);
        xpos = newPoint.first;
        ypos = newPoint.second;
        points.insert(newPoint);
    }
    std::cout << points.size() << endl;

    // part 2
    points.clear();
    xpos=0, ypos=0;
    bool santa;
    for (char &c : directions) {
        if (santa) {
            pair<int, int> newPoint = step(c, xpos, ypos);
            xpos = newPoint.first;
            ypos = newPoint.second;
            points.insert(newPoint);
        } else {
            pair<int, int> newPoint = step(c, roboxpos, roboypos);
            roboxpos = newPoint.first;
            roboypos = newPoint.second;
            points.insert(newPoint);
        }
        santa = !santa;
    }
    std::cout << points.size();
}
