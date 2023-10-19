from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque([(p, i) for i, p in enumerate(priorities)])

     while queue:
       current = queue.popleft()
       if any(current[0] < item[0] for item in queue):
         queue.append(current)
         else:
             answer += 1
             if current[1] == location:
                 break
     return answer

if __name__ == "__main__":
   priorities = [2, 1, 3, 2]
   location = 2
   result = solution(priorities, location)
   print(result)