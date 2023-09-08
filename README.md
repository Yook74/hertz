`pip install hertz`

```python
from hertz import *

foo = kHz(4)
foo += 1.2
print(foo) # prints 1.204 because if units aren't specified everything is done in MHz
print(foo.in_hz) # prints 1204000.0
foo += GHz('3')
print(foo.in_ghz) # prints 3.001204
```
