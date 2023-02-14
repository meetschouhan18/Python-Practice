import requests

#get
#r = requests.get('https://facebook.com')   #requests to get data from specified url
#print(r.content)     #it prints full html code of the url mentioned(fb in our case)
#commented bcz its too large
#print(r.status_code)   #prints 200 , which is issued by server
#status code are issued by server in response to a client's request made to the server

s = requests.get('https://httpbin.org/get')
print(s.headers['Server'])    #it prints specified header i.e. Server from the url mentioned
print(s.headers['Content-Type'])
response = s.json()    #json is header value of content type,and using requests library we can access header value
print(response)
payload = {'username':'administrator','password':'password'}   #we created a dictionary
r = requests.get('https://httpbin.org/get', params=payload)      #we uploaded our dictionar as argument on site
print(r.text)     #prints same as .content in more text then code

#post
payload = {'username':'administrator','password':'password'}   #we created a dictionary
r = requests.post('https://httpbin.org/post',data=payload)   #opposite of get, as post is used to send data to the specified url
print(r.text)

#redirect
r = requests.post('https://www.github.com')
print(r.history)    #history contains list of all response object on site to perform redirect
print(r.status_code)
r = requests.post('https://www.github.com',allow_redirects=False)   #we cancelled redirecting
print(r.history)     #prints nothing since no redirecting occurs
print(r.status_code)    #prints 301 since we are stuck on this response since it wannts to redirect us

# practise problems
# 1.

page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
print(page.text[:150]) #text function converts whole data into string
print(page.url)
print('-----------------')
# but it is very difficult to remember the parameters present in the url
# which is rel_rhy=funny in this case
# generally they are even more complicated
# thus we use a method to create the parameter
kval_pairs = {'rel_rhy': 'funny'}
page = requests.get('https://api.datamuse.com/words', params=kval_pairs)
print(page.text[:150])
print(page.url)
# we have just given base part, perimeter is given through dictionary, and perimeter is created in url


# 2.
def get_rhymes(word):
  baseurl = 'https://api.datamuse.com/words'
  parameter_dic = {}
  parameter_dic['rel_rhy'] = word
  parameter_dic['max'] = '3' # we add this to get max of 3 output
  resp = requests.get(baseurl, params=parameter_dic)
  word_ds = resp.json()
  print(word_ds)
  print('--------------')
  return [d['word'] for d in word_ds]
print(get_rhymes('funny'))