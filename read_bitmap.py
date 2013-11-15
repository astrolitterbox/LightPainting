import numpy as np
from PIL import Image
import sys

try:
	imageName = sys.argv[1]
except IndexError:
	print 'Pass image name as an argument!'
	print 'Debilai tu, priekurti!!1!'
	exit() 
i = Image.open(imageName)
data = np.asarray(i)
print data
data = data/255
vals = []
for i in range(0, data.shape[0]):
	out = data[:, -i]
	val = 0
	for i, num in enumerate(out):
		if num > 0:
			val += 2**i	
	vals.append(hex(val))

for i, val in enumerate(vals):
	print 'load', i, val
