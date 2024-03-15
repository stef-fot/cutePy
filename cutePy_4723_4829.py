# ELEFTHERIOS MARIOS MANIKAS AM:4723
# STEFANOS FOTOPOULOS AM:4829
import sys

tem = 0
verbalUnits = []
listOfid = []
counter = 0
counter_line = 1
counterBraces = 0
tk = ''
fam = ''
alphabet = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
relOperators = ['<', '>', '!=', '<=', '>=', '==']
addOperators = ['+', '-']
mulOperators = ['*', '//']
assignment = ['=']
delimeter = [';', ':', ',', '"']
groupSymbols = ['[', ']', '(', ')', '#{', '#}']
keywords = ['False', 'None', 'True', 'and', 'as', 'program', 'break', 'class', 'continue', 'def', 'del',
            'elif', 'else', 'except', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'not', 'or', 'return',
            'while', '#declare', 'print', 'input', 'int']
elements = []
T1_place = []
T2_place = []
E_place = []
F1_place = []
F2_place = []
T_place = []
F_place = []
B_true = []
B_false = []
Q_true = []
Q_false = []
Q1_true = []
Q1_false = []
Q2_true = []
Q2_false = []
R1_true = []
R1_false = []
R2_true = []
R2_false = []
R_true = []
R_false = []
E1_place = []
E2_place = []
condition_true = []
condition_false = []
condition_truef = []
condition_falsef = []
ifList = []
multemp = []
addtemp = []
mulid = []
addid = []
copyadd = []
counterwhile = 0
counterwhileList = []
id = ''
call = ''
tempfuncpar = 0
tempfuncomma = 0
counter_funcs = 0
main_name = ''
flag_main = 0


def start_compile():
    global verbalUnits, listOfid
    filePath = sys.argv[1]
    file = open(filePath, "r")
    content = file.read()
    listOfElements = list(content)
    file.close()
    k = 0
    pos_limit = (2 ** 32) - 1
    neg_limit = -((2 ** 32) - 1)
    word = ''

    for i in range(len(listOfElements)):
        if i != k:
            continue
        else:
            if k > len(listOfElements) - 1:
                verbalUnits.append(listOfElements[k - 1])
                break
            elif listOfElements[k] == ' ' or listOfElements[k] == '\t':
                k = k + 1
                continue
            elif listOfElements[k] == '\n':
                verbalUnits.append(listOfElements[k])
                k = k + 1
                continue
            elif listOfElements[k] == ',':
                verbalUnits.append(listOfElements[k])
                k = k + 1
                continue
            elif listOfElements[k] == ';':
                verbalUnits.append(listOfElements[k])
                k = k + 1
                continue
            elif listOfElements[k] == ':':
                verbalUnits.append(listOfElements[k])
                k = k + 1
                continue
            elif listOfElements[k] == '[':
                verbalUnits.append(listOfElements[k])
                k = k + 1
                continue
            elif listOfElements[k] == ']':
                verbalUnits.append(listOfElements[k])
                k = k + 1
                continue
            elif listOfElements[k] == '(':
                verbalUnits.append(listOfElements[k])
                k = k + 1
                continue
            elif listOfElements[k] == ')':
                verbalUnits.append(listOfElements[k])
                k = k + 1
                continue
            elif listOfElements[k] == '+':
                verbalUnits.append(listOfElements[k])
                k = k + 1
                continue
            elif listOfElements[k] == '-':
                verbalUnits.append(listOfElements[k])
                k += 1
                continue
            elif listOfElements[k] == '*':
                verbalUnits.append(listOfElements[k])
                k += 1
                continue
            elif listOfElements[k] == '/':
                k += 1
                if k > len(listOfElements) - 1:
                    print('EOF, Expecting a second / to be a division')
                    sys.exit()
                elif listOfElements[k] == '/':
                    verbalUnits.append(listOfElements[k] + listOfElements[k - 1])
                    k += 1
                    continue
                else:
                    print("Expecting a second / to be a division")
                    sys.exit()
            elif listOfElements[k] == '<':
                k = k + 1
                if k > len(listOfElements) - 1:
                    verbalUnits.append(listOfElements[k - 1])
                    break
                elif listOfElements[k] == '=':
                    verbalUnits.append(listOfElements[k - 1] + listOfElements[k])
                    k = k + 1
                    continue
                elif listOfElements[k] != '=':
                    verbalUnits.append(listOfElements[k - 1])
                    # k = k + 1
                    continue
            elif listOfElements[k] == '"':
                verbalUnits.append(listOfElements[k])
                k = k + 1
                continue

            elif listOfElements[k] == '>':
                k = k + 1
                if k > len(listOfElements) - 1:
                    verbalUnits.append(listOfElements[k - 1])
                    break
                elif listOfElements[k] == '=':
                    verbalUnits.append(listOfElements[k - 1] + listOfElements[k])
                    k = k + 1
                    continue
                elif listOfElements[k] != '=':
                    verbalUnits.append(listOfElements[k - 1])
                    # k = k + 1
                    continue
            elif listOfElements[k] == '=':
                k = k + 1
                if k > len(listOfElements) - 1:
                    verbalUnits.append(listOfElements[k - 1])
                    break
                elif listOfElements[k] == '=':
                    verbalUnits.append(listOfElements[k - 1] + listOfElements[k])
                    k = k + 1
                    continue
                elif listOfElements[k] != '=':
                    verbalUnits.append(listOfElements[k - 1])
                    # k = k + 1
                    continue
            elif listOfElements[k] == '!':
                k = k + 1
                if k > len(listOfElements) - 1:
                    print("Expecting = after ! so as to have !=")
                    sys.exit()
                elif listOfElements[k] == '=':
                    verbalUnits.append(listOfElements[k - 1] + listOfElements[k])
                    k = k + 1
                    continue
                elif listOfElements[k] != '=':
                    print("Expecting = after ! so as to have !=")
                    sys.exit()
            elif listOfElements[k] == '#':
                k = k + 1
                if k > len(listOfElements) - 1:
                    print("Expecting something after #")
                    sys.exit()
                elif listOfElements[k] == '$':
                    k = k + 1
                    # continue
                    while True:
                        if k > len(listOfElements) - 1:
                            print("Missing closing comment section with #$")
                            sys.exit()
                        elif listOfElements[k] == '#':
                            k = k + 1
                            if k > len(listOfElements) - 1:
                                print("Missing closing comment section  with #$")
                                sys.exit()
                            if listOfElements[k] == '$':
                                k = k + 1
                                break
                        else:
                            k = k + 1
                elif listOfElements[k] == '{':
                    verbalUnits.append('#{')
                    k = k + 1
                    continue
                elif listOfElements[k] == '}':
                    verbalUnits.append('#}')
                    k = k + 1
                    continue
                else:
                    continue
            elif listOfElements[k].isalpha() or listOfElements[k] == '_':
                word += listOfElements[k]
                while True:
                    k = k + 1
                    if k > len(listOfElements) - 1:
                        if len(word) <= 30:
                            if word == 'declare' and listOfElements[k - 8] == '#':
                                word = '#declare'
                                verbalUnits.append(word)
                                word = ''
                                break
                            else:
                                verbalUnits.append(word)
                                listOfid.append(word)
                                word = ''
                                break
                        else:
                            print("The word has over 30 characters make it smaller")
                            sys.exit()

                    if listOfElements[k].isalnum() or listOfElements[k] == '_':
                        word += listOfElements[k]
                        continue
                    else:
                        if len(word) <= 30:
                            if word == 'declare' and listOfElements[k - 8] == '#':
                                word = '#declare'
                                verbalUnits.append(word)
                                word = ''
                                break
                            else:
                                verbalUnits.append(word)
                                listOfid.append(word)
                                word = ''
                                break
                        else:
                            print("The word has over 30 characters make it smaller")
                            sys.exit()
            elif listOfElements[k].isdigit():
                word += listOfElements[k]
                while True:
                    k = k + 1
                    if k > len(listOfElements) - 1:
                        num = int(word)
                        if neg_limit <= num <= pos_limit:
                            verbalUnits.append(word)
                            word = ''
                            break
                        else:
                            print("The number must be between [ -((2^32) -1) , (2^32) -1 ]")
                            sys.exit()
                    if listOfElements[k].isdigit():
                        word += listOfElements[k]
                        continue
                    else:
                        num = int(word)
                        if neg_limit <= num <= pos_limit:
                            verbalUnits.append(word)
                            word = ''
                            break
                        else:
                            print("The number must be between [ -((2^32) -1) , (2^32) -1 ]")
                            sys.exit()

    line = 1
    for i in verbalUnits:
        if i in keywords:
            print("{:<31} {:<31} {:<11}".format(i, "family:keyword", "line:{}".format(line)))
        elif i in relOperators:
            print("{:<31} {:<31} {:<11}".format(i, "family:relOperator", "line:{}".format(line)))
        elif i in addOperators:
            print("{:<31} {:<31} {:<11}".format(i, "family:addOperator", "line:{}".format(line)))
        elif i in mulOperators:
            print("{:<31} {:<31} {:<11}".format(i, "family:mulOperator", "line:{}".format(line)))
        elif i in delimeter:
            print("{:<31} {:<31} {:<11}".format(i, "family:delimiter", "line:{}".format(line)))
        elif i in assignment:
            print("{:<31} {:<31} {:<11}".format(i, "family:assignment", "line:{}".format(line)))
        elif i in groupSymbols:
            print("{:<31} {:<31} {:<11}".format(i, "family:groupSymbol", "line:{}".format(line)))
        elif i.isdigit():
            print("{:<31} {:<31} {:<11}".format(i, "family:number", "line:{}".format(line)))
        elif i == '\n':
            line += 1
        else:
            print("{:<31} {:<31} {:<11}".format(i, "family:id", "line:{}".format(line)))


