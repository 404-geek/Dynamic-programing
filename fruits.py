from collections import defaultdict


def totalFruit(fruits):
    start = 0
    max_fruits = 0
    coll_fruits = 0

    fruit_type = defaultdict(int)

    for end in range(len(fruits)):

        fruit_type[fruits[end]] += 1
        coll_fruits += 1

        while len(fruit_type) == 3:

            max_fruits = max(coll_fruits - fruit_type[fruits[end]], max_fruits)

            fruit_type[fruits[start]] -= 1
            coll_fruits -= 1

            if fruit_type[fruits[start]] == 0:
                del fruit_type[fruits[start]]
            start += 1

    max_fruits = max(coll_fruits, max_fruits)
    return max_fruits

print(totalFruit([3,3,3,1,2,1,1,2,3,3,4]))