"""
721. Accounts Merge
Medium

Given a list accounts, each element accounts[i] is a list of strings, 
where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. 
Two accounts definitely belong to the same person if there is some email that is common to both accounts. 
Note that even if two accounts have the same name, they may belong to different people as people could have the same name. 
A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, 
and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input: 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation: 
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Note:

The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].
"""
from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dic = {} # for Union Find
        email2name = {}
		# classic funcion for Union Find
        def find(x):
            if x != dic.setdefault(x, x):
                dic[x] = find(dic[x])
            return dic[x]
		# build Union Find tree
        for it in accounts:
            email2name[it[1]] = it[0] # link first email with name
            root = find(it[1]) # this line is indispensable due to there might be only one email in account
            for mail in it[2:]:
                dic[find(mail)] = root # concatenate all emails to the first email
        # merge related email addresses
        ret = defaultdict(list)
        for key in dic:
            ret[find(key)].append(key) # donot write as ret[dic[key]].append(key)
        return [[email2name[k]] + sorted(v) for k, v in ret.items()]