def lex(j):
    if j > len(verbalUnits) - 1:
        return 'EOF', 'EOF'
    elif verbalUnits[j] in listOfid and verbalUnits[j] not in keywords:
        return verbalUnits[j], 'id'
    elif verbalUnits[j] in keywords:
        return verbalUnits[j], 'keywords'
    elif verbalUnits[j] in relOperators:
        return verbalUnits[j], 'relOperators'
    elif verbalUnits[j] in addOperators:
        return verbalUnits[j], 'addOperators'
    elif verbalUnits[j] in mulOperators:
        return verbalUnits[j], 'mulOperators'
    elif verbalUnits[j] in assignment:
        return verbalUnits[j], 'assignment'
    elif verbalUnits[j] in delimeter:
        return verbalUnits[j], 'delimeter'
    elif verbalUnits[j] in groupSymbols:
        return verbalUnits[j], 'groupSymbols'
    elif verbalUnits[j] == '\n':
        return 'newLine', 'newLine'
    elif verbalUnits[j].isdigit():
        return verbalUnits[j], 'number'


listOperator = "jump,begin_block,end_block,halt,call,in,out,par,cv,ref,ret"
listcopy = []
mergelist = []
counterTemp = 1
counterlist = 0
label_num = 1


def genQuad(op, op1, op2, op3):
    global label_num, listcopy
    listcopy.append(str(label_num) + ':')
    listcopy.append(op)
    listcopy.append(op1)
    listcopy.append(op2)
    listcopy.append(op3)
    label_num += 1


def nextQuad():
    global label_num
    return label_num


def newTemp():
    global counterTemp
    tmp = "%" + str(counterTemp)
    counterTemp += 1
    return tmp


def emptyList():
    emptylist = []
    return emptylist


def makeList(label):
    global label_num, listcopy, counterlist
    makelist = []
    makelist.append(str(label) + ':')
    return makelist


def mergeList(list1, list2):
    mergelist = list1.copy()
    mergelist.extend(list2)
    return mergelist


def backpatch(list, label):
    global label_num, listcopy, mergelist
    newlabel = str(label)  # + ':'
    for i in range(len(listcopy)):
        if listcopy[i] in list:
            if listcopy[i + 4] == '_':
                listcopy[i + 4] = newlabel


def printEndiamesos():
    global listcopy
    with open("Endiamesos.int", "w") as file1:
        for i in range(0, len(listcopy), 5):
            row = ''
            for j in range(i, min(i + 5, len(listcopy))):
                row += str(listcopy[j]) + ' '
            print(row)
            file1.write(row + "\n")
    file1.close()


import sys
from abc import ABC, abstractmethod

lastoffset = 0
Type = []
Mode = 'cv'
level = 0
entity_stack = []
scopes = None
scope_name = []
symbol_stack = []
framelengthgl = None
symbfile = []
starting_quad = []


class Entity(ABC):
    def __init__(self, name):
        self.name = name

        self.next = None


