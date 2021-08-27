#  nargs 
import argparse
#ver 1 can be overwritten
# class StartAction(argparse.Action):
#     def __init__(self, nargs=0, **kw):
#         super().__init__(nargs=nargs, **kw)
#     def __call__(self, parser, namespace, values, option_string=None):
#         print ("Hello")

# prevent overwriting
class StartAction(argparse.Action):
    def __init__(self, nargs=0, **kw):
        if nargs != 0:
            raise ValueError('nargs for StartAction must be 0; it is '
                             'just a flag.')
        super().__init__(nargs=nargs, **kw)
    def __call__(self, parser, namespace, values, option_string=None):
        print ("Hello")

start = argparse.ArgumentParser()
start.add_argument('-s', '--start', action=StartAction)
# nargs=0 in init ver 1 can be overwritten with:
# start.add_argument('-s', '--start', nargs=1, action=StartAction)
args = start.parse_args()




