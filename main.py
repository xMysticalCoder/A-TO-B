import os
password = os.environ['password']

from scratch2py import Scratch2Py
import scratchencoder
encoder = scratchencoder.Encoder()
s2py = Scratch2Py('xMysticalCoder', password)
cloudproject = s2py.scratchConnect('604133625')
while True:
  cloudproject = s2py.scratchConnect('604133625')
  print("Connected to A")
  sb = cloudproject.readCloudVar('var')
  print("Got A's variables")
  cloudproject = s2py.scratchConnect('604142511')
  print("Switched to B")
  cloudproject.setCloudVar("var", str(sb))
  print("Set B's variable")


