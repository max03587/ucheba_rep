
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