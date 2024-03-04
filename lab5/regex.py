import re
with open(r'C:\Users\Torekhan\Desktop\Git\py_repo\tsis5\row.txt','r',encoding='utf-8') as f:
    c = f.read()
    """Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s."""
    '''
    p = re.findall('ab*',c)
    print(p)
    '''
    """Write a Python program that matches a string that has an 'a' followed by two to three 'b'."""
    '''
    p = re.findall('ab{2,3}',c)
    print(p)
    '''
    """Write a Python program to find sequences of lowercase letters joined with a underscore."""
    '''
    p = re.findall('[a-z]+_[a-z]+',c)
    print(p)
    '''
    """Write a Python program to find the sequences of one upper case letter followed by lower case letters."""
    '''
    p = re.findall('[A-Z][a-z]+',c)
    print(p)
    '''
    """Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'."""
    ''''
    p = re.findall('a.*b',c)
    print(p)
    '''
    """Write a Python program to replace all occurrences of space, comma, or dot with a colon."""
    '''
    s = re.sub('[\s,.]',':',c)
    print(s)
    '''
    """Write a python program to convert snake case string to camel case string."""
    '''
    def s_to_c(m):
        return m.group(1)+m.group(2).title()
    s = re.sub('([a-z]+)_([a-z]+)',s_to_c,c)
    print(s)
    '''

    """Write a Python program to convert a given camel case string to snake case."""
    '''
    def c_to_s(m):
        return m.group(1)+'_'+m.group(2).lower()
    s = re.sub('([a-z]+)([A-Z][a-z]+)',c_to_s,c)
    print(s)
    '''
    """Write a Python program to split a string at uppercase letters."""
    '''
    str = "SplitTheStringByUppercaseLetters"
    s = re.split('[A-Z]',str)
    print(s)
    '''
    """Write a Python program to insert spaces between words starting with capital letters."""
    '''
    s = re.sub('(\w)([A-Z])',r'\1 \2',c)
    print(s)
    '''
