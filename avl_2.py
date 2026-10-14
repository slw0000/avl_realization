from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    key: int = None
    left: Node | None = None
    right: Node | None = None
    height: int = 1


def update_height(root: Node | None) -> int:
    if root is None:
        return 0

    lft = root.left.height if root.left else 0
    rght = root.right.height if root.right else 0

    return max(lft, rght) + 1


def get_balance(root: Node) -> int:
    lft = root.left.height if root.left else 0
    rght = root.right.height if root.right else 0

    return rght - lft


def balance(root: Node) -> Node | None:
    bal = get_balance(root)

    if bal == 2:
        if get_balance(root.right) >= 0:
            return left(root, root.key)
        else:
            right(root, root.right.key)
            return left(root, root.key)
    if bal == -2:
        if get_balance(root.left) <= 0:
            return right(root, root.key)
        else:
            left(root, root.left.key)
            return right(root, root.key)

    return root


def add_node(root: Node | None, key: int) -> Node | None:
    if root is None:
        new_root = Node()
        new_root.key = key
        new_root.height = 1
        return new_root

    elif key < root.key:
        root.left = add_node(root.left, key)

    elif key > root.key:
        root.right = add_node(root.right, key)

    root.height = update_height(root)
    return balance(root)


def check_node(root: Node | None, key: int) -> bool:
    if root is None:
        return False

    if key == root.key:
        return True

    if root.left is not None and key < root.key:
        return check_node(root.left, key)
    if root.right is not None and key > root.key:
        return check_node(root.right, key)

    return False


def find_node(root: Node | None, key: int) -> Node | None:
    if root is None:
        return None

    if key == root.key:
        return root

    if root.left is not None and key < root.key:
        return find_node(root.left, key)
    if root.right is not None and key > root.key:
        return find_node(root.right, key)

    return None


def replace_node(root: Node | None, key: int, tree: Node) -> Node:
    if key == root.key:
        return tree

    if root.left is not None and key < root.key:
        root.left = replace_node(root.left, key, tree)
    if root.right is not None and key > root.key:
        root.right = replace_node(root.right, key, tree)

    return root


def print_node(root: Node | None, sp: list[int] | None = None) -> list[int]:
    if sp is None:
        sp = []
    if root is None:
        return sp

    sp.append(root.key)
    sp = print_node(root.left, sp)
    sp = print_node(root.right, sp)

    return sp


def left(root: Node, key: int) -> Node:
    tree = find_node(root, key)

    prev_root = tree
    prev_root_right = tree.right

    prev_root.right = prev_root_right.left
    tree = prev_root_right
    tree.left = prev_root

    tree.left.height = update_height(tree.left)
    tree.height = update_height(tree)

    return replace_node(root, key, tree)


def right(root: Node, key: int) -> Node:
    tree = find_node(root, key)

    prev_root = tree
    prev_root_left = tree.left

    prev_root.left = prev_root_left.right
    tree = prev_root_left
    tree.right = prev_root

    tree.right.height = update_height(tree.right)
    tree.height = update_height(tree)

    return replace_node(root, key, tree)


def main():
    q = int(input())
    root = None

    for _ in range(q):
        command = input().split()

        if command[0] == "add":
            root = add_node(root, int(command[1]))

        elif command[0] == "root":
            if root is None:
                print("Empty")
            else:
                print(root.key)

        elif command[0] == "exists":
            is_exists = check_node(root, int(command[1]))
            if is_exists:
                print("YES")
            else:
                print("NO")

        elif command[0] == "height":
            if root is None:
                print(0)
            else:
                print(root.height)

        elif command[0] == "print":
            sp = print_node(root)
            if sp == []:
                print("Empty")
            else:
                print(" ".join(map(str, sp)))

main()
