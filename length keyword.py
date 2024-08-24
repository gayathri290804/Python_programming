#length keyword argument
def name(**a):
  for value,key in a.items():
    print("%s==%s" % (value , key))
name(x="hey",y="hi",z="hello")     
