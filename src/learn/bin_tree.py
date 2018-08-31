#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @author: LoopGan
    @contact: ganwei4955@gamil.com
    @time: 8/31/2018 1:39 PM
"""


class Node:
    def __init__(self, item):
        self.item = item
        self.lchild = None
        self.rchild = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
        else:
            q = [self.root]
            while True:
                pop_node = q.pop(0)
                if pop_node.lchild is None:
                    pop_node.lchild = node
                    return
                elif pop_node.rchild is None:
                    pop_node.rchild = node
                    return
                else:
                    q.append(pop_node.lchild)
                    q.append(pop_node.rchild)

    def traverse(self):
        if self.root is None:
            return None
        q = [self.root]
        res = [self.root.item]
        while q != []:
            pop_node = q.pop(0)
            if pop_node.lchild is not None:
                q.append(pop_node.lchild)
                res.append(pop_node.lchild.item)
            if pop_node.rchild is not None:
                q.append(pop_node.rchild)
                res.append(pop_node.rchild.item)
        return res

    def preorder(self, root):
        if root is None:
            return []
        result = [root.item]
        l_item = self.preorder(root.lchild)
        r_item = self.preorder(root.rchild)
        return result + l_item + r_item

    def inorder(self, root):
        if root is None:
            return []
        result = [root.item]
        l_item = self.inorder(root.lchild)
        r_item = self.inorder(root.rchild)
        return l_item + result + r_item

    def postorder(self, root):
        if root is None:
            return []
        result = [root.item]
        l_item = self.postorder(root.lchild)
        r_item = self.postorder(root.rchild)
        return l_item + r_item + result


if __name__ == "__main__":
    t = Tree()
    for i in range(10):
        t.add(i)
    print(t.traverse())
    print(t.preorder(t.root))
    print(t.inorder(t.root))
    print(t.postorder(t.root))
    print("hello imp")
