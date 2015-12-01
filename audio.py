def play(name, length=None):
  # For MacOSX
  import os
  if length == None:
    os.system("afplay %s &" % name)
  else:
    os.system("afplay %s TIME=%d &" % (name, length))

