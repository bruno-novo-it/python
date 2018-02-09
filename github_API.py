#import requests

#user = "cs-bruno-novo"
#pass = "Cisco@18"

#r = requests.get('https://api.github.com/user', auth=('cs-bruno-novo', 'Cisco@18'))

#print("O status code é : %i" % r.status_code)

#print("O tipo de codificação é: %s" % r.headers['content-type'])

#print("O tipo de Encoding: %s" % r.encoding)

#print(r.text)

#print(r.json())

from github import Github

gh = Github('cs-bruno-novo', 'Cisco@18')

usr = gh.get_user()

print("Data de criação: ", usr.created_at)

# Print all Repos from a User
count = 0
for repo in gh.get_user().get_repos():
    print(repo.name)
    count+=1

print("Total de repositórios é: %i" % count)
