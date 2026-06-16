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