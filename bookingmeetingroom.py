import time

class RoomDetails:
  def __init__(self, floor, number, capacity, availability):
    self.floor = floor
    self.number = int(number)
    self.capacity = int(capacity)
    self.availability = availability



rooms = []
file = open("rooms.txt","r")
for line in file:
	line = line.rstrip()
	roomValues = line.split(",")
	roomsAvailabilities = roomValues[2:]
	i = 0
	roomsAvailabilitiesSets=[]
	while i < len(roomsAvailabilities):
		roomsAvailabilitiesSets.append( [time.strptime(roomsAvailabilities[i],'%H:%M'), time.strptime(roomsAvailabilities[i+1],'%H:%M')])
		i = i+2
	room = RoomDetails(roomValues[0].split(".")[0], roomValues[0].split(".")[1],roomValues[1],roomsAvailabilitiesSets)
	rooms.append(room)

def getAvailability(floor,numberOfPeople,startTime,endTime):
	matchedRooms = []
	startTime = time.strptime(startTime,'%H:%M')
	endTime = time.strptime(endTime,'%H:%M')
	for eachRoom in rooms:
		if eachRoom.capacity >= numberOfPeople:
			for eachRoomAvailability in eachRoom.availability:
				if startTime >=  eachRoomAvailability[0]and endTime <= eachRoomAvailability[1]:
					matchedRooms.append ([int(eachRoom.floor), eachRoom.number])
	return getBestAvailability (matchedRooms, floor)

def getBestAvailability(matchedRooms, floor):
	matchedDiff = []
	for matchedRoom in matchedRooms:
		matchedDiff.append({"diff" : matchedRoom[0] - floor, "fn":str(matchedRoom[0]) +"."+ str(matchedRoom[1])})
	for matchedDif in matchedDiff:
		if matchedDiff[0]["diff"] == matchedDif["diff"]:
			return matchedDif["fn"]


print(getAvailability(5,8,"10:30","11:30"))
