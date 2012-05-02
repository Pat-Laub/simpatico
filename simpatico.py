import sys
import os
import re

sswith = lambda x, y: x.strip().startswith(y)
sewith = lambda x, y: x.strip().endswith(y)

def check_all():
    files = [x for x in os.listdir(os.getcwd())
             if x.endswith('.c') or x.endswith('.h')]

    for f in files:
        print '%s:'%f
        check(f)
        print

def check(filename):
    errors = []

    lines = [x+'\n' for x in remove_comments_and_strings(filename).split('\n')]
    errors.extend(check_indents(lines))
    errors.extend(check_function_lengths_names(lines))
    errors.extend(check_line_lengths(lines))
    errors.extend(check_naming(lines))
    errors.extend(check_horiz_whitespace(lines))
    errors.extend(check_braces(lines))

    errors.sort()
    for n, err in errors:
        print '%4s: %s'%(n, err)

def check_braces(lines):
    errors = []

    for n, line in enumerate(lines):
        if sswith(line, '*') or sswith(line, '/*'):
            continue
        
        if (' while' in line or ' for' in line or ' do' in line
            or ' if' in line or ' else' in line or ' switch' in line):
            i = 0
            while '{' not in lines[n + i] and ';' not in lines[n + i]:
                i += 1
                line = lines[n + i]

            if '{' in line:
                lst = line.rsplit('{', 1)
                if lst[0][-1] != ' ':
                    errors.append((n+1, 'Braces Error (spacing)'))

        if 'else' in line:
            if not sswith(line, '}'):
                errors.append((n+1, 'Braces Error (else placement)'))
            else:
                if line.split('{')[0][-1] != ' ':
                    errors.append((n+1, 'Braces Error (spacing)'))

    return errors

def check_horiz_whitespace(lines):
    errors = []

    for n, line in enumerate(lines):
        if sswith(line, '*') or sswith(line, '/*'):
            continue
        
        for c in (',', ';'):
            if not check_char_spacing(line, c):
                errors.append((n+1, "Horizontal Whitespace Error (%s)"%c))

        for c in ('=', '+=', '-=', '/=', '*='):
            if not check_char_spacing(line, c, True):
                errors.append((n+1, "Horizontal Whitespace Error (%s)"%c))

    return errors

def check_char_spacing(line, c, before=False):
    if c == '=':
        line = line.replace('==', '')
        line = line.replace('!=', '')
        line = line.replace('+=', '')
        line = line.replace('-=', '')
        line = line.replace('/=', '')
        line = line.replace('*=', '')
        line = line.replace('<=', '')
        line = line.replace('>=', '')
        
    if c not in line:
        return True
    lst = line.split(c)

    for i, s in enumerate(lst):
        if (i and s[0] not in ' \n') or (before and i != len(lst)-1 and s[-1] != ' '):
            return False
    return True

def check_naming(lines):
    errors = []

    validTypes = ['int', 'char', 'size_t', 'pid_t', 'bool', 'long', 'short',
                  'float', 'double', 'long double', 'FILE']

    seenTypedef = False
    inTypedef = False
    
    for n, line in enumerate(lines):
        if 'typedef' in line:
            seenTypedef = True
        if '{' in line and seenTypedef:
            inTypedef = True
        if '}' in line and inTypedef:
            inTypedef = False
            seenTypedef = False
            t = line.rstrip().split()[-1].rstrip(';')
            validTypes.append(t)
            if t[0].islower():
                errors.append((n+1, 'Type Naming Error (%s)'%t))
    
    matchStr = r'(unsigned )?(%s) /*?(?P<var>[^ ;)(]*)'%'|'.join(validTypes)

    for n, line in enumerate(lines):
        if sswith(line, '*') or sswith(line, '/*'):
            continue
        
        match = re.search(matchStr, line)
        if match is not None:
            _, _, svs = line.partition(match.groups()[1])
            decs = [x for x in svs.split(',') if x.strip()]

            vs = [match.group('var')]
            if len(decs) > 1:
                for dec in decs:
                    m2 = re.search(matchStr, dec)
                    if m2 is None:
                        continue
                    vs.append(m2.group('var'))

            if line[0] != ' ':
                vs = vs[1:]

            vs = [x.strip('*,') for x in vs]
            vs = [x for x in vs if x]

            for v in vs:
                if v[0].isupper():
                    errors.append((n+1,"Variable Naming Error (%s)"%v))

    for n, line in enumerate(lines):
        if line.startswith('#define '):
            define = line.split()[1]
            for c in define:
                if c.islower():
                    errors.append((n+1, "#define Naming Error (%s)"%define))
                    break
    
    return errors

