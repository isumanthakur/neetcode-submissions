class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        rotations =0
        while queue and rotations < len(queue):
            if queue[0] == sandwiches[0]:
                queue.popleft()
                sandwiches.pop(0)
                rotations = 0
            else:
                queue.append(queue.popleft())
                rotations+=1
        return len(queue)
            
         