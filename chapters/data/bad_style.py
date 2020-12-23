x = {  'a':37,'b':42,
'c':927}
very_long_variable_name = {'field': 1,
                        'is_debug': True}
this=True

if very_long_variable_name is not None and very_long_variable_name["field"] > 0 or very_long_variable_name['is_debug']:
 z = 'hello '+'world'
else:
 world = 'world'
 a = 'hello {}'.format(world)
 f = rf'hello {world}'
if (this): y = 'hello ''world'#FIXME: https://github.com/python/black/issues/26
class Foo  (     object  ):
  def f    (self   ):
    return       37*-2
  def g(self, x,y=42):
      return y
# fmt: off
custom_formatting = [
    0,  1,  2,
    3,  4,  5
]
# fmt: on
regular_formatting = [
    0,  1,  2,
    3,  4,  5
]