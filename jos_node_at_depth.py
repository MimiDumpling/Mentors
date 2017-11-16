def print_node_at_depth(root, depth):
    
    def wut_depth(root, depth, current_d):

        # base case
        if current_d == depth:
            print node
        else:
            current_d += 1
            wut_depth(root.left, depth, current_d)
            wut_depth(root.right, depth, current_d)
