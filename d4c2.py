import operator
from collections import defaultdict

BEGIN = 0
SLEEP = 1
WAKE  = 2

YEAR = 10
MONTH = 11
DAY = 12
HOUR = 13
MINUTE = 14
GUARD = 15
WAKES = 16
START = 17

events = []

class event:
    def __init__(self, year, month, day, hour, minute, guard, wakes, start=False):
        self.year  = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.guard = guard
        self.wakes = wakes
        self.start = start

    def __getitem__(self,index):
    	if index == YEAR:
    		return self.year
    	if index == MONTH:
    		return self.month 
    	if index == DAY:
    		return self.day
    	if index == HOUR:
    		return self.hour
    	if index == MINUTE:
    		return self.minute
    	if index == GUARD:
    		return self.guard
    	if index == WAKES:
    		return self.wakes
    	if index == START:
    		return self.start
		
def shift_start(guard):
	return event(0, 0, 0, 0, 0, guard, False, True)

def print_event(self):
	txt = 'At ' + str(self.hour) + ':' + str(self.minute)
	txt += ' of day ' + str(self.day) + '/' + str(self.month) + '/' + str(self.year)
	txt += ' guard ' + str(self.guard)
	
	txt += ' starts his shift.' if self.start else ' wakes up.' if self.wakes else ' falls asleep.'
	print(txt)

def parse_line(line):
	date, text = line.split(']')
	date = date[1:]
	date, hour = date.split(' ')
	year, month, day = date.split('-')
	hour, minute = hour.split(':')
	text = text.strip()
	if text.find('#') != -1:
		_, guard = text.split('#')
		guard, _, _ = guard.split(' ')
		events.append(event(int(year), int(month), int(day), int(hour), int(minute), int(guard), False, True))
	else:
		wakes = text == 'wakes up'
		events.append(event(int(year), int(month), int(day), int(hour), int(minute), int(0), wakes))
	
def get_moment(event):
	moment = event.year*12*30*24*60
	moment += event.month*30*24*60
	moment += event.day*24*60
	moment += event.hour*60
	moment += event.minute 
	return moment

def argmax(d):
    best = None
    for k,v in d.items():
        if best is None or v > d[best]:
            best = k
    return best

with open("input", "r") as f:
	data = f.readlines()
	for line in data:
		parse_line(line)

last_guard = None
last_sleep = None
guards = defaultdict(int)
minutes = defaultdict(int)

events.sort(key = operator.itemgetter(YEAR, MONTH, DAY, HOUR, MINUTE))

for event in events:
	if event.start:
		last_guard = event.guard
		last_sleep = None
	elif not event.wakes:
		last_sleep = event.minute
	else:
		for m in range(last_sleep, event.minute):
			minutes[(last_guard, m)] += 1
			guards[last_guard] += 1

sleepy_guard, sleepy_minute = argmax(minutes)
print(sleepy_guard)
print(sleepy_minute)
print(sleepy_guard * sleepy_minute)


				