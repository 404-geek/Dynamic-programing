import heapq


def mostBooked(n, meetings):
    meetings.sort()
    free_rooms = list(range(n))
    heapq.heapify(free_rooms)
    ongoing = []  # (end_time, room_id)
    count = [0]*n

    for start, end in meetings:
        # free rooms whose meetings ended before start
        while ongoing and ongoing[0][0] <= start:
            _, room = heapq.heappop(ongoing)
            heapq.heappush(free_rooms, room)

        duration = end - start

        if not free_rooms:
            end_time, room = heapq.heappop(ongoing)
            start = end_time
            end = start + duration
            heapq.heappush(free_rooms, room)

        room = heapq.heappop(free_rooms)
        count[room] += 1
        heapq.heappush(ongoing, (end, room))

    return count.index(max(count))

print(mostBooked(3, [[1,20],[2,10],[3,5],[4,9],[6,8]]))