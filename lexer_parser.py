import ply.lex as lex
import ply.yacc as yacc

reserved = {
	'IF' : 'IF',
	'THEN' : 'THEN',
	'ELSE' : 'ELSE',
	'ELSIF' : 'ELSIF',
	'FOR' : 'FOR',
	'TO' : 'TO',
	'STEP' : 'STEP',
	'LOOP' : 'LOOP',
	'NEXT' : 'NEXT',
	'DO' : 'DO',
	'DECLARE' : 'DECLARE',
	'FUNCTION' : 'FUNCTION',
	'END' : 'END',
	'CALL' : 'CALL',
	'IMPORT' : 'IMPORT'
}

tokens = ['PRINT', 'STRING', 'NUMBER', 'ID', 'LPAREN', 'RPAREN', 'COMMENT', 'COND', 'ATT', 'WHITIL'] + list(reserved.values())

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_STRING = r'\".*?\"'
t_ATT = r'='
t_COND = r'(==|<<|>>|<=|>=|<>)' 
t_ignore = ' \t\n'

def t_COMMENT(t):
    r'COMMENT .*'
    pass
    # No return value. Token discarded

def t_WHITIL(t):
	r'WHILE|UNTIL'
	return t

def t_PRINT(t):
	r'PRINT '
	return t

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*'
	t.type = reserved.get(t.value, 'ID')
	return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NL(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t): t.lexer.skip(1)

lexer = lex.lex()

def p_stmt(p): 
	'''stmt : prnt
			| if
			| cdlp
			| func
			| impt
			| 
  	''' 

def p_if(p):
	'''if : IF ID COND ID THEN stmt
			| ELSIF ID COND ID THEN stmt
			| ELSE stmt
	'''
	print("if|else|elsif reconhecido")

def p_cdlp(p):
	'''cdlp : FOR ID ATT NUMBER TO NUMBER STEP NUMBER stmt NEXT
			| DO stmt LOOP WHITIL ID COND ID
	'''
	print("for|do while reconhecido")

def p_func(p):
	'''func : DECLARE FUNCTION ID LPAREN ID RPAREN stmt END 
			| CALL ID LPAREN NUMBER RPAREN
	'''
	print("function|call reconhecida")

def p_impt(p):
	'''impt : IMPORT ID
	'''
	print("import reconhecido")

def p_prnt(p):
	'''prnt : PRINT STRING'''
	print("print reconhecido")
	
def p_error(p): print("Erro de sintaxe!")

parser = yacc.yacc()
