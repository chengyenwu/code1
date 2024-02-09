# 131. Palindrome partitioning
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # recursive
        def is_palindrome(s):
            if s == s[::-1]:
                return True

        def dfs(result, curr_index, path):
            if not s:
                return [[]]
            if curr_index == len(s):
                result.append(path)
            for i in range(curr_index, len(s)):
                substring = s[curr_index : i+1]
                if is_palindrome(substring) == True:
                    dfs(result, i+1, path + [substring])
            
        result=[]
        path=[]
        dfs(result, 0, path)
        return result

# recording (s="aab")
# i=0
# substring = s[0: 0+1] = s[0 : 1] = a
# is_palindrome(a) = True
# dfs(result, 0+1, []+["a"])
#     # i=1
#     substring = s[1 : 1+1] = s[1 : 2] = a
#     is_palindrome(a) = True
#     dfs(result, 1+1, ["a"] + ["a"])
#         # i=2
#         substring = s[2 : 2+1] = s[2 : 3] = b
#         is_palindrome(b) = True
#         dfs(result, 2+1, ["a", "a"] + ["b"])  ==> 3 = len(s) = 3, result = [["a", "a", "b"]]
#     # i=2
#     substring = s[1 : 2+1] = s[1 : 3] = ab
#     is_palindrome(ab) = False
# i=1
# substring = s[0 : 1+1] = s[0 : 2] = aa
# is_palindrome(aa) = True
# dfs(result, 1+1, [] + ["aa"])
#     # i=2
#     substring = s[2 : 2+1] = s[2 : 3] = b
#     is_palindrome(b) = True
#     dfs(result, 2+1, ["aa"] + ["b"])  ==> 3 = len(s) = 3, result = [["a", "a", "b"], ["aa", "b"]]
# i=2
# substring = s[0 : 2+1] = s[0 : 3] = aab
# is_palindrome(aab) = False