import dis

def add(a):
    a = a + 1
    return a

print(dis.dis(add))
