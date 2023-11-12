# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

################### SLOW solution, because i didn't notice it's a BINARY SEARCH tree !!! ###################
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def hasNode(node, n):
            if not node:
                return False

            if node.val == n.val:
                return True

            return hasNode(node.left, n) or hasNode(node.right, n)


        if root.val == p.val or root.val == q.val:
            return root
        
        leftHasP = hasNode(root.left, p)
        rightHasQ = hasNode(root.right, q)
        
        if leftHasP and rightHasQ:
            return root

        leftHasQ = hasNode(root.left, q)
        rightHasP = hasNode(root.right, p)

        if leftHasQ and rightHasP:
            return root

        if leftHasP: # in this case, leftHasQ == True
            return self.lowestCommonAncestor(root.left, p, q)

        if rightHasP: # in this case, rightHasQ == True
            return self.lowestCommonAncestor(root.right, p, q)


################### CORRECT solution benefits from Binary search tree ###################
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root.val == p.val or root.val == q.val:
            return root
        
        if p.val < root.val < q.val:
            return root

        if q.val < root.val < p.val:
            return root

        if p.val < root.val: # in this case, q.val < root.val
            return self.lowestCommonAncestor(root.left, p, q)

        if root.val < p.val: # in this case, root.val < q.val
            return self.lowestCommonAncestor(root.right, p, q)
