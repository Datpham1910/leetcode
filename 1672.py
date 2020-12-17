class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum=0 
        for i in range (len(accounts)):
            sum_account = sum(accounts[i])
            if max_sum < sum_account:
                max_sum= sum_account
        return max_sum   
                