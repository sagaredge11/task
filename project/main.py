# Appartment hunting

def distance(block1, block2):
    return abs(block1 - block2)


def find_final_block(blocks, required):
    min_distance = float('inf')
    final_block = None
    for i in range(len(blocks)):
        distances = []
        for requirement in required:
            required_distances = [distance(i, j) for j in range(len(blocks)) if blocks[j][requirement]]
            if required_distances:
                distances.append(min(required_distances))
        if distances and max(distances) < min_distance:
            min_distance = max(distances)
            final_block = i
    return final_block


blocks = [
    {
        "gym": False,
        "school": True,
        "store": False,
    },
    {
        "gym": True,
        "school": False,
        "store": False,
    },
    {
        "gym": True,
        "school": True,
        "store": False,
    },
    {
        "gym": False,
        "school": True,
        "store": False,
    },
    {
        "gym": False,
        "school": True,
        "store": True,
    },
]

required = ['gym', 'school', 'store']

final_block = find_final_block(blocks, required)
print(final_block)

# Calender Matching
def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    # Convert the input times from strings to minutes
    def timeToMinutes(time):
        hours, minutes = map(int, time.split(':'))
        return hours * 60 + minutes

    # Convert the input minutes to time strings
    def minutesToTime(minutes):
        hours = minutes // 60
        minutes = minutes % 60
        return '{:02d}:{:02d}'.format(hours, minutes)

    # Find the available time blocks for a calendar and daily bounds
    def getAvailability(calendar, dailyBounds):
        availability = []
        startOfDay = timeToMinutes(dailyBounds[0])
        endOfDay = timeToMinutes(dailyBounds[1])
        for i in range(len(calendar)):
            currentEnd = timeToMinutes(calendar[i][0])
            if i == 0 and currentEnd != startOfDay:
                availability.append([startOfDay, currentEnd])
            if i > 0:
                previousEnd = timeToMinutes(calendar[i - 1][1])
                if currentEnd != previousEnd:
                    availability.append([previousEnd, currentEnd])
            if i == len(calendar) - 1 and timeToMinutes(calendar[i][1]) != endOfDay:
                availability.append([timeToMinutes(calendar[i][1]), endOfDay])
        return availability

    # Convert the input calendars to availability lists
    availability1 = getAvailability(calendar1, dailyBounds1)
    availability2 = getAvailability(calendar2, dailyBounds2)

    # Find the available time blocks for the meeting
    meetingAvailability = []
    for i in range(len(availability1)):
        for j in range(len(availability2)):
            start = max(availability1[i][0], availability2[j][0])
            end = min(availability1[i][1], availability2[j][1])
            if end - start >= meetingDuration:
                meetingAvailability.append([start, end])

    # Convert the output availability to time strings
    meetingAvailability = [[minutesToTime(start), minutesToTime(end)] for start, end in meetingAvailability]

    return meetingAvailability


calendar1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
dailyBounds1 = ['9:00', '20:00']
calendar2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
dailyBounds2 = ['10:00', '18:30']
meetingDuration = 30

print(calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration))
