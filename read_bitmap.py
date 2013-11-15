import numpy as np
from PIL import Image

i = Image.open("cross.png")
data = np.asarray(i)
data = data/255
vals = []
for i in range(0, data.shape[0]):
	out = data[:, -i]
	val = 0
	for i, num in enumerate(out):
		if num > 0:
			val += 2**i	
	vals.append(val)

for i, val in enumerate(vals):
	print 'load', i, val
