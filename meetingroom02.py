def canAttendMeetings(intervals):
    """
    :type intervals: List[Interval]
    :rtype: bool
    """
    if len(intervals) < 2:
        # return True
        print("subrat2")
    else:
        print("subrat4")
        intervals = sorted(intervals, key=lambda x: x[1])
        print(intervals)
        for p, q in zip(intervals, intervals[1:]):
            print("subrat6")
            print(p[1])
            print(q[0])
            if q[0] < p[1]:
                print(p)
                print(q)
                print("We are not suppose to attend q meeting:", q)
            else:
                print("We can attend q meeting:", q)

        # return True
        #print("subrat3")
        #print("We can attend q meeting:", q)


canAttendMeetings([[9.00, 9.15], [14.30, 15.00], [10.00, 11.00]])
