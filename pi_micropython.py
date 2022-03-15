import gc
from utime import ticks_ms, ticks_diff
import machine
import os

def pi(places=100):
    # 3 + 3*(1/24) + 3*(1/24)*(9/80) + 3*(1/24)*(9/80)*(25/168)
    # The numerators 1, 9, 25, ... are given by (2x + 1) ^ 2
    # The denominators 24, 80, 168 are given by (16x^2 -24x + 8)
    extra = 8
    one = 10 ** (places+extra)
    t, c, n, na, d, da = 3*one, 3*one, 1, 0, 0, 24

    while t > 1:
        n, na, d, da = n+na, na+8, d+da, da+32
        t = t * n // d
        c += t
    return c // (10 ** extra)

def pi_t(n=1000):
    gc.collect()
    t1 = ticks_ms()
    pi(n)
    t2 = ticks_ms()
    print('  ', ticks_diff(t2, t1), 'ms')


r = os.uname()
print('\n\n')
print('Pi calculation performance test')
print('===============================')
print('chip:', r.sysname)
print('ver: ', r.version)
try:
    print('Freq:', machine.freq())
except:
    print('Freq: unknow')
print('Ram: ', gc.mem_free() + gc.mem_alloc())
for i in (100, 500, 1000, 2000, 5000, 10000, 100000):
    try:
        print('\nCalc {} bits pi'.format(i))
        pi_t(i)
    except:
        print('Calc error!')