def check_line_lengths(lines):
    errors = []

    for n, line in enumerate(lines):
        if len(line) > 79:
            errors.append((n+1, 'Line Length Error (%s characters)'%len(line)))

    return errors

def check_indents(lines):
    errors = []
    
    indent = 0
    idc = ' '*4

    dbrackets = 0

    lineCont = False
    inCase = False
    
    for n, line in enumerate(lines):
        # skip lines with only whitespace or comments
        if not line.strip() or sswith(line, '/*'):
            continue

        #handle falling out of case without break
        if inCase and sswith(line, '}') and indent == caseIndent:
            inCase = False
        
        if inCase and sswith(line, 'case '):
            inCase = False
        # special case of closing brace needing to be one back
        # special case of line continuation (needing two further indents)
        # special case of case statements (need one further indent)
        reqindent = indent - sswith(line, '}') + lineCont*2 + inCase
        if ((not line.startswith(idc*reqindent)
             or line.startswith(idc*reqindent+' '))
             and not sswith(line, '*')):
            errors.append((n+1,
                           'Indentation error (expected %d, got %d)'%(
                               len(idc*reqindent), len(line) - len(line.lstrip()))))

        indent += count_char(line, '{') - count_char(line, '}')

        dbrackets += (count_char(line, '(') - count_char(line, ')'))
        lineCont = dbrackets > 0
        if not lineCont:
            dbrackets = 0

        if sswith(line, 'case ') or sswith(line, 'default:'):
            inCase = True
            caseIndent = indent
        if inCase and sswith(line, 'break;'):
            inCase = False

    return errors

  

def count_char(string, char):
    n = 0
    for c in string:
        if c == char:
            n += 1
    return n

def check_function_lengths_names(lines):
    errors = []

    inFunction = False
    curFunctiion = ''
    c = 0

    for n, line in enumerate(lines):
        if inFunction:
            c += 1
            if line.startswith('}'):
                inFunction = False

                if c > 50:
                    errors.append((n+1-c,
                                   'Function Length Error (%s is %s lines)'%(
                                       curFunction, c)))

                c = 0

        else:
            if not line_is_function_or_prototype(line):
                continue
            if sewith(line, ';') or (sewith(line, ',')
                             and sewith(lines[n+1], ';')):
                continue

            curFunction = line.partition(' ')[2].partition('(')[0]
            inFunction = True

            for ch in curFunction:
                if ch.isupper():
                    errors.append((n+1,
                            'Function Naming Error (%s contains uppercase)'%(
                                curFunction)))
                    break
            

    return errors

def line_is_function_or_prototype(line):
    if line and line[0] in ' {}/#' or not line.strip():
        return False
    if 'typedef' in line or 'struct' in line or 'union' in line:
        return False
    return True

def remove_comments_and_strings(filename):
    f = open(filename, 'U')

    s = ''

    inComment = False
    inString = False
    inChar = False

    preComment = False
    preEndComment = False

    for line in f:
        line = line.rstrip('\n')
        for c in line:
            if c == '"':
                inString = not inString
            if c == "'":
                inChar = not inChar
            if preComment:
                preComment = False
                if c == '*':
                    inComment = True
                    s = s[:-1]
                if c == '/':
                    break
            else:
                if c == '/':
                    preComment = True
            if c == '*':
                preEndComment = True
            elif preEndComment:
                if c == '/':
                    if inComment:
                        inComment = False
                        continue
                preEndComment = False
            if inComment or inString or inChar:
                continue
            s += c
        inString = False
        inChar = False
        preComment = False
        preEndComment = False
        s += '\n'
        
    return s
    

#####
import signal

def sigint_handler(signum, frame):
    print 'Failed to parse file.'
    exit()
    
signal.signal(signal.SIGINT, sigint_handler)

if __name__ == '__main__':
    #try:
        for i in range(1, len(sys.argv)):
            if sys.argv[i].strip():
                print
                print 'Parsing %s...'%sys.argv[i]
                check(sys.argv[i])
    #except:
#        sigint_handler(None, None)
