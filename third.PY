from urllib.request import urlopen
import zipfile
import os

directory_to_extract_to = "directory.22"  
arch_file = "/Users/vladimirskobcov/Desktop/11 lab/python/tiff-4.2.0.zip"

try:
    os.makedirs(directory_to_extract_to)
except OSError:
    print ("Create directory: %s, failed, directory exists" % directory_to_extract_to)
else:
    print ("Directory: %s, was created successfully" % directory_to_extract_to)

with zipfile.ZipFile('tiff-4.2.0.zip', 'r') as zip_file:
    zip_file.extractall(directory_to_extract_to)

import hashlib

txt_files=[]
walks = []
var_count = 0
target_hash = "4636f9ae9fef12ebd56cd39586d33cfb"
tmp_data = " "
tmp_walk = " "

for r, d, f in os.walk(directory_to_extract_to):
    for file in f:
        walks.append(os.path.join(r, file))
        txt_files.append(file)       
        target_file = open(walks[var_count], 'rb').read()
        target_file_data = hashlib.md5(target_file).hexdigest()
        if file.endswith('.txt'):    
            print(txt_files[var_count] + ": " + target_file_data)
        if target_file_data == target_hash:
            tmp_data = open(walks[var_count]).read()
            tmp_walk = walks[var_count]
        var_count += 1 

print(end="\n" + tmp_walk)
print(end="\n" + tmp_data)

import pip._vendor.requests
import re


r = pip._vendor.requests.get(tmp_data)
result_dct ={} 

counter=0

lines = re.findall(r'<div class="Table-module_row__3TH83">.*?</div>.*?</div>.*?</div>.*?</div>.*?</div>', r.text)
for line in lines:
    if counter == 0:
        headers = re.sub(r"([^>А-я<]+)", " " , line)
        headers = re.findall(r'([А-я][^.<>]+)', headers)
    if counter > 0:
        temp = re.sub(r'<div.*?>', ';', line)
        temp = re.sub(r"\(.*?\)", ';', temp)
        temp = re.sub(r'<\/div*?>|<\/span*?>|<span style="color:#5C5E62;font-|size:10px">', "", temp)
        temp = re.sub(r"['; *]", ' ', temp)
        tmp_split = re.findall(r"([0-9А-я_][^' ]+|0|_|[0-9])", temp)
        if len(tmp_split) > 5:
            tmp_split[0] = tmp_split[0] + ' ' + tmp_split[1]
            for i in range(len(tmp_split)-2):
                tmp_split[i+1] = tmp_split[i+2] 
        
            if len(tmp_split) > 6:
                tmp_split[0] = tmp_split[0] + ' ' + tmp_split[1] + ' ' + tmp_split[2]
                for i in range(len(tmp_split)-2):
                    tmp_split[i+1] = tmp_split[i+2] 
                 
            x = len(tmp_split) -1
            tmp_split = tmp_split[:x]



        country_name = re.sub('(\xa0|</strong>)', '', tmp_split[0])
        col1_val = re.sub('(\xa0|</strong>)', '', tmp_split[1])
        col2_val = re.sub('(\xa0|</strong>)', '', tmp_split[2])
        col3_val = re.sub('(\xa0|</strong>)', '', tmp_split[3])
        if '_' == tmp_split[4]:
            col4_val = re.sub('_', '-1', tmp_split[4])
        else: 
            col4_val = re.sub('(\xa0|</strong>)', '', tmp_split[4])     
        
        from collections import defaultdict
        result_dct.setdefault(country_name, {})[headers[0]] = int(col1_val)
        result_dct.setdefault(country_name, {})[headers[1]] = int(col2_val)
        result_dct.setdefault(country_name, {})[headers[2]] = int(col3_val)
        result_dct.setdefault(country_name, {})[headers[3]] = int(col4_val)
        print(result_dct, end="\n")
        print(end="\n")
    counter+=1


output = open('data.csv', 'w')
for key in result_dct:
    s = str(key) 
    s += ':' 
    s += str(result_dct[key])
    s += '\n'

    output.write(s)

output.close()

ch_count = 0 
target_country = input("Введите название страны: ")
for key in result_dct:
    if target_country == key:
        value = result_dct[target_country]
        print (value)
        ch_count+=1

if ch_count == 0:
    print ("Undefined name of country: ", target_country)
exit()