#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

ifstream fin;
ofstream fout;

vector<vector<string> > name_list;
vector<vector<string> > event_list;

string toString(int cnt) {
	string ret = "";
	do {
		char c = (cnt % 10) + '0';
		ret = c + ret;
		cnt /= 10;
	} while (cnt);
	return ret;
}

void readName() {
	ifstream fin;
	fin.open("name.txt");
	string str;
	name_list.clear();
	event_list.clear();
	while(getline(fin, str)) {
		string name = "";
		vector<string> full_name;
		full_name.clear();
		for (int i = 0; i < str.length(); i++) {
			if (str[i] == ' ') {
				full_name.push_back(name);
				name = "";
			} else {
				name += str[i];
			}
		}
		name_list.push_back(full_name);
	}
	fin.close();
}

void readEvent() {
	ifstream fin;
	string str;
	fin.open("Timeline.txt");
	string year = "";
	int cnt = 0;
	while(getline(fin, str)) {
		if (str == ";") {
			getline(fin, str);
			year = str;
			cnt = 0;
			continue;
		}
		vector<string> full_event;
		full_event.clear();
		full_event.push_back(year + '.' + toString(cnt));
		full_event.push_back(str);
		event_list.push_back(full_event);
		cnt++;
	}
	fin.close();
}

bool check(const vector<string> & name, const string & str) {
	for (int i = 0; i < name.size(); i++) {
		if (str.find(name[i]) != -1)
			return true;
	}
	return false;
}

int main() {
	readName();
	readEvent();
	fout.open("evets.json");
	fout << "[\n";
	for (int i = 0; i < name_list.size(); i++) {
		if (i) fout << ",";
		fout << "{";
		fout << "\"name\":\"";
		for (int j = 0; j < name_list[i].size(); j++) {
			cout << name_list[i][j] << " ";
			fout << name_list[i][j] << " ";
		}
		cout << endl;
		fout << "\",";
		fout << "\"events\":[";
		int cnt = 0;
		for (int ei = 0; ei < event_list.size(); ei++) {
			if (check(name_list[i], event_list[ei][1])) {
				if (cnt++) fout << ",";
				fout << "{\"date\":\"" << event_list[ei][0] << "\",";
				fout << "\"event\":\"" << event_list[ei][1] << "\"}";
			}
		}
		fout << "]";
		fout << "}\n";
	}
	fout << "]\n";
	fout.close();
	return 0;
}
