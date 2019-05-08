class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    pass

  def delete(self):
    # delete = self.storage[0]
    # self.storage[0] = self.storage[len(self.storage) - 1]
    # self.storage.pop()
    pass

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
    pass
