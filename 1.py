#**********Q1*********#
class Solution:
    def checkStraightLine(self, coordinates):
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if (x - x0) * (y1 - y0) != (y - y0) * (x1 - x0):
                return False

        return True
    
    #************Q2***********#
    class Solution:
    def checkValidString(self, s: str) -> bool:
		# Simplify s to reduce complexity in further loop
        while s != s.replace("()", ""):
            s = s.replace("()", "")
			
		"""
		The first loop, from left to right, is to check if there are supplementary ")" before "(".
		For example, a string like ")(*" won't be able to pass the first loop.
		"""
        queue = []
        for i in range(len(s)):
            if s[i] in ["(", "*"]:
                queue.append(1)
            else:
                if queue:
                    queue.pop()
                else:
                    return False

		"""
		The second loop, from right to left, is to check if there are supplementary "(" after ")".
		For example, a string like "*)(" won't be able to pass the second loop.
		"""
        queue = []
        for i in range(len(s) - 1, -1, -1):
            if s[i] in [")", "*"]:
                queue.append(1)
            else:
                if queue:
                    queue.pop()
                else:
                    return False
        return True
    
    #************Q3**************3
    def minDistance(self, word1: str, word2: str) -> int:
	def solve(w1, w2, i, j):
		if i == L1 and j == L2 : return 0
		if i == L1 or j == L2 : 
			return max(L1 - i, L2 - j)
		if w1[i] == w2[j] : 
			return solve(w1, w2, i + 1, j + 1)                
		return 1 + min(solve(w1, w2, i + 1, j), solve(w1, w2, i, j + 1))
	L1, L2 = len(word1), len(word2)
	return solve(word1, word2, 0, 0)   

    #****************Q4**********#
    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(N) where N is the number of the nodes in the tree
# Space Complexity: O(H) where H is the height of the tree. 
# In worse case, H can be N when it is a left skewed binary tree / right skewed binary tree
class Solution:
    # case 1: root is nullptr -> ""
    # case 2: root doesn't have left sub tree and right sub tree -> root.val
    # case 3: root.left is not nullptr -> root.val + (dfs result from left sub tree)
    # case 4: root.left is nullptr but root.right is not nullptr -> root.val + () 
    # case 5: root.right is not nullptr -> root.val + (dfs result from right sub tree)
    def tree2str(self, root: Optional[TreeNode]) -> str:
        # handle case 1
        if root is None:
            return ''
        # we convert root.val to string here, then append results from different cases
        s = str(root.val)
        # handle case 2
        # this line is obviously not necessary
        if root.left is None and root.right is None:
            s += ''
        # handle case 3
        if root.left:
            s += '({})'.format(self.tree2str(root.left))
        # handle case 4
        # alternatively, you can use `elif root.right: s += '()'`
        if root.left is None and root.right:
            s += '()'
        # handle case 5
        if root.right:
            s += '({})'.format(self.tree2str(root.right))
        return s        
    
    #************Q5***********#
    class Solution:
  def compress(self, chars: List[str]) -> int:
    ans = 0
    i = 0

    while i < len(chars):
      letter = chars[i]
      count = 0
      while i < len(chars) and chars[i] == letter:
        count += 1
        i += 1
      chars[ans] = letter
      ans += 1
      if count > 1:
        for c in str(count):
          chars[ans] = c
          ans += 1

    return ans

    #***********Q6**********#
        def findAnagrams(self, s: str, p: str) -> List[int]:
        hm, res, pL, sL = defaultdict(int), [], len(p), len(s)
        if pL > sL: return []

        # build hashmap
        for ch in p: hm[ch] += 1

        # initial full pass over the window
        for i in range(pL-1):
            if s[i] in hm: hm[s[i]] -= 1
            
        # slide the window with stride 1
        for i in range(-1, sL-pL+1):
            if i > -1 and s[i] in hm:
                hm[s[i]] += 1
            if i+pL < sL and s[i+pL] in hm: 
                hm[s[i+pL]] -= 1
                
            # check whether we encountered an anagram
            if all(v == 0 for v in hm.values()): 
                res.append(i+1)
                
        return res

    #*************Q7***********#
    
class Solution(object):
    def decodeString(self, s):
        stack = []; curNum = 0; curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():     # curNum*10+int(c) is helpful in keep track of more than 1 digit number
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString
    
    #***********Q8************#
    class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n = len(s)

        if len(goal) != n:
            return False;

        if s == goal:
            temp = set(s)
            return len(temp) < len(goal)  # Swapping same characters

        i = 0
        j = n - 1

        while i < j and s[i] == goal[i]:
            i += 1

        while j >= 0 and s[j] == goal[j]:
            j -= 1

        if i < j:
            s_list = list(s)
            s_list[i], s_list[j] = s_list[j], s_list[i]
            s = ''.join(s_list)

        return s == goal

