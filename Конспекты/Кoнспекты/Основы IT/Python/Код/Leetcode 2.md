```python
class Solution:

    def pivotInteger(self, n: int) -> int:

        a=1

        r =0

        o = []

        for i in range(n+1):

            o.append(i)

        o = sorted(o, reverse = False)

        o.remove(0)

        while True:

            r = r+1

            if sum(o[:a]) == sum(o[a-1:]):

                return r

            a = a + 1

            if r == n:

                return -1
