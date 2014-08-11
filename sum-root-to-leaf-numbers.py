class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
    	if not root:
    		return 0
    	stack = [root]
    	visited = [False]
    	top = 0
    	count = 0
    	data = [str(root.val)]
    	while stack:    
    		if visited[top]:
    			data.pop()
    			stack.pop()
    			visited.pop()
    			top -= 1
    			if not stack:
    				break
    			if not visited[top] and stack[top].right:
    				visited[top] = True
    				stack.append(stack[top].right)
    				visited.append(False)
    				data.append(str(stack[top].right.val))
    				top += 1
    			else:
    				 visited[top] = True
    				 continue 
    			continue  				

    		node = stack[top]
    		if not node.left and not node.right:
    			count += int("".join(data))    			
    			visited[top] = True		
    		elif node.left and node.right:
    			stack.append(node.left)
    			visited.append(False)
    			top += 1
    			data.append(str(node.left.val))
    		elif node.left and not node.right:
    			visited[top] = True
    			stack.append(node.left)
    			visited.append(False)
    			top += 1
    			data.append(str(node.left.val))    			
    		elif not node.left and node.right:
    			visited[top] = True
    			stack.append(node.right)
    			visited.append(False)
    			top += 1
    			data.append(str(node.right.val))
    	return count