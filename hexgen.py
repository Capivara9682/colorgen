from PIL import Image as img
import random
import os
print("color generator")
hexcodes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E', 'F']
outputhex = ''
var1 = ''
for i in range(6):
    rdn_thingy = random.choice(hexcodes)
    outputhex += rdn_thingy
    if len(outputhex) == 2 and len(outputhex) < 4:
        var1 = outputhex
    elif len(outputhex) == 4 and len(outputhex) < 6:
        var2 = outputhex[2:]
    if len(outputhex) == 6:
        var3 = outputhex[4:]
print('#' + outputhex)
outputimg = img.new('RGB', (100, 100), color=(int(str(var1), 16), int(str(var2), 16), int(str(var3), 16)))
outputimg.save(outputhex + '.png')
os.system('pause')