class Procedure(Entity):
    def __init__(self, name, startingQuad, framelength, formalParameters):
        super().__init__(name)
        self.startingQuad = startingQuad
        self.framelength = framelength
        self.formalParameters = formalParameters

    def update_fields(self, startingQuad, framelength):
        self.startingQuad = startingQuad
        self.framelength = framelength

    def add_standard_parameter(self, parameter):
        self.formalParameters.append(parameter)


class Function(Procedure):
    def __init__(self, name, datatype, startingQuad, framelength, formalParameters):
        super().__init__(name, startingQuad, framelength, formalParameters)
        self.datatype = datatype

    def update_fields(self, startingQuad, framelength):
        super().update_fields(startingQuad, framelength)

    def add_standard_parameter(self, parameter):
        super().add_standard_parameter(parameter)


class FormalParameter(Entity):
    def __init__(self, name, datatype, mode):
        super().__init__(name)
        self.datatype = datatype
        self.mode = mode


class Variable(Entity):
    def __init__(self, name, datatype, offset):
        super().__init__(name)
        self.datatype = datatype
        self.offset = offset


class Parameter(FormalParameter, Variable):
    def __init__(self, name, datatype, mode, offset):
        FormalParameter.__init__(self, name, datatype, mode)
        Variable.__init__(self, name, datatype, offset)


class TemporaryVariable(Variable):
    def __init__(self, name, datatype, offset):
        Variable.__init__(self, name, datatype, offset)


class SymbolicConstant(Entity):
    def __init__(self, name, datatype, value):
        super().__init__(name)
        self.type = datatype
        self.value = value


class Scope(Entity):
    global Scopes

    def __init__(self, name, level):
        super().__init__(name)
        self.level = level


class Table(Scope):
    global Scopes

    def __init__(self, name, level):
        super().__init__(name, level)

sublist = []

def insert_entity(entity):
    global lastoffset, Type, Mode, entity_stack, symbol_stack, level, framelengthgl
    Type.append(type)
    new_ent = entity

    if not entity_stack:
        new_ent.offset = 12
        lastoffset = new_ent.offset
    else:
        new_ent.offset = lastoffset + 4
        lastoffset = new_ent.offset
    if entity.datatype == 'var':
        if not symbol_stack:
            symbol_stack.append([])
        symbol_stack[-1].append('[{}/{}] <- '.format(entity.name, entity.offset))
    elif entity.datatype == 'par':
        if not symbol_stack:
            symbol_stack.append([])
        symbol_stack[-1].append('[{}/{}/{}] <- '.format(entity.name, entity.offset, Mode))
    elif entity.datatype == 'func':
        if framelengthgl is not None:
            if not symbol_stack:
                symbol_stack.append([])
            symbol_stack[-1].append('[{}/{}]  '.format(entity.name, entity.framelength))
            symbol_stack.append([])
            framelengthgl = None
        else:
            if not symbol_stack:
                symbol_stack.append([])
            symbol_stack[-1].append('[{}] '.format(entity.name))
            symbol_stack.append([])
            # symbol_stack[-1].append(sublist)
            #
            # # Add item to the sublist
            # sublist.append('[{}] '.format(entity.name))

            lastoffset = 8

    entity_stack.append(new_ent)


def new_scope(name):
    global entity_stack, level, scopes, scope_name, symbol_stack

    new_scope = Scope(name, level)
    new_scope.name = name
    scope_name.append(name)
    if scopes is None:
        level = 0
        scopes = new_scope
    else:
        new_scope.next = scopes
        scopes = new_scope
        level += 1

    return new_scope


def remove_scope():
    global level, entity_stack, scopes, symbol_stack,lastoffset
    if scopes is None:
        print("There no scope to delete")
        sys.exit()
    if flag_main == 0:
        if level > 0:

            symbol_stack.pop(-1)
            level -= 1

        else:
            symbol_stack.pop(-1)
    else:
        symbol_stack=[]
        entity_stack = []
        level = -1
        lastoffset=0
    return

def update_fields(name, startingQuadup, framelengthup):
    global framelengthgl, symbol_stack,lastoffset
    temp = 0
    startquad = startingQuadup
    if level > 1:
        i = search(name)
        if i is None:
            return
        else:
            print(level)
            entity_stack[i].startingQuad = startquad
            entity_stack[i].framelength = framelengthup
            lastoffset = framelengthup
            symbol_stack[level - 1][-1] = '[{}/{}/{}]  '.format(name, framelengthup,startquad)
    else:
        i = search(name)
        if i is None:
            return
        else:
            entity_stack[i].startingQuad = startquad
            entity_stack[i].framelength = framelengthup
            lastoffset = framelengthup
            for element in reversed(symbol_stack[level]):
                if "<-" in element:
                    temp = element.split('/')[1].replace(']', '').replace(' <-', '')
                    temp = int(temp)
                    break
            if level == 0:

                symbol_stack[level][-1] = '[{}/{}/{}]  '.format(name, framelengthup, startquad)

            else:
                symbol_stack[level - 1][-1] = '[{}/{}/{}]  '.format(name, temp + 4,startquad)


def add_standard_parameter(parameter):
    global entity_stack
    insert_entity(FormalParameter(parameter, "par", "cv"))


def search(name):
    global entity_stack
    for i, entity in reversed(list(enumerate(entity_stack))):
        if entity.name == name:
            return i
    return None




def print_symbol_table():
    global Type, Mode, level, entity_stack, scope_name, scopes, symbol_stack, symbfile,main_name,flag_main,counter_main
    scope = scopes
    with open("Symbol.symb", "a") as symbfile:
        while True:
            if not entity_stack:
                return
            else:
                if not scope_name:
                    return
                else:
                    if flag_main == 1:
                        symbfile.write("Current Scope: {}\n".format(scope_name[0]))
                        print("Current Scope:", scope_name[0])

                        prev_level = None
                        print("".join(symbol_stack[0]))
                        symbfile.write("".join(symbol_stack[0]) + "\n")
                        print("\n")
                        symbfile.write("\n")
                        scope_name.pop(0)


                    else:
                        symbfile.write("Current Scope: {}\n".format(scope_name[0]))
                        print("Current Scope:", scope_name[0])

                        prev_level = None
                        for i in range(len(symbol_stack)):
                            if symbol_stack[i]:
                                print("Level:", i)
                                print("".join(symbol_stack[i]))
                                symbfile.write("Level: {}\n".format(i))
                                symbfile.write("".join(symbol_stack[i]) + "\n")

                        print("\n")
                        symbfile.write("\n" )
                        scope_name.pop(0)
                        #symbol_stack = []


