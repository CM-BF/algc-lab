"""
author:Citrine GUI
date: 9th, November 2018
description:红黑树维护算法及其区间树应用：实现红黑树的插入删除算法，实现区间树上的重叠区间查找算法。程序输出的演示方式不限。
"""
import json
RED = 'RED'
BLACK = 'BLACK'


class RBtreeNode(object):
    r"""
    description: implement basic node structure of Red Black tree
    properties: color, key, left, right, parent
    """
    def __init__(self, key=-1, color=BLACK, left=None, right=None, p=None):
        self.color = color
        self.key = key
        self.left = left
        self.right = right
        self.p = p



class RBtree(object):
    r"""
    description: basic Red Black tree including nodes of nil and root
    """
    def __init__(self):
        self.nil = RBtreeNode()
        self.nil.left = self.nil
        self.nil.right = self.nil
        self.nil.p = self.nil
        self.root = self.nil

    def output(self, T, x):
        """
        description: output the structure of RBtree in json format
        :param x: root node
        :return: True when success
        """
        structure = self.traverse(T, x)
        json_structure = json.dumps(structure, indent=5)
        print('json_structure:\n' + json_structure)
        return True

    def traverse(self, T, x):
        """
        description: deep first traverse
        :param S: structure
        :param x: current node
        :return: child structure
        """
        S = {}
        S['key'] = x.key
        S['color'] = x.color
        if x == T.nil:
            return S
        S['left'] = self.traverse(T, x.left)
        S['right'] = self.traverse(T, x.right)
        return S


