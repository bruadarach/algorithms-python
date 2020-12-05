'''
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.
It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.


Example 1:

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

Example 2:

Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".

Example 3:

Input: paths = [["A","Z"]]
Output: "Z"
 

Constraints:

1 <= paths.length <= 100
paths[i].length == 2
1 <= cityAi.length, cityBi.length <= 10
cityAi != cityBi
All strings consist of lowercase and uppercase English letters and the space character
'''


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        result = []
        for i in paths:
            for j in i:
                result.append(j)
        result = result[2:]

        final = [paths[0][0], paths[0][1]]
        keep = paths[0][1]

        while True:
            if keep in result:
                idx = result.index(keep)

                if len(result) > 2:
                    if idx % 2 == 0:
                        keep = result[idx+1]
                        final.append(result[idx])
                        final.append(result[idx+1])
                        result.pop(idx)
                        result.pop(idx)
                else:
                    final.append(result[idx])
                    final.append(result[idx+1])
                    break
            else:
                break
        return final[-1]

# (runtime / memory)
#  48 ms / 14.2 MB

# My code is better in the example of 
# paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"],["Seoul","Tokyo"]]



'''
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts = [x[0] for x in paths]
        destinations = [x[1] for x in paths]

        for destination in destinations:
            if destination not in starts:
                return destination
'''
# (runtime / memory)
#  56 ms / 14.3 MB
