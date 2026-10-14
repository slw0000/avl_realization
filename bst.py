from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    key: int = None
    left: Node | None = None
    right: Node | None = None


def add_node(root: Node | None, key: int) -> Node | None:
    if root is None:
        new_root = Node()
        new_root.key = key
        return new_root

    if key < root.key:
        root.left = add_node(root.left, key)

    if key > root.key:
        root.right = add_node(root.right, key)

    return root


def delete_node(root: Node | None, key: int) -> Node | None:
    if root is None:
        return None

    if root.key > key and root.left is not None:
        root.left = delete_node(root.left, key)

    if root.key < key and root.right is not None:
        root.right = delete_node(root.right, key)

    if root.key == key:
        if root.left is None and root.right is None:
            return None

        if root.left is None and root.right is not None:
            return root.right

        if root.left is not None and root.right is None:
            return root.left

        temp_root = root.right
        while temp_root.left is not None:
            temp_root = temp_root.left
        root.key = temp_root.key
        root.right = delete_node(root.right, temp_root.key)

    return root



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


def get_height(root: Node | None) -> int:
    if root is None:
        return 0

    return max(get_height(root.left), get_height(root.right)) + 1


def print_node(root: Node | None, sp: list[int] | None = None) -> list[int]:
    if sp is None:
        sp = []
    if root is None:
        return sp

    sp.append(root.key)

    sp = print_node(root.left, sp)
    sp = print_node(root.right, sp)

    return sp


def main():
    q = int(input())
    root = None

    for _ in range(q):
        command = input().split()

        if command[0] == "add":
            root = add_node(root, int(command[1]))

        elif command[0] == "del":
            root = delete_node(root, int(command[1]))

        elif command[0] == "exists":
            is_exists = check_node(root, int(command[1]))
            if is_exists:
                print("YES")
            else:
                print("NO")

        elif command[0] == "height":
            height = get_height(root)
            print(height)

        elif command[0] == "print":
            sp = print_node(root)
            if sp == []:
                print("Empty")
            else:
                print(" ".join(map(str, sp)))

main()
