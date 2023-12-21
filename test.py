from random import randint
from timeit import timeit

from TreeStore import TreeStore

items: list[dict] = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]

ts = TreeStore(items)

print(f'Результат для изначального древа элементов')
print('getAll()')
print(ts.getAll())
print(timeit('ts.getAll()', number=1, globals=globals()), end='\n\n')

print('getItem(7)')
print(ts.getItem(7))
print(timeit('ts.getItem(7)', number=1, globals=globals()), end='\n\n')

print('getChildren(4)')
print(ts.getChildren(4))
print(timeit('ts.getChildren(4)', number=1, globals=globals()), end='\n\n')

print('getChildren(5)')
print(ts.getChildren(5))
print(timeit('ts.getChildren(5)', number=1, globals=globals()), end='\n\n')

print('getAllParents(8)')
print(ts.getAllParents(8))
print(timeit('ts.getAllParents(8)', number=1, globals=globals()), end='\n\n')


def test(count_items: int):
    new_items = items.copy()

    for _ in range(8, count_items):
        new_items.append(
            {
                "id": len(new_items) + 1,
                "parent": new_items[randint(2, len(new_items) - 1)]["id"],
                "type": "test" if len(new_items) % 5 == 0 else None
            }
        )

    ts = TreeStore(new_items)

    print(f'Результат для древа из {count_items} элементов')
    print('getAll()')
    print(timeit('ts.getAll()', number=1, globals={'ts': ts}), end='\n\n')

    i = randint(1, count_items - 1)
    print(f'getItem({i})')
    print(timeit(f'ts.getItem({i})', number=1, globals={'ts': ts}), end='\n\n')

    i = randint(1, count_items - 1)
    print(f'getChildren({i})')
    print(timeit(f'ts.getChildren({i})', number=1, globals={'ts': ts}), end='\n\n')

    i = randint(1, count_items - 1)
    print(f'getChildren({i})')
    print(timeit(f'ts.getChildren({i})', number=1, globals={'ts': ts}), end='\n\n')

    print(f'getAllParents({count_items - 1})')
    print(timeit(f'ts.getAllParents({count_items - 1})', number=1, globals={'ts': ts}), end='\n\n')


test(10_000)
test(100_000)
test(10_000_000)
