class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)

        dpA = [0] * n
        dpB = [0] * n

        dpA[0] = energyDrinkA[0]
        dpB[0] = energyDrinkB[0]

        for i in range(1, n):
            dpA[i] = max(dpA[i-1], dpB[i-2]) + energyDrinkA[i]
            dpB[i] = max(dpB[i-1], dpA[i-2]) + energyDrinkB[i]

        return max(dpA[-1], dpB[-1])