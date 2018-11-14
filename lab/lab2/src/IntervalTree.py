import lab2.src.RBtree as rb
import json
RED = rb.RED
BLACK = rb.BLACK


class Interval(object):
    def __init__(self, low=-1, high=-1):
        self.low = low
        self.high = high


class IntervalTreeNode(rb.RBtreeNode):

    def __init__(self, high, low=-1, color=BLACK, left=None, right=None, p=None):
        rb.RBtreeNode.__init__(self, low, color, left, right, p)
        self.int = Interval()
        self.int.low = self.key
        self.int.high = high
        self.max = high



class IntervalTree(object):

    def __init__(self):
        self.nil = IntervalTreeNode(high=-1)
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
        I = {}
        I['low'] = x.int.low
        I['high'] = x.int.high
        S['int'] = I
        S['max'] = x.max
        S['left'] = self.traverse(T, x.left)
        S['right'] = self.traverse(T, x.right)
        return S


class IntervalProcess(rb.RBProcess):
    r"""
    description: basic methods of IntervalTree, other's inherit from RBProcess
    override methods:
        left_rotate(T, x)
        right_rotate(T, x)
    new methods:
        interval_find(T, key)
        fix_max(x)
        interval_insert(T, x)
        interval_delete(T, x)
        interval_max_fixup(T, x)
        interval_search(T, i)
        overlaps(x, y)
    inherit methods:
        rb_insert_fixup(T, x)
        rb_delete_fixup(T, x)
        rb_tree_minimum(T, x)
        rb_transplant(T, u, v)
    """
    def overlap(self, x, y):
        """
        :param x: interval
        :param y: interval
        :return: if x overlaps y than True else False
        """
        if (not x.high < y.low) and (not y.high < x.low):
            return True
        else:
            return False

    def interval_search(self, T, i):
        x = T.root
        while x != T.nil and (not self.overlap(i, x.int)):
            if x.left != T.nil and x.left.max >= i.low:
                x = x.left
            else:
                 x = x.right
        return x

    def interval_find(self, T, key):
        return self.rb_find(T, key)

    def fix_max(self, x):
        x.max = max(x.int.high, x.left.max, x.right.max)
        return True

    def left_rotate(self, T, x):
        y_back = x.right
        x_back = x
        process = rb.RBProcess()
        process.left_rotate(T, x)
        # order is important
        self.fix_max(x_back)
        self.fix_max(y_back)
        return True

    def right_rotate(self, T, x):
        y_back = x.left
        x_back = x
        process = rb.RBProcess()
        process.right_rotate(T, x)
        # order is important
        self.fix_max(x_back)
        self.fix_max(y_back)
        return True

    def interval_insert(self, T, z):
        y = T.nil
        x = T.root
        while x != T.nil:
            y = x
            # add max control
            if y.max < z.max:
                y.max = z.max
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
        # there is no need of a max control in following function
        # because  except insert and delete, only rotation can change property max.
        self.rb_insert_fixup(T, z)
        return True

    def interval_delete(self, T, z):
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
            self.interval_max_fixup(T, x)
            self.rb_delete_fixup(T, x)
        return True

    def interval_max_fixup(self, T, x):
        while x != T.nil:
            self.fix_max(x)
            x = x.p
        return True

if __name__=='__main__':
    T = IntervalTree()
    Process = IntervalProcess()
    low_list = [16, 8, 25, 5, 15, 17, 26, 0, 6, 19]
    high_list = [21, 9, 30, 8, 23, 19, 26, 3, 10, 20]
    for i in range(low_list.__len__()):
        x = IntervalTreeNode(low=low_list[i], high=high_list[i])
        Process.interval_insert(T, x)
    T.output(T, T.root)
    print(Process.interval_search(T, Interval(7, 9)).key)
    print(Process.interval_search(T, Interval(0, 2)).key)
    print(Process.interval_search(T, Interval(27, 30)).key)
    print(Process.interval_search(T, Interval(31, 32)).key)
    # delete_list = [8, 5, 17, 0, 19, 16, 25, 15, 26, 6]
    # for i in range(high_list.__len__()):
    #     x = Process.interval_find(T, delete_list[i])
    #     Process.interval_delete(T, x)
    #     T.output(T, T.root)
    #     print('\n-----------------------------------------------\n')
