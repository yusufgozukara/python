# Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.

# "hello"     -->  "hll"
# "codewars"  -->  "cdwrs"
# "goodbye"   -->  "gdby"
# "HELLO"     -->  "HELLO"


# def shortcut( s ):
#     return s.replace('a','').replace('e','').replace('i','').replace('u','').replace('o','')


def shortcut( s ):
    for i in ["a","e","i","o","u"]:
        if i in s:
            s = s.replace(i, '')
    return(s)

print(shortcut('hello'))