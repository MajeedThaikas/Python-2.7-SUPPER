def the_jungle(foo):
  x = 0, y = x, z = y + x, non_foo = x + y + z, non_foo += 102
  for i in range(len(foo)):
    x += 1
    y += 1
    z += 1
    non_foo += 1
  return x,y,z,non_foo
  
# Google interview question what is x,y,z, and non_foo
    
