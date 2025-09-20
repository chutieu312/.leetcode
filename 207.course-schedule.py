#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

from collections import deque
from typing import List

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
            graph = [[] for _ in range(numCourses)]             # adjacency: u -> [v...]
            in_degree = [0] * numCourses                        # number of prereqs per course

            for a, b in prerequisites:                          # edge b -> a (b before a)
                graph[b].append(a)                              # b points to a
                in_degree[a] += 1                               # a needs one more prereq

            q = deque([c for c in range(numCourses) if in_degree[c] == 0])  # ready courses
            taken = 0                                           # how many we've scheduled

            while q:                                            # process all ready courses
                u = q.popleft()                                 # take course u
                taken += 1
                for v in graph[u]:                              # unlock neighbors v
                    in_degree[v] -= 1                           # we've satisfied one prereq of v
                    if in_degree[v] == 0:                       # v becomes ready
                        q.append(v)

            return taken == numCourses                          # all taken → feasible; else cycle
        
# @lc code=end

