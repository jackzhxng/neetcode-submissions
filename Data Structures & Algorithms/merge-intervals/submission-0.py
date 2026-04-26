class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Time taken: 5 min
        """
        intervals.sort()
        curr_interval = None
        res = []
        for interval in intervals:
            if curr_interval is None:
                curr_interval = interval
                continue
            if curr_interval[1] >= interval[0]:
                curr_interval[1] = max(interval[1], curr_interval[1])
            else:
                res.append(curr_interval)
                curr_interval = interval
        if curr_interval:
            res.append(curr_interval)
        return res
                