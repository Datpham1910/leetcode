def minCostToMoveChips(self, position: List[int]) -> int:
	pos = [0, 0]  # even, odd counts
	for p in position:
		pos[p & 1] += 1
	return min(pos)