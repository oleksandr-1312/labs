class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    @staticmethod
    def from_file(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            values = file.read().split()

        if not values or values[0] == 'N': 
            return None
            
        root = BinaryTree(int(values[0]))
        queue = [root]
        i = 1
        
        while i < len(values):
            current = queue.pop(0)
            
            if i < len(values) and values[i] != 'N':
                current.left = BinaryTree(int(values[i]))
                queue.append(current.left)
            i += 1
            
            if i < len(values) and values[i] != 'N':
                current.right = BinaryTree(int(values[i]))
                queue.append(current.right)
            i += 1
            
        return root

    def print_side_view(self, prefix="", is_left=None):
        """Вивід дерева з боку з намальованими лініями (палками)"""
        # Спочатку йдемо в праве піддерево (воно буде зверху при виводі)
        if self.right:
            self.right.print_side_view(prefix + ("│   " if is_left else "    "), False)
            
        # Виводимо поточний вузол з відповідною "палкою"
        if is_left is None:
            print(prefix + "── " + str(self.value))     # Корінь
        elif is_left:
            print(prefix + "└── " + str(self.value))    # Ліва гілка
        else:
            print(prefix + "┌── " + str(self.value))    # Права гілка
            
        # Потім йдемо в ліве піддерево (воно буде знизу)
        if self.left:
            self.left.print_side_view(prefix + ("    " if is_left else "│   "), True)


def branchSums(root):
    if root is None:
        return 0
    
    sum_left = 0
    if root.left and root.left.left is None and root.left.right is None:
        sum_left += root.left.value
    else:
        sum_left += branchSums(root.left)
        
    sum_left += branchSums(root.right)
    
    return sum_left