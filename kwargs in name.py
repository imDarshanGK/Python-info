def func(name, **kwds):
  return 'name' in kwds
print(func(1, **{'name': 2}))
