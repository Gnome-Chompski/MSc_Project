import urllib3, facebook, requests

token = 'EAACEdEose0cBANOqbZBwtQrrYU1EENjGGw2rmagTXCjNRLZB2FZAIZAufYxd7BZAmBCQKovH50bX0lZAt96qhH6AoHb4jYtPvPtkOGfBDgrDEZCyNGJ2z5lvm4gCB5aMHlPVZAZBeakZCnEantsFR181aoApBy5W4p6I3RjHDNvTybJyXX9ZBwKZABwnZBZBXtaoI9kZBqX3vAhatyxegZDZD'

graph = facebook.GraphAPI(access_token=token, version = 2.7)
profile = graph.get_object("100001541961253", fields='name,location,age_range,first_name,address,birthday,link,last_name,email,gender')
#connections = graph.get_connections("me", connection_name='posts')
print(profile)