def lexer():
    global counter
    token, family = lex(counter)
    counter += 1
    return token, family


def syntax():
    global tk, fam, counterBraces
    start_Rule()


def start_Rule():
    global tk, fam, counterBraces, counter_line
    tk, fam = lexer()
    while fam == 'newLine':
        counter_line += 1
        tk, fam = lexer()
    if tk == 'def':
        main_part()
    if tk == 'if':
        call_main_part()


def main_part():
    global tk, fam, counter_line
    main_function()
    while fam == 'newLine':
        counter_line += 1
        tk, fam = lexer()
    while tk == 'def':
        main_function()

counter_main = 0
def main_function():
    global tk, fam, counterBraces, counter_line, starting_quad, level,main_name,flag_main,scope_name,counter_main,lastoffset
    if tk == 'def' and fam != 'EOF':
        tk, fam = lexer()
        if fam == 'id' and fam != 'EOF':
            functionName = tk
            new_scope(functionName)
            tk, fam = lexer()
            if tk == '(' and fam != 'EOF':
                tk, fam = lexer()
                if tk == ')' and fam != 'EOF':
                    tk, fam = lexer()
                    if tk == ':' and fam != 'EOF':
                        tk, fam = lexer()
                        while fam == 'newLine' and fam != 'EOF':
                            counter_line += 1
                            tk, fam = lexer()
                            if tk == '#{' and fam != 'EOF':
                                counterBraces += 1
                                declarations()
                                while tk != '#}':
                                    while tk == 'def' and fam != 'EOF':
                                        function()
                                    genQuad("begin_block", 'main_' + functionName, "_", "_")
                                    starting_quad.append(nextQuad())

                                    statements()
                                if tk == '#}' and fam != 'EOF':
                                    scope_name.append(functionName)
                                    flag_main = 1
                                    tempoff = lastoffset
                                    insert_entity(Function(functionName, "func", 0, 0, 0))
                                    lastoffset = tempoff
                                    framelengthgl = lastoffset + 4
                                    update_fields(functionName, starting_quad[-1], framelengthgl)
                                    starting_quad.pop(-1)

                                    print_symbol_table()
                                    remove_scope()
                                    flag_main = 0
                                    counter_main += 1
                                    genQuad('halt', '_', '_', '_')
                                    genQuad("end_block", 'main_' + functionName, "_", "_")
                                    counterBraces -= 1
                                    tk, fam = lexer()
                                    while fam == 'newLine':
                                        counter_line += 1
                                        tk, fam = lexer()
                                    if fam == 'EOF':
                                        if counterBraces != 0:
                                            print("Some Braces are missing,", 'line:', counter_line)
                                            sys.exit()
                                        print("Compilation Successfull")
                                        # sys.exit()
                                    return 0

                                else:
                                    print('Error Perimena #} kai vrika ', tk, 'line:', counter_line)
                                    sys.exit()
                            else:
                                print('Error Perimena #{ kai vrika ', tk, 'line:', counter_line)
                                sys.exit()
                        else:
                            print('Error perimena #{ kai vrika ', tk, 'line:', counter_line)
                            sys.exit()
                    else:
                        print('Error Perimena : kai vrika ', tk, 'line:', counter_line)
                        sys.exit()
                else:
                    print('Error Perimena ) kai vrika ', tk, 'line:', counter_line)
                    sys.exit()
            else:
                print('Error Perimena ( kai vrika ', tk, 'line:', counter_line)
                sys.exit()
        else:
            print('Error Perimena Family id kai vrika ', fam, 'line:', counter_line)
            sys.exit()
    else:
        print('Error Perimena def kai vrika ', tk, 'line:', counter_line)
        sys.exit()


def function():
    global tk, fam, counterBraces, counter_line, tempfuncpar, starting_quad, level
    if tk == 'def' and fam != 'EOF':
        tk, fam = lexer()
        if fam == 'id' and fam != 'EOF':
            functionName = tk

            insert_entity(Function(functionName, "func", 0, 0, 0))
            print_symbol_table()
            new_scope(functionName)
            tk, fam = lexer()
            if tk == '(' and fam != 'EOF':
                tk, fam = lexer()
                tempfuncpar = 1
                id_list()

                if tk == ')' and fam != 'EOF':
                    tk, fam = lexer()
                    if tk == ':' and fam != 'EOF':
                        tk, fam = lexer()
                        while fam == 'newLine':
                            counter_line += 1
                            tk, fam = lexer()
                            if tk == '#{' and fam != 'EOF':
                                counterBraces += 1
                                declarations()
                                while tk != '#}':
                                    while tk == 'def':
                                        function()

                                    statements()
                                genQuad("begin_block", 'main_' + functionName, "_", "_")
                                starting_quad.append(nextQuad())
                                if tk == '#}' and fam != 'EOF':
                                    framelengthgl = lastoffset + 4
                                    func = Function(functionName, "func", 0, 0, 0)
                                    update_fields(functionName, starting_quad[-1], framelengthgl)
                                    starting_quad.pop(-1)

                                    print_symbol_table()
                                    remove_scope()
                                    genQuad('halt', '_', '_', '_')
                                    genQuad("end_block", 'main_' + functionName, "_", "_")
                                    counterBraces -= 1

                                    tk, fam = lexer()
                                    while fam == 'newLine':
                                        counter_line += 1
                                        tk, fam = lexer()

                                    if fam == 'EOF':
                                        if counterBraces != 0:
                                            print("some Braces are missing")
                                            sys.exit()
                                        print("Compilation Successfull")
                                        sys.exit()
                                    else:
                                        return 0

                                else:
                                    print('Error Perimena #} kai vrika ', tk, 'line:', counter_line)
                                    sys.exit()
                            else:
                                print('Error Perimena #{ kai vrika ', tk, 'line:', counter_line)
                                sys.exit()
                        else:
                            print('Error perimena #{ kai vrika ', tk, 'line:', counter_line)
                            sys.exit()
                    else:
                        print('Error Perimena : kai vrika ', tk, 'line:', counter_line)
                        sys.exit()
                else:
                    print('Error Perimena ) kai vrika ', tk, 'line:', counter_line)
                    sys.exit()
            else:
                print('Error Perimena ( kai vrika ', tk, 'line:', counter_line)
                sys.exit()
        else:
            print('Error Perimena Family id kai vrika ', fam, 'line:', counter_line)
            sys.exit()
    else:
        print('DEN YPARXEI ALLI DEF ', tk, 'line:', counter_line)


