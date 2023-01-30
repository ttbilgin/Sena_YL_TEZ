import re
from tokenize import tokenize, ENCODING, NEWLINE, ENDMARKER
from io import BytesIO
import json

KEYWORDS = ("and", "as","abs", "assert", "await", "async", "append",
            "break","bin","bool",
            "class", "continue", "clear",",count","capitalize","complex",
            "def", "del","dict",
            "elif", "else","exec","end",
            "finally","False" "for", "from","find","float","functools","filter",
            "get","global",
            "hex", 
            "nonlocal",
            "if", "import", "in", "is","input","index","isdigit","insert","int","isupper","islower","items",
            "join",
            "keys",
            "lambda", "len","lower","list",
            "not", "None",
            "map",
            "or",
            "pass", "print",
            "raise", "return", "range","round","replace","rfind","reduce",
            "str","split",
            "True","tuple","time","type",
            "upper",
            "values",
            "while", "with",
            "yield",  
            )

UPPER_KEYWORDS = [x.upper() for x in KEYWORDS]
print(UPPER_KEYWORDS)

TOKENS = (
    (r'[a-zA-Z_]\w*', 'VAR'),
    (r'0', 'INT'),
    (r'[-+]?\d+[eE][-+]?\d+[jJ]', 'FLOAT_EXPONANT_COMPLEX'),
    (r'[-+]?\d+.\d?[eE][-+]?\d+[jJ]', 'FLOAT_EXPONANT_COMPLEX'),
    (r'[-+]?\d?.\d+[eE][-+]?\d+[jJ]', 'FLOAT_EXPONANT_COMPLEX'),
    (r'\d+[eE][-+]?\d*', 'FLOAT_EXPONANT'),
    (r'\d+\.\d*[eE][-+]?\d*', 'FLOAT_EXPONANT'),
    (r'\.\d+[eE][-+]?\d*', 'FLOAT_EXPONANT'),
    (r'\d*\.\d+[jJ]', 'COMPLEX'),
    (r'\d+\.[jJ]', 'COMPLEX'),
    (r'\d+[jJ]', 'COMPLEX'),
    (r'\d+\.', 'FLOAT'),
    (r'\d*[_\d]*\.[_\d]+[lL]?', 'FLOAT'),
    (r'\d+[_\d]+\.[_\d]*[lL]?', 'FLOAT'),
    (r'\.', 'DOT'),
    (r'[1-9]+[_\d]*[lL]', 'LONG'),
    (r'[1-9]+[_\d]*', 'INT'),
    (r'0[xX][\d_a-fA-F]+[lL]?', 'HEXA'),
    (r'(0[oO][0-7]+)|(0[0-7_]*)[lL]?', 'OCTA'),
    (r'0[bB][01_]+[lL]?', 'BINARY'),
    (r'\(', 'LEFT_PARENTHESIS'),
    (r'\)', 'RIGHT_PARENTHESIS'),
    (r':', 'COLON'),
    (r',', 'COMMA'),
    (r';', 'SEMICOLON'),
    (r'@', 'AT'),
    (r'\+', 'PLUS'),
    (r'-', 'MINUS'),
    (r'\*', 'STAR'),
    (r'/', 'SLASH'),
    (r'\|', 'VBAR'),
    (r'&', 'AMPER'),
    (r'@', 'AT'),
    (r'<', 'LESS'),
    (r'>', 'GREATER'),
    (r'=', 'EQUAL'),
    (r'%', 'PERCENT'),
    (r'\[', 'LEFT_SQUARE_BRACKET'),
    (r'\]', 'RIGHT_SQUARE_BRACKET'),
    (r'\{', 'LEFT_BRACKET'),
    (r'\}', 'RIGHT_BRACKET'),
    (r'`', 'BACKQUOTE'),
    (r'==', 'EQUAL_EQUAL'),
    (r'<>', 'NOT_EQUAL'),
    (r'!=', 'NOT_EQUAL'),
    (r'<=', 'LESS_EQUAL'),
    (r'>=', 'GREATER_EQUAL'),
    (r'~', 'TILDE'),
    (r'\^', 'CIRCUMFLEX'),
    (r'<<', 'LEFT_SHIFT'),
    (r'>>', 'RIGHT_SHIFT'),
    (r'\*\*', 'DOUBLE_STAR'),
    (r'\+=', 'PLUS_EQUAL'),
    (r'-=', 'MINUS_EQUAL'),
    (r'@=', 'AT_EQUAL'),
    (r'\*=', 'STAR_EQUAL'),
    (r'/=', 'SLASH_EQUAL'),
    (r'%=', 'PERCENT_EQUAL'),
    (r'&=', 'AMPER_EQUAL'),
    (r'\|=', 'VBAR_EQUAL'),
    (r'\^=', 'CIRCUMFLEX_EQUAL'),
    (r'<<=', 'LEFT_SHIFT_EQUAL'),
    (r'>>=', 'RIGHT_SHIFT_EQUAL'),
    (r'\.\.\.', 'ELLIPSIS'),
    (r'->', 'RIGHT_ARROW'),
    (r'\*\*=', 'DOUBLE_STAR_EQUAL'),
    (r'//', 'DOUBLE_SLASH'),
    (r'//=', 'DOUBLE_SLASH_EQUAL'),
    (r'\n', 'ENDL'),
    (r'\t', 'TABSPACE'),
    (r'\r\n', 'ENDL'),
    (r'#.*', 'COMMENT'),
    (r'(\s|\\\n|\\\r\n)+', 'SPACE'),
    (r'["\'](.|\n|\r)*["\']', 'STRING'),
    (r'[uU]["\'](.|\n|\r)*["\']', 'UNICODE_STRING'),
    (r'[fF]["\'](.|\n|\r)*["\']', 'INTERPOLATED_STRING'),
    (r'[rR]["\'](.|\n|\r)*["\']', 'RAW_STRING'),
    (r'[bB]["\'](.|\n|\r)*["\']', 'BINARY_STRING'),
    (r'[uU][rR]["\'](.|\n|\r)*["\']', 'UNICODE_RAW_STRING'),
    (r'[bB][rR]["\'](.|\n|\r)*["\']', 'BINARY_RAW_STRING'),
    (r'[fF][rR]["\'](.|\n|\r)*["\']', 'INTERPOLATED_RAW_STRING'),
    (r'[rR][fF]["\'](.|\n|\r)*["\']', 'INTERPOLATED_RAW_STRING'),
    (r'±','SUM_INTENDED'),
)

