# -*- coding: utf-8 -*-

def hey(b):
    """Address a teenager and get his response.
    
    Returns:
    'Sure.' when passed a question,
    'Whoa, chill out!' on all uppercase input,
    'Fine. Be that way!' on whitespace-only input,
    'Whatever.' with anything else.
    """
    if b[-1] == '?':
        return 'Sure.'
    elif b == b.upper:
        return 'Whoa, chill out!'
    elif b == '':
        return 'Fine. be thath way!'
    else:
        return 'Whatever'
        
        
        
#------------------------------------------------------------------------------
        
a = input('Du: ')
x = str(a)
x = x.strip()
print (hey(x))