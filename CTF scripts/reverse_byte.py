f = open('flag.png', 'rb')
g = open('reverse.png', 'wb')
g.write(f.read()[::-1])
print("Done!")
