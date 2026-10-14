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

    return replace_node(root, key, tree)


def right(root: Node, key: int) -> Node:
    tree = find_node(root, key)

    prev_root = tree
    prev_root_left = tree.left

    prev_root.left = prev_root_left.right
    tree = prev_root_left
    tree.right = prev_root

    return replace_node(root, key, tree)

def main():
    q = int(input())
    root = None

    sp = list(map(int, input().split()))
    for i in sp:
        root = add_node(root, i)

    m = int(input())
    for _ in range(m):
        command = input().split()
        if command[0] == 'left':
            root = left(root, int(command[1]))
            sp = print_node(root)
            print(' '.join(map(str, sp)))
        if command[0] == 'right':
            root = right(root, int(command[1]))
            sp = print_node(root)
            print(' '.join(map(str, sp)))

main()
