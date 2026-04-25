from collections import Counter, deque, namedtuple
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Time: 25 minutes

        Got working solution for O(nlogn) but not the most optimal, didn't get greedy. Don't think I'd be able to get greedy during an interview.
        """
        Item = namedtuple('Item', ['task', 'freq', 'time_used'])

        freqs = Counter(tasks)
        max_heap = [(freq, task) for task, freq in freqs.items()]
        queue = deque()
        heapq.heapify_max(max_heap)
        idles = 0
        i = 0
        while max_heap or queue:        
            if max_heap:
                curr_freq, curr = heapq.heappop_max(max_heap)
                curr_freq -= 1
                if curr_freq > 0:
                    queue.append(Item(curr, curr_freq, i))
            else:
                idles += 1
            while queue and i - queue[0].time_used >= n:
                task, freq, _ = queue.popleft()
                heapq.heappush_max(max_heap, (freq, task))
            i += 1
        return idles + len(tasks)
                