#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

class d4
{
private:
    vector<string> getFileInput();
    vector<int> getJobs(string line);
    int jobsOverlap(vector<int> job1, vector<int> job2);
    int containsOverlap(vector<int> job1, vector<int> job2);

public:
    int problem1();
    int problem2();
};