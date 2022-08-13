import re
mystr='''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: 72353-8281
Fax: 72353-8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9727
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
aiiiii
aii
ai
ai
aiii
aiiii'''


# patt=re.compile(r'www.northamerica.tata.com')
# patt=re.compile(r'.www')
# patt=re.compile(r'^Tata')
# patt=re.compile(r'^Email')
# patt=re.compile(r'fass$')
# patt=re.compile(r'View$')
# patt=re.compile(r'Email{1}')
# patt=re.compile(r'ai{2}')
# patt=re.compile(r'(aii){1}')
# patt=re.compile(r'ai+')


# special sequence
# patt = re.compile(r'Fax\b')
# patt = re.compile(r'27\b')
# patt = re.compile(r'\d')
# patt = re.compile(r'\d{5}-\d{4}')






matches=patt.finditer(mystr)

for match in matches:
    print(match)
