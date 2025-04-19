class Solution:
    def clearDigits(self, s):
        s = list(s)
        i = 0
        while i < len(s):
            if s[i].isdigit():
                del s[i]
                if i > 0:
                    del s[i - 1]
                    i -= 1
            else:
                i += 1
        return "".join(s)

def main():
    test_cases = ["abc", "cb34"]
    sol = Solution()
    for s in test_cases:
        print(sol.clearDigits(s))

if __name__ == "__main__":
    main()
