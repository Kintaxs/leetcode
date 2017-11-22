class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        count = 0

        len_points = len(points)

        d = dict()

        for i in range(len_points - 1):
            for j in range(i+1, len_points):
                distance = self.getDis(points[i], points[j])

                if(d.has_key(distance)):
                    d[distance] += 1
                else:
                    d[distance] = 1

        for k in d:
            if d[k] >= 2:
                count += 2 * d[k]
        
        return count

    def getDis(self, li, lj):

        return ((li[0]-lj[0])**2 + (li[1]-lj[1])**2) ** 0.5

