import jmespath

d = {'foo': {'bar': 'baz'}}
print(jmespath.search('foo.bar', d))


dl = {'foo':{'bar':[{'name':'one'},{'name':'two'}]}}
print(jmespath.search('foo.bar[*].name',dl))

source_2 = ["a", "b", "c", "d", "e", "f"]
index_result = jmespath.search("[1]",source_2)
print(repr(index_result))