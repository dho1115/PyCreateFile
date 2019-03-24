

import json;

class basketball:
    def __init__(self, name, ppg, reb, asst, stl):
        self.name = name;
        self.ppg = float(ppg);
        self.rebounds = float(reb);
        self.assists = float(asst);
        self.steals = float(stl);

    def stats(self):
        obj = {};
        obj[self.name] = {};
        obj[self.name]["PPG"] = self.ppg;
        obj[self.name]["rebounds"] = self.rebounds;
        obj[self.name]["assists"] = self.assists;
        obj[self.name]["steals"] = self.steals;

        return obj;

sportStatsWrite = open("SportStats.html","w");
sportStatsAppend = open("SportStats.html","a");

RussellWestbrook = basketball("Kevin Durant", 27.9, 9.3, 3.5, 1.7);
print(RussellWestbrook.stats());

JamesHarden = basketball("James Harden", 31.0, 7.5, 6.3, 1.5);
print(JamesHarden.stats());

KarlAnthonyTowns = basketball("Karl Anthony Towns", 21.9, 11.0, 2.9, 2.7);
print(KarlAnthonyTowns.stats());

parseRusselWestbrook = json.dumps(RussellWestbrook.stats());
parseJamesHarden = json.dumps(JamesHarden.stats());
parseKAT = json.dumps(KarlAnthonyTowns.stats());

sportStatsWrite.write("<h3>" + parseRusselWestbrook + "</h3>");
sportStatsAppend.write("<h3>" + parseJamesHarden + "</h3>");
sportStatsAppend.write("<h3>" + parseKAT + "</h3>");








