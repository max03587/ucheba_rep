1.
```python
class Solution:

    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:

        y = sorted(arr,reverse = True)

        print(y)

        a = 1

        if len(arr) != 1:

            u = y[0] - y[1]

        for i in range(len(y) - 2):

            if y[a] - y[a+1] != u:

                return False

            a = a+1

        return True
```

2.
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
```

3.
```python
class Solution:

    def isPalindrome(self, x: int) -> bool:

        p = str(x)

        o = []

        for u in p:

            o += u

        print(o)

        if o == o[::-1]:

            return True

        else:

            return False
```
4.
```python
  

class Solution:

    def isUgly(self, n: int) -> bool:

        a = 2

        p = []

        if n < 0 :

            return False

        if n == 0:

            return False

        n = abs(n)

        if (n ** 0.5)%1 == 0:

            n = n ** 0.5

        while n != 1:

            if (n/a)%1 == 0:

                p.append(a)

                while (n/a)%1 == 0:

                    n = n/a

                    if (n ** 0.5)%1 == 0:

                        n = n ** 0.5

            else:

                a = a + 1

        print(p)

        while 2 in p:

            p.remove(2)

        while 3 in p:

            p.remove(3)

        while 5 in p:

            p.remove(5)

        if len(p) == 0:

            return True

        else:

            return False
```