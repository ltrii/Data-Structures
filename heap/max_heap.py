class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    delete = self.storage[0]
    self.storage[0] = self.storage[len(self.storage) - 1]
    self.storage.pop()
    self._sift_down(0)
    return delete

  def get_max(self):
    if self.storage[0] != None:
      return self.storage[0]
    else:
      return None

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while (index - 1) // 2 >= 0:
        if self.storage[(index - 1) // 2] < self.storage[index]:
            self.storage[index], self.storage[(
                index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
        index = (index - 1) // 2

  def _sift_down(self, index):
    storage = self.storage
    maxid = None
    if index * 2 + 1 >= self.get_size():
        return
    elif index * 2 + 2 >= self.get_size():
        maxid = index * 2 + 1
    elif storage[index * 2 + 1] > storage[index * 2 + 2]:
        maxid = index * 2 + 1
    else:
        maxid = index * 2 + 2

    if storage[index] < storage[maxid]:
        storage[index], storage[maxid] = storage[maxid], storage[index]
        self._sift_down(maxid)
    else:
        return
