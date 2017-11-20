class Solution(object):
    def islandPerimeter(self, grid):
	""" 
	:type grid: List[List[int]]
	:rtype: int
	"""

	perimeter = 0 

	li = len(grid)
	lj = len(grid[0]) if li else 0

	for i in range(li):
	    for j in range(lj):
		if grid[i][j] == 0:
		    continue
		perimeter += 4
		if(i-1 >= 0): 
		    if grid[i-1][j] == 1:
			perimeter -= 1
		if(j+1 < lj): 
		    if grid[i][j+1] == 1:
			perimeter -= 1
		if(j-1 >= 0): 
		    if grid[i][j-1] == 1:
			perimeter -= 1
		if(i+1 < li): 
		    if grid[i+1][j] == 1:
			perimeter -= 1

	return perimeter

