class Solution:
    def isSubsequence(self, s, t):
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == len(s)

def main():
    s1 = "abc"
    t1 = "ahbgdc"
    solution = Solution()
    result = solution.isSubsequence(s1, t1)
    print(result)

    s2 = "axc"
    t2 = "ahbgdc"
    solution = Solution()
    result = solution.isSubsequence(s2, t2)
    print(result)

if __name__ == "__main__":
    main()
