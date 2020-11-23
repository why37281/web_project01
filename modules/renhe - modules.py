
def rgb2hex(rgb):
    strs = '#'
    for i in rgb:
        num = int(i)
        strs += str(hex(num))[-2:].replace('x', '0').upper()
    return strs
def hex2rgb(hex):
    return list(int(hex[i:i+2], 16) for i in (1, 3, 5))
print(rgb2hex((199, 210, 255)))
