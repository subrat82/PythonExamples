def canAttendMeetings(intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if len(intervals) < 2:
            #return True
            print("subrat2")
        else:
            print("subrat4")
            intervals = sorted(intervals, key=lambda x: x[:-1])
            print(intervals)
            for p, q in zip(intervals, intervals[1:]):
                if q[0] < p[1]:
                    print(p)
                    print(q)
                    print("We are not suppose to attend q meeting:", q)
            #return True
            print("subrat3")
            print("We can attend q meeting:", q)

#intervals = [[0, 20],[5,15], [20, 30]]
canAttendMeetings([[11, 18],[5,15],[20, 30]])