TOKENS = [(re.compile('^' + x[0] + '$'), x[1]) for x in TOKENS]

def more_tokenize(sequence, print_function=False):
    return list(tokenize_generator(sequence))

def tokenize_current_keywords(print_function=False):
    if print_function is True:
        return [x for x in KEYWORDS if x != "print"]
    else:
        return KEYWORDS

def tokenize_generator(sequence):
    print(sequence)
    current_keywords = tokenize_current_keywords()
    for item in sequence:
        if item in current_keywords:
            yield [item.upper(), item]
            continue
        
        for candidate, token_name in TOKENS:
            if candidate.match(item):
                yield [token_name, item]
                break
        else:
           # raise Exception(
           #     "Can't find a matching token for this item: '%s'" % item)
            raise Exception(
                "Can't find a matching token for this item: '%s'" % item)
    # yield ('ENDMARKER', '')
    # yield


def call_moretokenizer(errorline):
    g = tokenize(BytesIO(errorline.encode('utf-8')).readline)
    tokenarray = []
    for toknum, tokval, _, _, _ in g:
        if toknum not in [ENCODING, NEWLINE, ENDMARKER] and tokval != '':
            tokenarray.append(tokval)
    more_tkn = more_tokenize(tokenarray)
    tkn_named_entity = []
    for tkn in more_tkn:
        tkn_named_entity.append(tkn[0])
        
    return tkn_named_entity


errorcode="""
def say_hello():
	print()
say_hello()
if 
for
"""

deneme=call_moretokenizer(errorcode)

print(deneme)

list1=[]
for i in TOKENS:
    list1.append(i[1])
print(list1)

keywords_tokens_list=list1+UPPER_KEYWORDS
print(keywords_tokens_list)

list_ind= []
for item in deneme:
    index=keywords_tokens_list.index(item)
    list_ind.append(index)
print(list_ind)