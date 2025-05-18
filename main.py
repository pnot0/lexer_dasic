from lexer_parser import parser

"""
Esta linguagem foi inspirada em BASIC
"""

comandos = [
    'PRINT "hellord"',
    'IF a == b THEN PRINT "hello world"',
    'ELSE PRINT "hellord"',
    'FOR i = 1 TO 10 STEP 1 NEXT',
    'DO LOOP WHILE c << test',
    'DECLARE FUNCTION asda(b) END',
    'CALL asda(10)',
    'IMPORT librarytest',
    'COMMENT this is a comment',
    'erro(teste)'
    ]

i = 0
for linha in comandos:
    i+=1
    print(f"\n{i}:", linha)
    parser.parse(linha)

