class Solution(object):
    def obtain_unique_values(self, s):
        """
        Creates a list with the unique elements of the receibed string.
        
        Arg:
            s(string): The given string
        
        Returns:
            list(set(s)) (list): list with the unique elements
            of the receibed string.
        """
        return list(set(s))
    
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        lexicographic_smallest = ""
        unique_characters = self.obtain_unique_values(s)
        
        while len(unique_characters) > 0:
            lexicographic_smallest += min(unique_characters)
            unique_characters.pop(unique_characters.index(min(unique_characters)))
        
        return lexicographic_smallest

s = "cbacdcbc"
distinct_characters = Solution().smallestSubsequence(s)
print(distinct_characters)
