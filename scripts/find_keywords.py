
from os import listdir
from os import path as Path
import re

path = "./"

mdFileNames = [ f for f in listdir(path) if Path.isfile(Path.join(path,f)) and f.endswith(".md")]

print("Number of .md files found:", len(mdFileNames))

def build_keywords(keywords):
    str = '["'
    
    for keyword in keywords:
        str += keyword.strip() + '","'
        
    str = str[:-2]
    str += "]"
    
    return str 

def read_files(file):
    f = open(file,"r",encoding='utf-8')
    text = f.read()
    pattern = re.compile("(?:^#+\s)(.*)",flags=re.M)
    headers = re.findall(pattern,text)            
    pattern_keywords = re.compile(r"(-{3}[\n|\w\W]+keywords:\s)(?:.*|)(\s-{3})",flags=re.M)
    keywords = build_keywords(headers)
    newOutput = re.sub(pattern_keywords,r"\1"+keywords+"\n---",text)
    
    f.close()  
    print(newOutput)
    f = open(file,"w",encoding='utf-8')
    f.writelines(newOutput)
    f.close()
    

for f in mdFileNames:
    read_files(f)


