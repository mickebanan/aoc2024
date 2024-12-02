import helpers

data = """
3   4
4   3
2   5
1   3
3   9
3   3""".split('\n')
data = open('1.dat').readlines()
values = [tuple(row.split()) for row in data if row]
first = sorted(int(t[0]) for t in values)
second1 = sorted(int(t[1]) for t in values)
second2 = second1.copy()

@helpers.timer
def solve():
    s1 = s2 = 0
    for v1 in first:
        v2 = second1.pop(0)
        s1 += abs(v1 - v2)
        score = len([v2 for v2 in second2 if v2 == v1])
        s2 += v1 * score
    print(s1, s2)
solve()