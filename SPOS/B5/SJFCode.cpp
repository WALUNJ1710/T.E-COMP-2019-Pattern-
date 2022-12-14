#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
class process
{
public:
string name;
int bursttime, arrivaltime, turnaroundtime, waitingtime, finishtime, arrivaltimegantt;
process()
{
name = "p0";
bursttime = 0;
finishtime = 0;
waitingtime = 0;
turnaroundtime = 0;
arrivaltime = 0;
}
void set();
void sortbyjob(process *, int);
void sortbyat(process *, int);
void Null(process *, int);
friend ostream &operator<<(ostream &os, const process &p);
};
ostream &operator<<(ostream &os, const process &p)
{
os << " " << p.name << endl;
os << p.arrivaltimegantt << " ";
return os;
}
void process::set()
{
cout << "Enter the process name: ";
cin >> name;
cout << "Enter the burst time: ";
cin >> bursttime;
cout << "Enter the arrival time: ";
cin >> arrivaltime;
arrivaltimegantt = arrivaltime;
}
void process::Null(process *p, int n)
{
int i;
for (i = 0; i < n; i++)
{
p[i] = p[i + 1];
}
}
void process::sortbyat(process *p, int n)
{
std::sort(p, p + n, [](process const &a, process const &b) -> bool
{ return a.arrivaltime < b.arrivaltime; });
}
void process::sortbyjob(process *p, int n)
{
std::sort(p, p + n, [](process const &a, process const &b) -> bool
{ return a.bursttime < b.bursttime; });
}
int main()
{
process p[10], gantt[10], u;
int n, i, currenttime = 0;
cout << "Enter the number of process: ";
cin >> n;
for (i = 0; i < n; i++)
{
p[i].set();
cout << endl;
}
u.sortbyat(p, n);
gantt[0] = p[0];
currenttime = p[0].bursttime;
gantt[0].finishtime = currenttime;
gantt[0].turnaroundtime = gantt[0].finishtime - gantt[0].arrivaltime;
gantt[0].waitingtime = gantt[0].turnaroundtime - gantt[0].bursttime;
p[0].Null(p, n);
for (i = 1; i < n; i++)
{
u.sortbyjob(p, n);
gantt[i] = p[i];
currenttime += p[i].bursttime;
gantt[i].finishtime = currenttime;
gantt[i].arrivaltimegantt = gantt[i - 1].finishtime;
gantt[i].turnaroundtime = gantt[i].finishtime - gantt[i].arrivaltime;
gantt[i].waitingtime = gantt[i].turnaroundtime - gantt[i].bursttime;
p[i].Null(p, n);
}
cout << "\n********* Gantt Chart *********";
cout << "\n|";
for (i = 0; i < n; i++)
{
cout << " " << gantt[i].name << "\t|";
}
cout << "\n";
cout << gantt[0].arrivaltimegantt;
for (i = 0; i < n; i++)
{
cout << "\t" << gantt[i].finishtime;
}
cout << "\n";
// turnaround time
int tsum = 0, wsum = 0;
cout << "*\n******** Turnaround time *********" << endl;
cout << "Process | Turnaround Time" << endl;
for (i = 0; i < n; i++)
{
cout << " " << gantt[i].name << " | " << gantt[i].turnaroundtime << endl;
tsum += gantt[i].turnaroundtime;
}
// waiting time
cout << "\n********* Wating time *********" << endl;
cout << "Process | Waiting Time" << endl;
for (i = 0; i < n; i++)
{
cout << " " << gantt[i].name << " | " << gantt[i].waitingtime << endl;
wsum += gantt[i].waitingtime;
}
float tavg, wavg;
tavg = float(tsum / n);
wavg = float(wsum / n);
cout << "\n";
cout << "Average Turnaround time: " << tavg << endl;
cout << "Average waiting time: " << wavg << endl;
}
