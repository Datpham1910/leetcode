"""
692. Top K Frequent Words
Medium

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.
"""

from typing import List

import collections, heapq

class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word
        
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count
    
    def __eq__(self, other):
        return self.count == other.count and self.word == other.word
class Solution:
    
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counts = collections.Counter(words)   
        
        freqs = []
        heapq.heapify(freqs)
        for word, count in counts.items():
            heapq.heappush(freqs, (Element(count, word), word))
            if len(freqs) > k:
                heapq.heappop(freqs)
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(freqs)[1])
        return res[::-1]

    def topKFrequent1(self, words: List[str], k: int) -> List[str]:
        heap = []
        result = []
        WordDic = collections.Counter(words)
        
        for word, numOfWord in WordDic.items():
            heapq.heappush(heap, (-numOfWord, word))
        
        for _ in range(k):
            wordCount = heapq.heappop(heap)
            result.append(wordCount[1])

        return result

        # dic = collections.Counter(words)
        # result = sorted(dic.keys(), key=lambda k:(-dic[k], k))
        # return result[:k]
        # # return nsmallest(k, dic.keys(), key=lambda k:(-dic[k], k))