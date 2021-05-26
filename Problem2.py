"""
Sample Input
[[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]
Sample Output (Read the disks from left to right)
[[4, 4, 5], [3, 2, 3], [2, 1, 2]]

"""
"""
Sample Input
[[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]
Sample Output (Read the disks from left to right)
[[4, 4, 5], [3, 2, 3], [2, 1, 2]]

"""


class Solution(object):

    def pileUpCuboids(self, cuboids, cuboid):  # Find a box smaller than the current box and put it on it
        if len(cuboids) == 1:  # just left one cuboid
            if cuboids[0][2] < cuboid[2] and cuboids[0][1] < cuboid[1] and cuboids[0][0] < cuboid[0]:
                return cuboids  # return it
            else:
                return None  # Nothing smaller than the current one
        else:
            maxHeight = 0
            cuboidList = []  # results
            i = 0
            while i < len(cuboids):  # try all the boxes

                # print(cuboids, cuboid)
                if cuboids[i][2] < cuboid[2] and cuboids[i][1] < cuboid[1] and cuboids[i][0] < cuboid[0]:  # Smaller than the current box
                    curList = []  #
                    height = cuboids[i][2]
                    thiscuboid = cuboids[i]
                    thiscuboids = cuboids.copy()
                    thiscuboids.pop(i)
                    # print("success", thiscuboid)
                    result = self.pileUpCuboids(thiscuboids, thiscuboid)
                    if result is not None:
                        curList.append(thiscuboid)
                        curList += result
                    else:
                        curList.append(thiscuboid)
                    for x in curList:
                        # print("222,", curList)
                        height += x[2]
                    if height > maxHeight:
                        maxHeight = height
                        cuboidList = curList

                i += 1
            if len(cuboidList) == 0:
                return None
            else:
                # print("111,", cuboidList)
                return cuboidList


    def maxHeight(self, cuboids:list):
        """
        :type cuboids: List[List[int]]
        :rtype: int
        """
        if len(cuboids) > 1:
            maxHeight = 0
            maxList = []
            for c in range(0, len(cuboids)):  # Put the current box at the bottom
                cuboidList = cuboids.copy()
                cuboid = cuboids[c]
                cuboidList.pop(c)
                result = self.pileUpCuboids(cuboidList, cuboid)

                if result is None:
                    if maxHeight < cuboids[c][2]:
                        maxList.append(cuboid)
                        maxHeight = cuboids[c][2]

                else:
                    height = cuboids[c][2]
                    # print("res is ", result)
                    for x in result:

                        height += x[2]
                    if height > maxHeight:
                        maxHeight = height
                        # result.append(cuboids[c])
                        maxList = result
                        maxList.insert(0, cuboid)
                    elif height > maxHeight:
                        self.anothermethod += result

            return maxList

        else:
            return cuboids[0]

    def output(self, maxlist):
        print("Sample Output (Read the disks from left to right)")
        astr = ''
        for alist in maxlist:
            astr += str(alist) + ","
        print("[", astr[:-1], "]")

    def input(self, cuboids):
        self.output(self.maxHeight(cuboids))

s = Solution()

cuboids = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]
Height = s.input(cuboids)
# print(s.maxHeight(cuboids))
#
# cuboids = [[1,1,1],[2,2,2],[3,3,3]]
# Height = s.input(cuboids)
#
#
# cuboids = [[1,1,1],[2,2,2],[3,3,2]]
# Height = s.input(cuboids)
