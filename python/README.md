## Intro

I created 4 different compute functions and analyzed their performance. They all satisfy the unit test.

## Unit Test


```python
!python -m unittest test.hamming_test
```

    ................
    ----------------------------------------------------------------------
    Ran 16 tests in 0.002s
    
    OK



```python
!python -m unittest test.hamming_test_compute_with_zip
```

    ................
    ----------------------------------------------------------------------
    Ran 16 tests in 0.005s
    
    OK



```python
!python -m unittest test.hamming_test_compute_with_numpy
```

    ................
    ----------------------------------------------------------------------
    Ran 16 tests in 0.003s
    
    OK



```python
!python -m unittest test.hamming_test_regular_for_loop
```

    ................
    ----------------------------------------------------------------------
    Ran 16 tests in 0.005s
    
    OK


## Performance Test


```python
import hamming

TAG = 'TAG' * 500000
GAT = 'GAT'* 500000

```


```python
# Compute using a Generator and izip from itertools
%timeit hamming.compute(TAG, GAT)
```

    10 loops, best of 3: 191 ms per loop



```python
# Compute using a Generator and the built-in zip (Python 2.7)
%timeit hamming.compute_with_zip(TAG, GAT)
```

    1 loop, best of 3: 313 ms per loop



```python
# Compute using a regular for loop function
%timeit hamming.compute_with_for_loop(TAG, GAT)
```

    1 loop, best of 3: 286 ms per loop



```python
# Compute using numpy arrays
%timeit hamming.compute_with_numpy(TAG, GAT)
```

    1 loop, best of 3: 230 ms per loop
    
## Conclusion
 - Using the generator performed better than using a regular for loop.
 - Use of izip gave almost an order of magnitude better performance.
    

