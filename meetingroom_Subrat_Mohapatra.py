import itertools

#take input as a list and split into sublist

test = [7.11, 8, 9.00, 9.15, 14.30, 15.00,
        8.23, 6, 10.00, 11.00, 14.00, 15.00,
        8.43, 7, 11.30, 12.30, 17.00, 17.30,
        9.511, 9, 9.30, 10.30, 12.00, 12.15, 15.15, 16.15,
        9.527, 4, 9.00, 11.00, 14.00, 16.00,
        9.547, 8, 10.30, 11.30, 13.30, 15.30, 16.30, 17.30]

split_list = [2, 6, 8, 12, 14, 18, 20, 26, 28, 32, 34]

res = [test[i: j] for i, j in zip([0] +
                                  split_list, split_list + [None])]



# Extract the timings into a single list

li = []
count = 0
for i in range(len(split_list) + 1):
    # print(i)
    if count % 2 == 1:
        # print(str(res[i]))
        li.append(res[i])
    count += 1

brandnewarray = list(itertools.chain.from_iterable(li))

# all the timings split into start-time , End-time combination of sublist

split_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]

res2 = [brandnewarray[i: j] for i, j in zip([0] +
                                            split_list, split_list + [None])]


# Define function to calculate the exact meeting room

def canAttendMeetings(intervals):
    """
    :type intervals: List[Interval]
    :rtype: bool
    """

# define one variables for which we need to find out the available meeting room
    s = [10.30, 11.30]

#checking if the time interval does not have start and End tme
    if len(intervals) < 2:

        print("Input is not correct, kindly correct it")
    else:

#sort the time intervals
        intervals = sorted(intervals, key=lambda x: x[1])

#check which interval , we can book the meeting
        for p in intervals:

            if s[0] >= p[0]:

                if s[1] <= p[1]:

                    print("We can book this meeting room having available timeings:", p)
                    q = str(p[0])
                    res11 = [i for i in res if 'q' in i]
                    print("hence can book on the floor# , the room#, and no of people can accomodate #: ",
                          res[len(res) - 2])
            else:

                return ()


canAttendMeetings(res2)
