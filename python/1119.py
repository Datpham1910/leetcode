import re

class Solution:
    def remove_vowels(self, s: str) -> str:
        return re.sub('[aeiouAEIOU]', '', s)

print(Solution().remove_vowels('chau len ba hauchaubsc'))