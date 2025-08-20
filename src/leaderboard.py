import time
import operator
import file
import datetime

class Leaderboard():
    def __init__(self, leaderboard=False):
        self.leaderboard = leaderboard
        if leaderboard == False:
            self.leaderboard = file.load_json('leaderboard.json')
        self.leaderboard.sort(key=operator.itemgetter('score', 'time'), reverse = True)
        self.length = len(self.leaderboard)

    def update_leaderboard(self, score, initials, state):
        slurs = ["FAG", "NIG", "KKK", "JEW", "JAP", "WOP", "FGT"]
        if initials not in slurs:
            self.leaderboard.append({'name':initials,'score':score,'time':int(time.time()),'state':state})
            self.leaderboard.sort(key=operator.itemgetter('score', 'time'), reverse = True)
            self.length = len(self.leaderboard)
            file.save_json(self.leaderboard,'leaderboard.json')

    def get_daily_leaderboard(self):
        return [x for x in self.leaderboard if(datetime.datetime.fromtimestamp(x['time']).date() == datetime.datetime.now().date())]
        
    def get_position(self, position):
        #returns item at position on leaderboard, accouting for offset of arrays starting at 0
        if self.length > position and position >= 0:
            return self.leaderboard[position]
        return False
    