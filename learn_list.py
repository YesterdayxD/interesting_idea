class LNode(object):
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LinkedListUnderflow(ValueError):
    pass


class LList(object):
    def __init__(self):
        self._head = None
        self.num = 0

    def is_empty(self):
        return self._head is None

    def len(self):
        return self.num

    def located(self, loc):
        if loc > self.num or loc < 1:
            raise LinkedListUnderflow('in located')
        temp = self._head
        i = 1
        if loc == 1:
            return temp
        else:
            while i < loc:
                temp = temp.next
                i += 1
            return temp

    def located_add(self, loc, elem):
        temp = self.located(loc)  # 这句可以放到else里边
        node = LNode(elem)
        if loc == 1:
            node.next = self._head
            self._head = node
        else:
            node.next = temp.next
            temp.next = node
        self.num += 1

    def located_del(self, loc):
        temp = self.located(loc)
        if loc == 1:
            self._head = self._head.next
        else:
            temp.next = temp.next.next
        self.num -= 1

    def prepend(self, elem):
        self._head = LNode(elem, self._head)
        self.num += 1

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop')
        e = self._head.elem
        self._head = self._head.next
        self.num -= 1
        return e

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            self.num += 1
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)
        self.num += 1

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop_last')
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            self.num -= 1
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        self.num -= 1
        return e

    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem)
            if p.next is not None:
                print(' ')
            p = p.next
        print("xxx")


if __name__ == "__main__":
    l = LList()
    l.append(1)
    l.append(2)
    l.append(3)
    l.printall()
    l.pop_last()
    l.printall()
