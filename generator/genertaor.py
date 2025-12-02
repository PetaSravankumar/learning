def gener():
    yield 1
    yield 2
    yield 3
res=gener()
print(res)
print(next(res))
print(next(res))
print(next(res))