def declarations():
    global tk, fam, counter_line
    tk, fam = lexer()
    while True:
        if tk == '#declare':
            declaration_line()
        elif fam == 'newLine':

            tk, fam = lexer()
            continue
        else:
            break
    counter_line += 1
    return


def declaration_line():
    global tk, fam, counter_line
    if tk == '#declare':
        tk, fam = lexer()
        id_list()

    else:
        print('Error Perimena #declare kai vrika ', tk, 'line:', counter_line)
        sys.exit()


def statement():
    global tk, fam, counter_line
    while fam == 'id' or tk == 'print' or tk == 'return':
        simple_statement()
        return
    while tk == 'if' or tk == 'while':
        structured_statement()
    while fam == 'newLine':
        counter_line += 1
        tk, fam = lexer()


def statements():
    global tk, fam, counter_line
    statement()
    while fam == 'newLine':
        counter_line += 1
        tk, fam = lexer()
    while tk == 'def':
        main_function()
    while fam == 'id' or tk == 'print' or tk == 'return':
        statement()

def simple_statement():
    global tk, fam, counter_line

    if fam == 'id' and fam != 'EOF':
        assignment_stat()
        return
    elif tk == 'print' and fam != 'EOF':
        print_stat()
    elif tk == 'return' and fam != 'EOF':
        return_stat()
    else:
        print('Error Perimena id || print || return kai vrika   ', tk, '  ', fam, 'line:', counter_line)
        sys.exit()


def structured_statement():
    global tk, fam, tem, counter_line
    if tk == 'if' and fam != 'EOF':
        if_stat()

        return 0


    elif tk == 'while' and fam != 'EOF':
        while_stat()
    else:
        print('Error Perimena if || while kai vrika   ', tk, 'line:', counter_line)
        sys.exit()


def assignment_stat():
    global tk, fam, E_place, T_place, tem, counter_line
    if fam == 'id' and fam != 'EOF':
        id1 = tk
        tk, fam = lexer()
        if tk == '=' and fam != 'EOF':
            assign = tk
            tk, fam = lexer()
            if (fam == 'addOperators' or fam == 'number' or tk == '(' or fam == 'id') and fam != 'EOF':
                E_place = expression()

                genQuad(assign, E_place, '_', id1)
                if tk == ';' and fam != 'EOF':
                    tk, fam = lexer()
                    while fam == 'newLine':
                        counter_line += 1
                        tk, fam = lexer()

                    return 0
                else:
                    print('Error Perimena ; kai vrika ', tk)
                    sys.exit()

            elif tk == 'int' and fam != 'EOF':
                tk, fam = lexer()
                if tk == '(' and fam != 'EOF':
                    tk, fam = lexer()
                    if tk == 'input' and fam != 'EOF':
                        tk, fam = lexer()
                        if tk == '(' and fam != 'EOF':
                            tk, fam = lexer()
                            if tk == ')' and fam != 'EOF':
                                tk, fam = lexer()
                                if tk == ')' and fam != 'EOF':
                                    tk, fam = lexer()
                                    if tk == ';' and fam != 'EOF':
                                        genQuad('in', id1, '_', '_')
                                        tk, fam = lexer()
                                        while fam == 'newLine':
                                            counter_line += 1
                                            tk, fam = lexer()
                                    else:
                                        print('Error Perimena ; kai vrika ', tk, 'line:', counter_line)
                                        sys.exit()
                                else:
                                    print('Error Perimena ) kai vrika ', tk, 'line:', counter_line)
                                    sys.exit()
                            else:
                                print('Error Perimena ) kai vrika ', tk, 'line:', counter_line)
                                sys.exit()
                        else:
                            print('Error Perimena ( kai vrika ', tk, 'line:', counter_line)
                            sys.exit()
                    else:
                        print('Error Perimena input kai vrika ', tk, 'line:', counter_line)
                        sys.exit()
                else:
                    print('Error Perimena ( kai vrika ', tk, 'line:', counter_line)
                    sys.exit()
            else:
                print('Error Perimena int kai vrika ', tk, 'line:', counter_line)
                sys.exit()
        else:
            print('Error Perimena = kai vrika ', tk, 'line:', counter_line)
            sys.exit()
    else:
        print('Error Perimena Family id kai vrika ', fam, 'line:', counter_line)
        sys.exit()


def print_stat():
    global tk, fam, counter_line
    if tk == 'print':
        tk, fam = lexer()
        if tk == '(' and fam != 'EOF':
            tk, fam = lexer()
            outtk = tk
            expression()
            if tk == ')' and fam != 'EOF':
                tk, fam = lexer()
                if tk == ';' and fam != 'EOF':
                    genQuad('out', outtk, '_', '_')
                    tk, fam = lexer()
                    while True:
                        if fam == 'EOF':
                            print('den gyrizei pote sto kleisimo', 'line:', counter_line)
                            sys.exit()
                        elif fam == 'newLine':
                            tk, fam = lexer()
                        else:
                            break
                else:
                    print('Error Perimena ; kai vrika ', tk, 'line:', counter_line)
                    sys.exit()
            else:
                print('Error Perimena ) kai vrika ', tk, 'line:', counter_line)
                sys.exit()
        else:
            print('Error Perimena ( kai vrika ', tk, 'line:', counter_line)
            sys.exit()
    else:
        print('Error Perimena print kai vrika ', tk, 'line:', counter_line)
        sys.exit()


def return_stat():
    global tk, fam, counter_line
    if tk == 'return' and fam != 'EOF':
        tk, fam = lexer()
        if tk == '(' and fam != 'EOF':
            tk, fam = lexer()
            exp = tk
            expression()
            if tk == ')' and fam != 'EOF':
                tk, fam = lexer()
                if tk == ';' and fam != 'EOF':
                    genQuad('ret', '_', '_', exp)
                    tk, fam = lexer()
                    while fam == 'newLine':
                        counter_line += 1
                        tk, fam = lexer()
                        return 0
                else:
                    print('Error Perimena ; kai vrika ', tk, 'line:', counter_line)
                    sys.exit()
            else:
                print('Error Perimena ) kai vrika ', tk, 'line:', counter_line)
                sys.exit()
        else:
            print('Error Perimena ( kai vrika ', tk, 'line:', counter_line)
            sys.exit()
    else:
        print('Error Perimena return kai vrika ', tk, 'line:', counter_line)
        sys.exit()


