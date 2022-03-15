# PiCalcTest
Pi calculation performance test for micropython and circuitpython.

The performance of different processors is compared by calculating the Pi of different bits.

## Test program
- [pi_micropython.py](pi_micropython.py)  
- [pi_circuitpython.py](pi_circuitpython.py)


## Result

- [2019, micropython 1.9.4](https://github.com/shaoziyang/micropython_benchmarks/tree/master/1.9.4-479)
- [2022-03, micropython 1.18 / circuitpython 7.2.0](2022-03.md)

### Please Note

1. In order to reduce the influence of other factors on the calculation, the hardware should be reset before calculation.
2. It is normal for the calculation time to fluctuate in a small range.
