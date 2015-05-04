import sys
import re

from . import rational


def run(filename):
    with open(filename, 'r') as f:
        numbers_str = f.readline().strip()
    regexp = r'^(?P<a1>-?\d+)/(?P<b1>\d+) *(?P<a2>-?\d+)/(?P<b2>\d+)$'
    assert re.match(regexp, numbers_str), 'Wrong format.'
    numbers = re.match(regexp, numbers_str).groupdict()
    r1 = rational.Rational(int(numbers['a1']), int(numbers['b1']))
    r2 = rational.Rational(int(numbers['a2']), int(numbers['b2']))
    print '{} + {} = {}'.format(str(r1), str(r2), str(r1 + r2))
    print '{} - {} = {}'.format(str(r1), str(r2), str(r1 - r2))
    print '{} * {} = {}'.format(str(r1), str(r2), str(r1*r2))
    try:
        print '{} / {} = {}'.format(str(r1), str(r2), str(r1/r2))
    except ZeroDivisionError:
        print '{} / {} = inf'.format(str(r1), str(r2))




























if __name__ == '__main__':
    assert len(sys.argv) > 1, 'Set inpul filename'
    filename = sys.argv[1]
    run(filename)