def if_stat():
    global tk, fam, counter, condition_true, condition_false, ifList, condition_falsef, condition_truef, counter_line
    condition_truef = []
    condition_falsef = []
    if tk == 'if' and fam != 'EOF':
        tk, fam = lexer()
        if tk == '__name__' and fam != 'EOF':
            counter = counter - 2
            tk, fam = lexer()
            call_main_part()
        if tk == '(' and fam != 'EOF':
            tk, fam = lexer()
            condition()
            backpatch(condition_true, nextQuad())

            if tk == ')' and fam != 'EOF':
                tk, fam = lexer()
                if tk == ':' and fam != 'EOF':
                    tk, fam = lexer()
                    while fam == 'newLine':
                        counter_line += 1
                        tk, fam = lexer()
                    if (fam == 'id' or tk == 'print' or tk == 'return' or tk == 'if' or tk == 'while') and fam != 'EOF':
                        statement()
                        ifList += makeList(nextQuad())
                        genQuad('jump', '_', '_', '_')
                        backpatch(condition_falsef, nextQuad())
                        while fam == 'newLine':
                            counter_line += 1
                            tk, fam = lexer()
                        if tk == 'else' and fam != 'EOF':
                            tk, fam = lexer()
                            if tk == ':' and fam != 'EOF':
                                tk, fam = lexer()
                                while fam == 'newLine':
                                    counter_line += 1
                                    tk, fam = lexer()
                                if (
                                        fam == 'id' or tk == 'print' or tk == 'return' or tk == 'if' or tk == 'while') and fam != 'EOF':
                                    statement()
                                elif tk == '#{' and fam != 'EOF':
                                    tk, fam = lexer()
                                    while fam == 'newLine':
                                        counter_line += 1
                                        tk, fam = lexer()
                                    if fam == 'id' or tk == 'print' or tk == 'return' or tk == 'if' or tk == 'while':
                                        while tk != '#}':
                                            statements()

                                    while fam == 'newLine':
                                        counter_line += 1
                                        tk, fam = lexer()
                                    if tk == '#}' and fam != 'EOF':
                                        tk, fam = lexer()
                                    else:
                                        print('Error Perimena #} kai vrika ', tk, 'line:', counter_line)
                                        sys.exit()
                                else:
                                    print('Error Perimena #{ kai vrika ', tk, 'line:', counter_line)
                                    sys.exit()
                            else:
                                print('Error Perimena : kai vrika ', tk, 'line:', counter_line)
                                sys.exit()
                        backpatch(ifList, nextQuad())
                    elif tk == '#{' and fam != 'EOF':
                        tk, fam = lexer()
                        while fam == 'newLine':
                            counter_line += 1
                            tk, fam = lexer()
                        if (
                                fam == 'id' or tk == 'print' or tk == 'return' or tk == 'if' or tk == 'while') and fam != 'EOF':
                            while tk != '#}':
                                statements()
                                ifList += makeList(nextQuad())
                                genQuad('jump', '_', '_', '_')
                                backpatch(condition_falsef, nextQuad())

                        while fam == 'newLine':
                            tk, fam = lexer()
                        if tk == '#}' and fam != 'EOF':
                            tk, fam = lexer()
                            while fam == 'newLine':
                                counter_line += 1
                                tk, fam = lexer()

                            if tk == 'else' and fam != 'EOF':
                                tk, fam = lexer()
                                if tk == ':' and fam != 'EOF':
                                    tk, fam = lexer()
                                    while fam == 'newLine':
                                        counter_line += 1
                                        tk, fam = lexer()
                                    if (
                                            fam == 'id' or tk == 'print' or tk == 'return' or tk == 'if' or tk == 'while') and fam != 'EOF':
                                        statement()
                                    elif tk == '#{' and fam != 'EOF':
                                        tk, fam = lexer()
                                        while fam == 'newLine':
                                            counter_line += 1
                                            tk, fam = lexer()
                                        if (
                                                fam == 'id' or tk == 'print' or tk == 'return' or tk == 'if' or tk == 'while') and fam != 'EOF':
                                            while tk != '#}':
                                                statements()
                                        while fam == 'newLine':
                                            counter_line += 1
                                            tk, fam = lexer()
                                        if tk == '#}' and fam != 'EOF':
                                            tk, fam = lexer()
                                        else:
                                            print('Error Perimena #} kai vrika ', tk, 'line:', counter_line)
                                            sys.exit()
                                    else:
                                        print('Error Perimena #{ kai vrika ', tk, 'line:', counter_line)
                                        sys.exit()
                                else:
                                    print('Error Perimena : kai vrika ', tk, 'line:', counter_line)
                                    sys.exit()
                            backpatch(ifList, nextQuad())
                        else:
                            print('Error Perimena #} kai vrika ', tk, 'line:', counter_line)
                            sys.exit()
                    else:
                        print('Error Perimena #{ kai vrika ', tk, 'line:', counter_line)
                        sys.exit()
                else:
                    print('Error Perimena : kai vrika ', tk, 'line:', counter_line)
                    sys.exit()
            else:
                print('Error Perimena ) kai vrika ', tk, 'line:', counter_line)
                sys.exit()
        else:
            print('Error Perimena ( kai vrika ', tk, 'line:', counter_line)
            sys.exit()

    else:
        print('Error Perimena if kai vrika ', tk)
        sys.exit()



