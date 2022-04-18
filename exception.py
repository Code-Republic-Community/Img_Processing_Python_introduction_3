class NewException(Exception):
    pass


def foo(a):
    assert a > 10
    #raise NewException()
    return 8

try:
    foo(8)
except NewException:
    print('Catched ...')
finally:
    print('In any case')