class RBProcess(object):
    r"""
    description: basic methods of Red Black tree
    method:
        rb_find(T, key)
        left_rotate(T, x)
        right_rotate(T, x)
        rb_insert(T, x)
        rb_delete(T, x)
        rb_transplant(T, u, v)
        rb_insert_fixup(T, x)
        rb_delete_fixup(T, x)
        rb_tree_minimum(T, x)
    """
    def rb_find(self, T, key):
        """
        description: find the node that key is key.
        :param T: RBtree
        :param key: RBtreeNode
        :return: target node <RBtreeNode>
        """
        x = T.root
        while x != T.nil:
            if x.key == key:
                return x
            if key < x.key:
                x = x.left
            else:
                x = x.right
        raise Exception("In rb_find : Can't not find a node with key=%d" % key)

    def left_rotate(self, T, x):
        r"""
        description: left rotate with x which is the center of this rotate
        :param T: <class RBtree> stand of RBtree
        :param x: <class RBtreeNode>the center of rotate
        :return: True when success (change the Red Black tree in memory directly)
        """
        y = x.right
        x.right = y.left
        if y.left != T.nil:
            y.left.p = x
        y.p = x.p
        if x.p == T.nil:
            T.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y
        return True

    def right_rotate(self, T, x):
        r"""
        description: Right rotate with x which is the center of this rotate
        :param T: <class RBtree> stand of RBtree
        :param x: <class RBtreeNode>the center of rotate
        :return: True when success (change the Red Black tree in memory directly)
        """
        y = x.left
        x.left = y.right
        if y.right != T.nil:
            y.right.p = x
        y.p = x.p
        if x.p == T.nil:
            T.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.right = x
        x.p = y
        return True

    def rb_insert(self, T, z):
        """
        description: This method is about to  insert an node x to the end of T.
        :param T: RBtree
        :param z: RBtreeNode
        :return: True when success
        """
        y = T.nil
        x = T.root
        while x != T.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == T.nil:
            T.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = T.nil
        z.right = T.nil
        z.color = RED
        self.rb_insert_fixup(T, z)
        return True

    def rb_delete(self, T, z):
        """
        description: Delete a node from RBtree
        :param T: RBtree
        :param z: RBtreeNode : which will be deleted
        :return: True when success
        """
        y = z
        y_original_color = y.color
        if z.left == T.nil:
            x = z.right
            self.rb_transplant(T, z, z.right)
        elif z.right == T.nil:
            x = z.left
            self.rb_transplant(T, z, z.left)
        else:
            y = self.rb_tree_minimum(T, z.right)
            y_original_color = y.color
            x = y.right
            if y.p == z:
                x.p = y
            else:
                self.rb_transplant(T, y, y.right)
                y.right = z.right
                y.right.p = y
            self.rb_transplant(T, z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if y_original_color == BLACK:
            self.rb_delete_fixup(T, x)
        return True

    def rb_transplant(self, T, u, v):
        """
        description: Transplant v node to u node's position
        :param T: RBtree
        :param u: RBtreeNode
        :param v: RBtreeNode
        :return: True when success
        """
        if u.p == T.nil:
            T.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p
        return True

    def rb_insert_fixup(self, T, z):
        """
        description: if z.p.color == RED, there is a violation about property 4, thus, we have to fix it
        :param T: RBtree
        :param z: RBtreeNode
        :return: True when success
        """
        while z.p.color == RED:
            if z.p == z.p.p.left:
                # y uncle node
                y = z.p.p.right
                if y.color == RED:
                    # case 1 : RED uncle, BLACK down
                    z.p.color = BLACK
                    y.color = BLACK
                    z.p.p.color = RED
                    z = z.p.p
                else:
                    # case 2-3: BLACK uncle RR'B'B->R'B'RB  ''means top node:  rotate and exchange color
                    if z == z.p.right:
                        # case 2 : turn to z == z.p.left case
                        z = z.p
                        self.left_rotate(T, z)
                    z.p.color = BLACK
                    z.p.p.color = RED
                    self.right_rotate(T, z.p.p)
            else:
                # the mirror operator of which we saw above
                y = z.p.p.left
                if y.color == RED:
                    z.p.color = BLACK
                    y.color = BLACK
                    z.p.p.color = RED
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self.right_rotate(T, z)
                    z.p.color = BLACK
                    z.p.p.color = RED
                    self.left_rotate(T, z.p.p)
        T.root.color = BLACK
        return True

    def rb_delete_fixup(self, T, x):
        """
        description: if y.color == BLACK then x and y.p(now x.p) may have the same color RED, it violates property 4
                    and because of the leaving of y(BLACK), its original parent's black height will be subtracted by 1,
                    to fix it, we have to assume that the x has another layer of BLACK, so it will be double BLACK or
                    RED + BLACK. And this method is constructed to solve this.
        :param T: RBtree
        :param x: RBtreeNode
        :return: True when success
        """
        while x != T.root and x.color == BLACK:
            if x == x.p.left:
                w = x.p.right
                # w is x's cousin
                if w.color == RED:
                    # case 1: turn to the case that x's cousin.color is BLACK
                    w.color = BLACK
                    x.p.color = RED
                    self.left_rotate(T, x.p)
                    w = x.p.right
                if w.left.color == BLACK and w.right.color == BLACK:
                    # case 2: BLACK up, turn x to parent node
                    w.color = RED
                    x = x.p
                else:
                    if w.right.color == BLACK:
                        # case 3: cousin w's right is BLACK, turn to case 4 that cousin w's right is RED
                        w.left.color = BLACK
                        w.color = RED
                        self.right_rotate(T, w)
                        w = x.p.right
                    # case 4: top link is: dB '?' B R -> B B '?' B : a BLACK of dB push color to right and overlap the
                    # most right RED and rotate for color balance
                    w.color = x.p.color
                    x.p.color = BLACK
                    w.right.color = BLACK
                    self.left_rotate(T, x.p)
                    # case 4 solve that dilemma directly
                    x = T.root
            else:
                # the mirror operator
                w = x.p.left
                if w.color == RED:
                    w.color = BLACK
                    x.p.color = RED
                    self.right_rotate(T, x.p)
                    w = x.p.left
                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED
                    x = x.p
                else:
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self.left_rotate(T, w)
                        w = x.p.left
                    w.color = x.p.color
                    x.p.color = BLACK
                    w.left.color = BLACK
                    self.right_rotate(T, x.p)
                    x = T.root
        x.color = BLACK
        return True

    def rb_tree_minimum(self, T, x):
        """
        description: get the most left child node
        :param T: RBtree
        :param x: RBtreeNode
        :return: the most left child node
        """
        while x.left != T.nil:
            x = x.left
        return x


if __name__ == "__main__":
    T = RBtree()
    Process = RBProcess()
    key_list = [41, 38, 31, 12, 19, 8]
    for i in range(6):
        x = RBtreeNode(key=key_list[i])
        Process.rb_insert(T, x)
    T.output(T, T.root)
    delete_list = [8, 12, 19, 31, 38, 41]
    for i in range(6):
        x = Process.rb_find(T, delete_list[i])
        Process.rb_delete(T, x)
        T.output(T, T.root)
        print('\n-----------------------------------------------\n')


