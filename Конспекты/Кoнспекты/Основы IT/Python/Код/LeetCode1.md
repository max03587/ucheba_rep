
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

