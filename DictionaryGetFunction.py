count = {}
names = ['meet','rohan','billa','pok','gd','meet','rohan','meet','billa','meet','pok','rohan','gd']
for name in names:
    count[name] = count.get(name,0) + 1
print(count)

#get function check name in count
#if name is present in count then its value is returned
#if name is not present in count then default value mentioned i.e. 0 is returned
