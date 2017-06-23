import urllib
import xml.etree.ElementTree as ET

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'


# address = raw_input('Enter location: ')
address = 'http://python-data.dr-chuck.net/comments_42.xml'
# if len(address) < 1 : break

# url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
url = address
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
print data
tree = ET.fromstring(data)


# results = tree.findall('commentinfo')
# nums = results.find('comments').find('comment').find('count').text
counts = tree.findall('./counts/count')
# lng = results[0].find('geometry').find('location').find('lng').text
# location = results[0].find('formatted_address').text
print counts
# print 'nums: ',nums
# print location