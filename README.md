# The fall

## Why ?

1/ Making fun about learning dev methodology like TDD
2/ Making a co-op game
3/ Spending time with interesting colleagues :)

## Methodology

Ok, we can spend hours to talk about TDD, Why TDD and How TDD. Or talking about UML.
Instead of that, I am going to give you the Dev survivor guide.

### Use pen and paper

Before coding some thing, take a paper and a pen, and **draw**. You can make square, bubble,
tree. It is up to you but make your idea clear as water.

### Test first, test everything

The related idea is simple: 

1/ imagine what you need
2/ create a test (unittest, we will talk later) about what you want to do
3/ the **simpliest** function that you need.
4/ the test will work
5/ repeat 1-4

### git commit

Basic rule on git : make commits as atomic as possible. Do not commit your day job in one commit.

### code guideline

This a python oriented guideline

- add comments for :
    - module
    - class
    - function/member
- a function should not have more than 10 lines
- a class should not have more than 3 data variables
- limit the variable scope as much as possible
- make your function/variable/class as clear as possible
- for Python, refere to PEP8 coding style
- a python module should contains as least the unittest class.
- a python module should be auto-testable
- do not make import ouside of the global scope
- do not use "from x import *"
- do not use mutable as default parameter

### unittest

This is a template of unittest

```python
import unittest

# this module shows how to structure tests

def foo(x, y):
    # return the sum of x and y
    return x+y

class TestClass(unittest.TestCase):
    def test_foo(self):
        self.assertEqual(foo(1,2), 3)

if __name__ == "__main__":
    unittest.main()
```