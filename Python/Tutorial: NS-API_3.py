import requests

auth_details = ('niels.boot@student.hu.nl', 'gIbh4pov7EJogdCx2XZwlvUczv0bvqnPUpvAuVvv0eXoipu6B0hH9g')
api_url = 'http://webservices.ns.nl/ns-api-avt?station=ut'

response = requests.get(api_url, auth=auth_details)