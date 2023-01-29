import requests
r = requests.get('https://api.github.com/events')

#.get function automatically decode data
print(r.encoding)
#tells us which encoding is applied on data

r.encoding = 'ISO-8859-1'
print(r.encoding)
#encoding changed
result = requests.get('https://api.github.com/events',stream=True)

#raw is uesd in rare cases when we actually want to get these socket responses
print(result.raw)
# it created the actual http response object at this memory address

print(result.raw.read(15))
#we are reading response object of first 15 bytes