def while_stat():
    global tk, fam, condition_true, condition_false, R1_false, counterwhile, counterwhileList,counter_line
    counterwhile = 0
    newcondfalse = []
    label = []
    if tk == 'while' and fam != 'EOF':
        tk, fam = lexer()
        condQuad = nextQuad()
        if tk == '(' and fam != 'EOF':
            tk, fam = lexer()
            condition()
            counterwhileList.append(counterwhile)
            if tk == ')' and fam != 'EOF':
                tk, fam = lexer()
                backpatch(condition_true, nextQuad())
                if tk == ':' and fam != 'EOF':
                    tk, fam = lexer()
                    while fam == 'newLine':
                        counter_line += 1
                        tk, fam = lexer()
                    if (fam == 'id' or tk == 'print' or tk == 'return' or tk == 'if' or tk == 'while') and fam != 'EOF':
                        statement()
                        genQuad('jump', '_', '_', condQuad)

                        lastnumofcond = counterwhileList[-1:]
                        counterwhileList.pop()
                        lastnumofcond = int(lastnumofcond[0])
                        for i in range(len(condition_false) - 1, len(condition_false) - lastnumofcond - 1, -1):
                            newcondfalse.append(condition_false[i])

                            condition_false.pop()
                        for i in range(len(listcopy)):

                            if listcopy[i] == str(newcondfalse[0]):

                                if listcopy[i + 4] == '_':
                                    backpatch(newcondfalse, nextQuad())
                                else:
                                    lastnumofcond = counterwhileList[-1:]
                                    counterwhileList.pop()
                                    lastnumofcond = int(lastnumofcond[0])
                                    for i in range(len(condition_false) - 1, len(condition_false) - lastnumofcond - 1,
                                                   -1):
                                        newcondfalse.append(condition_false[i])
                                        condition_false.pop()
                                        backpatch(newcondfalse, nextQuad())

                                    return

                    elif tk == '#{' and fam != 'EOF':
                        tk, fam = lexer()
                        while fam == 'newLine':
                            counter_line += 1
                            tk, fam = lexer()
                        if (
                                fam == 'id' or tk == 'print' or tk == 'return' or tk == 'if' or tk == 'while') and fam != 'EOF':
                            while tk != '#}':
                                statements()
                                genQuad('jump', '_', '_', condQuad)
                                backpatch(condition_false, nextQuad())

                        while fam == 'newLine':
                            counter_line += 1
                            tk, fam = lexer()
                        if tk == '#}' and fam != 'EOF':
                            tk, fam = lexer()
                        else:
                            print('Error Perimena #} kai vrika ', tk,'line:',counter_line)
                            sys.exit()
                    else:
                        print('Error Perimena #{ kai vrika ', tk,'line:',counter_line)
                        sys.exit()
                else:
                    print('Error Perimena : kai vrika ', tk,'line:',counter_line)
                    sys.exit()
            else:
                print('Error Perimena ) kai vrika ', tk,'line:',counter_line)
                sys.exit()
        else:
            print('Error Perimena ( kai vrika ', tk,'line:',counter_line)
            sys.exit()

    else:
        print('Error Perimena while kai vrika ', tk,'line:',counter_line)
        sys.exit()



def id_list():
    global tk, fam, counter_line, tempfuncpar, tempfuncomma
    if fam == 'id' and fam != 'EOF':
        if tempfuncpar == 1:
            tempfuncpar = 0
            tempfuncomma = 1
            add_standard_parameter(tk)

        else:
            insert_entity(Variable(tk, "var", 0))
        tk, fam = lexer()
        if fam != 'newLine':
            counter_line += 1
            while True:
                if tk == ',' and fam != 'EOF':
                    tk, fam = lexer()
                    if fam == 'id' and fam != 'EOF':
                        if tempfuncomma == 1:
                            add_standard_parameter(tk)

                        else:
                            insert_entity(Variable(tk, "var", 0))
                        tk, fam = lexer()
                        continue
                    else:
                        print('Error Perimena kati meta to komma ', 'line:', counter_line)
                        sys.exit()
                else:
                    tempfuncomma = 0
                    break
        else:
            return 0

    else:
        print('Error Perimena Family id kai vrika ', fam, 'line:', counter_line)
        sys.exit()


def expression():
    global tk, fam, T1_place, T2_place, multemp, addtemp, copyadd, E_place, elements, F1_place, F2_place, T_place

    optional_sign()
    T1_place = term()

    while tk == '+' or tk == '-':
        tkOper = ADD_OP()
        T2_place = term()


        w = newTemp()

        genQuad(tkOper, T1_place, T2_place, w)
        T1_place = w

    E_place = T1_place
    return E_place


def term():
    global tk, fam, T1_place, T2_place, E_place, T_place, F1_place, F2_place, elements, alphabet
    F1_place = factor()

    while tk == '*' or tk == '//':
        tkOper = MUL_OP()
        F2_place = factor()
        w = newTemp()
        genQuad(tkOper, F1_place, F2_place, w)
        F1_place = w

    T_place = F1_place

    return T_place


def factor():
    global tk, fam, F_place, E_place, addtemp, multemp, T1_place, F1_place, call, counter_line
    if fam == 'number' and fam != 'EOF':
        F_place = tk
        tk, fam = lexer()
        return F_place
    elif tk == '(' and fam != 'EOF':
        tk, fam = lexer()
        while tk != ')':
            addtemp = T1_place
            multemp = F1_place
            E_place = expression()
            T1_place = addtemp
            F1_place = multemp
            if tk in relOperators:
                break
        if tk == ')' and fam != 'EOF':
            F_place = E_place
            tk, fam = lexer()

            while fam == 'newLine':
                counter_line += 1
                tk, fam = lexer()
            return F_place
        else:

            return 0
    elif (fam == 'id' or fam == 'keywords') and fam != 'EOF':
        F_place = tk
        tk, fam = lexer()
        if tk == '(' and fam != 'EOF':
            call = F_place
            id_tail()

        return F_place
    else:

        return tk


def id_tail():
    global tk, fam, mulid, addid, T1_place, F1_place, counter_line
    if tk == '(' and fam != 'EOF':
        tk, fam = lexer()
        actual_par_list()
        while fam == 'newLine':
            # counter_line += 1
            tk, fam = lexer()
            return tk
        if tk == ')' and fam != 'EOF':


            tk, fam = lexer()
            return id
        else:
            print('Error Perimena ) kai vrika ', tk, 'line:', counter_line)
            sys.exit()


def actual_par_list():
    global tk, fam, E_place, mulid, addid, T1_place, T2_place, F1_place, F2_place, F_place
    temp_par = []
    temp_par.append(tk)
    tempT1 = T1_place
    E_place = expression()
    addid.append(E_place)
    if len(addid) > 1:
        T1_place = addid[0]
        addid.pop(0)

    while tk == ',':
        tk, fam = lexer()
        temp_par.append(tk)
        E_place = expression()

        continue
    par = newTemp()
    insert_entity(TemporaryVariable(par, "var", 0))
    while temp_par:
        genQuad("par", temp_par[0], "cv", "_")
        temp_par.pop(0)

    genQuad("par", par, "ret", "_")
    genQuad("call", call, "_", "_")
    T1_place = tempT1
    F_place = par
    return 0


def optional_sign():
    global tk, fam
    ADD_OP()


