class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Time taken: 25 min

        position =           [10, 8,  0,  5, 3]
        speed =              [2,  4,  1,  1, 3]
        time to target =     [1,  1,  12, 7, 3]

        For two cars A and B, with A ahead of B, if we know B takes less time to
        finish than A in a vacuum, then we know B will catch up to A at some point. aka a fleet leader will always be the a slow car that is ahead of faster cars that are behind.
        """
        time_to_target = []
        sorted_pos_and_speed = sorted(zip(position, speed), reverse=True)
        for pos, speed in sorted_pos_and_speed:
            time_to_target.append((target - pos) / speed)

        next_i = 0
        fleets = 0
        fleet_leader_time = 0
        for time in time_to_target:
            if time > fleet_leader_time:
                fleets += 1
                fleet_leader_time = time
                # The fleet is finished, and a new slower car that can't catch up with this fleet becomes the leader of a new fleet
        return fleets
