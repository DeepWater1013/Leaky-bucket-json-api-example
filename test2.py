# from urllib2 import Request, urlopen
import urllib.request
import requests
values = """
  {
    "ImageGalleryID": 45690021,
    "ImageGalleryFile": "nostrud ut qui eiusmod",
    "ImageGalleryCaption": "do in consectetur",
    "ImageGallerySorting": -51969841
  }
"""

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'SecureURL': '',
  'PrivateKey': '',
  'Token': ''
}
response_body = requests.put('https://apirest.3dcart.com/3dCartWebAPI/v2/Products/{catalogid}/Images/{imagegalleryid}', data=values, headers=headers)
# request.get_method = lambda: 'PUT'
# reqs = requests.put('https://apirest.3dcart.com/3dCartWebAPI/v2/Products', data=json.dumps(result), headers=headers)

print(response_body)