def condition():
    global tk, fam, B_true, B_false, Q1_true, Q1_false, Q2_true, Q2_false
    bool_term()

    B_true = Q1_true
    B_false = Q1_false
    if tk == 'or' and fam != 'EOF':
        while tk == 'or' and fam != 'EOF':
            backpatch(B_false, nextQuad())

            tk, fam = lexer()
            bool_term()
            B_true = mergeList(B_true, Q2_true)
            B_false = Q2_false

    else:
        return 0


def bool_term():
    global tk, fam, Q_true, Q_false, R1_true, R1_false, R2_true, R2_false
    bool_factor()
    Q_true = R1_true
    Q_false = R1_false
    backpatch(B_true, nextQuad())
    if tk == 'and' and fam != 'EOF':
        while tk == 'and':
            backpatch(Q_true, nextQuad())

            tk, fam = lexer()
            bool_factor()

            Q_false = mergeList(Q_false, R2_false)
            Q_true = R2_true

    else:
        return 0


def bool_factor():
    global tk, fam, R_true, R_false, E1_place, E2_place, Q1_true, Q1_false, Q2_true, Q2_false, R1_true, R1_false, R2_true, R2_false, condition_true, condition_false, condition_falsef, condition_truef, counterwhile, counter_line
    if tk == 'not' and fam != 'EOF':
        tk, fam = lexer()
        if tk == '[' and fam != 'EOF':
            tk, fam = lexer()
            condition()
            if tk == ']' and fam != 'EOF':
                R_true = B_false
                R_false = B_true
                tk, fam = lexer()
            else:
                print('Error Perimena ] kai vrika ', tk, 'line:', counter_line)
                sys.exit()
        else:
            print('Error Perimena [ kai vrika ', tk, 'line:', counter_line)
            sys.exit()

    if tk == '[' and fam != 'EOF':
        tk, fam = lexer()
        condition()
        if tk == ']' and fam != 'EOF':
            R_true = B_true
            R_false = B_false
            tk, fam = lexer()
        else:
            print('Error Perimena ] kai vrika ', tk, 'line:', counter_line)
            sys.exit()

    if (fam == 'addOperators' or fam == 'number' or tk == '(' or fam == 'id') and fam != 'EOF':
        E1_place = expression()
        if fam == 'relOperators' and fam != 'EOF':
            rel_op = tk

            tk, fam = lexer()

            E2_place = expression()
            R_true = makeList(nextQuad())
            Q1_true = makeList(nextQuad())
            Q2_true = makeList(nextQuad())
            R1_true = makeList(nextQuad())
            R2_true = makeList(nextQuad())
            condition_true += makeList(nextQuad())
            condition_truef += makeList(nextQuad())

            genQuad(rel_op, E1_place, E2_place, '_')
            R_false = makeList(nextQuad())
            Q1_false += makeList(nextQuad())
            Q2_false = makeList(nextQuad())
            R1_false = makeList(nextQuad())
            R2_false = makeList(nextQuad())
            condition_false += makeList(nextQuad())
            condition_falsef += makeList(nextQuad())

            genQuad('jump', '_', '_', '_')

            counterwhile += 1
        else:
            print('Error Perimena Family relOperators kai vrika ', fam, tk, 'line:', counter_line)
            sys.exit()

    else:

        return 0


def call_main_part():
    global tk, fam, counterBraces, counter_line
    if tk == 'if' and fam != 'EOF':
        tk, fam = lexer()
        if tk == '__name__' and fam != 'EOF':
            tk, fam = lexer()
            if tk == '==' and fam != 'EOF':
                tk, fam = lexer()
                if tk == '"' and fam != 'EOF':
                    tk, fam = lexer()
                    if tk == '__main__' and fam != 'EOF':
                        genQuad("begin_block", "__main__", "_", "_")
                        tk, fam = lexer()
                        if tk == '"' and fam != 'EOF':
                            tk, fam = lexer()
                            if tk == ':' and fam != 'EOF':
                                tk, fam = lexer()
                                while fam == 'newLine':
                                    counter_line += 1
                                    tk, fam = lexer()
                                main_function_call()
                                while fam == 'id':
                                    main_function_call()
                                if counterBraces != 0:
                                    print("Some Braces(#{ or #}) are missing", 'line:', counter_line)
                                    sys.exit()
                                else:
                                    genQuad('halt', '_', '_', '_')
                                    genQuad("end_block", "__main__", "_", "_")
                                    print("Compilation Succeeded")
                            else:
                                print('Error Perimena : kai vrika ', tk, 'line:', counter_line)
                                sys.exit()
                        else:
                            print('Error Perimena " kai vrika ', tk, 'line:', counter_line)
                            sys.exit()
                    else:
                        print('Error Perimena __main__ kai vrika ', tk, 'line:', counter_line)
                        sys.exit()
                else:
                    print('Error Perimena " kai vrika ', tk, 'line:', counter_line)
                    sys.exit()
            else:
                print('Error Perimena == kai vrika ', tk, 'line:', counter_line)
                sys.exit()
        else:
            print('Error Perimena __name__ kai vrika ', tk, 'line:', counter_line)
            sys.exit()
    else:
        print('Error Perimena if kai vrika ', tk, 'line:', counter_line)
        sys.exit()


def main_function_call():
    global tk, fam, counter_line
    if fam == 'id' and fam != 'EOF':
        tk, fam = lexer()
        if tk == '(' and fam != 'EOF':
            tk, fam = lexer()
            if tk == ')' and fam != 'EOF':
                tk, fam = lexer()
                if tk == ';' and fam != 'EOF':
                    tk, fam = lexer()
                    while fam == 'newLine':
                        counter_line += 1
                        tk, fam = lexer()
                else:
                    print('Error Perimena ; kai vrika ', tk, 'line:', counter_line)
                    sys.exit()
            else:
                print('Error Perimena ) kai vrika ', tk, 'line:', counter_line)
                sys.exit()
        else:
            print('Error Perimena ( kai vrika ', tk, 'line:', counter_line)
            sys.exit()
    else:
        print('Error Perimena Family id kai vrika ', fam, 'line:', counter_line)
        sys.exit()


def ADD_OP():
    global tk, fam, T2_place
    if fam == 'addOperators' and fam != 'EOF':
        oper = tk
        tk, fam = lexer()
        return oper


def MUL_OP():
    global tk, fam, T2_place
    oper = tk
    if fam == 'mulOperators' and fam != 'EOF':
        tk, fam = lexer()
        return oper


start_compile()
print("End of Verbal Analysis")
syntax()
printEndiamesos()

