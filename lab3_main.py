from lab3 import BinaryTree, branchSums

def main():
    root = BinaryTree.from_file('tree_data.txt')

    if root:
        print("--- Дерево (Вид з боку) ---")
        root.print_side_view()

        result = branchSums(root)

if __name__ == "__main__":
    main()
    