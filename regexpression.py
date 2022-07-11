import re

PhoneNoMatch = re.compile(r'\d{3}-\d{3}-\d{4}')
message = 'Please call at 412-333-5643 today by noon. 412-333-5699 is my office'
#match_no = PhoneNoMatch.search('Please call at 412-333-5643 today by noon. 412-333-5699 is my office')
#print('Phone number found: ' + match_no.group())

find_no = PhoneNoMatch.findall(message)
for value in find_no:
    print('Phone number found: ' + value)

match_phone = re.compile(r'(\d{3})-(\d{3}-\d{4})')
phoneNo = match_phone.search('Please call at 412-333-5643 today by noon.')
print(phoneNo.group(1))
print(phoneNo.group(2))
print(phoneNo.group(0))
print(phoneNo.group())
area_code, number = phoneNo.groups()
print(f'Area code is {area_code} and main number is {number}')

#matching multiple groups with Pipe
multipleRegex = re.compile(r'Olamide|Similoluwa Ilori')
group1 = multipleRegex.search('My name is Olamide and my sister\'s name is Similoluwa')
print(group1.group())
westRegex = re.compile(r'West(ham|hill|coast|wind)')
group1 = westRegex.search('I live on Westhill beside the Westcoast after Westwind. I support Westham football club')
print(group1.group())

#optional matching with the Question Mark
batRegex = re.compile(r'Bat(wo)?man')
output = batRegex.search('I am not a Batman')
print(output.group())

#substituting strings with the sub() method
namesRegex = re.compile(r'\w+ Office', re.I)
outputRegex = namesRegex.sub('home', 'I have worked from the office the last four days. Tomorrow I will be at the office again.')
print(outputRegex)

agentnamesRegex = re.compile(r'Agent (\w)(\w)\w*')
output  = agentnamesRegex.sub(r'\1\2********', 'Agent Olamide informed Agent Allen that Agent Joseph & Agent Jamal are double agents.')
print(output)
removespaceRegex = re.compile(r'\s+(\w+)(!)?(!+)?', re.I)
#removespaceRegex = re.compile(r'(\w+)\s+', re.I)
outputReg  = removespaceRegex.sub(r' \1\2', 'Find common typos such as multiple          spaces  between  words,      accidentally accidentally repeated words, \
                                    or multiple exclamation        marks at the end of sentences. Those are annoying!!')
print(outputReg)

atRegex = re.compile(r'.*at')
output = atRegex.findall('Flat')
print(output)
