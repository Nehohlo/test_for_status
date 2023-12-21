from copy import deepcopy
from collections import defaultdict


class TreeStore:
    def __init__(self, tree: list[dict]):
        self.tree = {}
        self.children = defaultdict(list)

        for item in tree:
            self.tree.update({item['id']: deepcopy(item)})
            self.children[item['parent']].append(item['id'])

    def getAll(self) -> list[dict]:
        return list(self.tree.values())

    def getItem(self, item_id: int) -> dict:
        return self.tree[item_id]

    def getChildren(self, item_id: int) -> list[dict]:
        if item_id in self.children:
            return [self.getItem(key) for key in self.children[item_id]]

        return []

    def getAllParents(self, item_id: int) -> list[dict]:
        parents = [self.getItem(item_id)]
        parent_id = parents[-1]['parent']

        while parent_id != 'root':
            item = self.getItem(parent_id)
            parents.append(item)
            parent_id = item['parent']

        return parents
