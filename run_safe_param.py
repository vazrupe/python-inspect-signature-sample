from utils import *


# Sample 1
print('## Run Sample 1 ##')


def sample(a, b, *args, c, **kwargs):
    print('a', a)
    print('b', b)
    print('c', c)
    print('args', args)
    print('kwargs', kwargs)

safe_sample = safe_param(sample)

print('+ sample')
param_info(sample)
print('\n+ safe_sample')
param_info(safe_sample)

try:
    print('+ safe_sample')
    safe_sample(1, 2, 3, 4, 5, 6, 7, d=10)
    print('\n+ sample')
    sample(1, 2, 3, 4, 5, 6, 7, d=10)
except Exception as e:
    print(e)


# Sample 2
print('\n\n## Run Sample 2 ##')


def sample2(a, b, *, c):
    print('a', a)
    print('b', b)
    print('c', c)

safe_sample2 = safe_param(sample2)

try:
    print('+ safe_sample2')
    safe_sample2(1, 2, 3, 4, 5, 6, 7, d=10)
    print('\n+ sample2')
    sample2(1, 2, 3, 4, 5, 6, 7, d=10)
except Exception as e:
    print(e)


# Sample 3
print('\n\n## Run Sample 3 ##')


@safe_param2('is default')
def sample3(a, b, *args, c, **kwargs):
    print('a', a)
    print('b', b)
    print('c', c)
    print('args', args)
    print('kwargs', kwargs)

print('+ sample3')
sample3(1, 2, 3, 4, 5, 6, 7, d=10)
