import _dictdraw, sys

d = {'arya': 666, 'john': 858, 'snow':1, 'alive': 2, 'dead':3}
surface = _dictdraw.draw_dictionary(d)
surface.write_to_png(sys.argv[1])
