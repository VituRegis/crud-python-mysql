import sys
import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='campeonatodecaraoucoroa',
)

cursor = conexao.cursor()

#----------------------FUNÇÔES----------------------# 

def getTabela(complemento):
    letra = input(f"\n\nDeseja {complemento} qual tabela? \n U - Usuario \n C - Campeonato \n I - Inscricao \n T - Tipo de Usuario\n")

    if letra.lower() == "u":
        tabela = 'usuario'
    elif letra.lower() == "c":
        tabela = 'campeonato'
    elif letra.lower() == "i":
        tabela = 'inscricao_campeonato'
    elif letra.lower() == "t":
        tabela = 'tipo_usuario'
    else:
        print(f"\n Por favor, insira uma letra valida (U, C, I ou T).\n Sua inserção: {letra}\n\n")
        getTabela(complemento)

    return tabela

def getCampo(tabela):
    inserir = 'S'
    campos = ''

    while inserir.upper == 'S':
        if tabela.lower() == "usuario":
            print("\nQual campo? \nT - Tipo de Usuario \n N - Nome de Usuario \n E - Email de Usuario \n NAS - Nascimento \n NAC - Nacionalidade \n")
        elif tabela.lower() == "campeonato":
            print("\nQual campo? \nI - Quantidade de Inscritos \n MAX - Maximo de Inscritos \n MIN - Minimo de Inscritos \n T - Tipo de Campeonato \n")
        elif tabela.lower() == 'inscricao_campeonato':
            print("\nQual campo? \nU - Usuario \n C - Campeonato \n")
        elif tabela.lower() == 'tipo_usuario':
            campo = 'desctipo'
        else: 
            print(f'\n\n[ERRO] Algo deu errado na seleção de campos para a tabela: {tabela}\n\n')
            sys.exit()
        
        if tabela.lower() != 'tipo_usuario':
            campo = input()

        if tabela.lower() == "usuario" and campo.upper == 'T' or campo.upper == 'N' or campo.upper == 'E' or campo.upper == 'NAS' or campo.upper == 'NAC':
            if campo.upper == 'T':
                campo = 'tipousu'
            if campo.upper == 'N':
                campo = 'nomeusu'
            if campo.upper == 'E':
                campo = 'emailusu'
            if campo.upper == 'NAS':
                campo = 'nascimento'
            if campo.upper == 'NAC':
                campo = 'nacionalidade'
        elif tabela.lower() == "campeonato" or campo.upper == 'I' or campo.upper == 'MAX' or campo.upper == 'MIN' or campo.upper == 'T':
            if campo.upper == 'I':
                campo = 'inscritos'
            if campo.upper == 'MAX':
                campo = 'maxinscritos'
            if campo.upper == 'MIN':
                campo = 'mininscritos'
            if campo.upper == 'T':
                campo = 'tipocamp'
        elif tabela.lower() == 'inscricao_campeonato' or campo.upper() == 'U' or campo.upper() == 'C':
            if campo.upper == 'U':
                campo = 'idusu'
            if campo.upper == 'C':
                campo = 'idcamp'

        campos = (',' + campo if campos == '' else campo)

        inserir = input('Deseja inserir outro campo? S/N').upper

    return campos

def getFiltro(tabela):
    print("\nPor qual campo deseja filtrar?\n")
    if tabela.lower() == "usuario":
        print(" ID - Código\n T - Tipo de Usuario \n N - Nome de Usuario \n E - Email de Usuario \n NAS - Nascimento \n NAC - Nacionalidade \n")
    elif tabela.lower() == "campeonato":
        print(" ID - Código \n I - Quantidade de Inscritos \n MAX - Maximo de Inscritos \n MIN - Minimo de Inscritos \n T - Tipo de Campeonato")
    elif tabela.lower() == 'inscricao_campeonato':
        print(" INS - Código do Inscrito \n CAMP - Código do Campeonato\n")
    elif tabela.lower() == 'tipo_usuario':
        print(" T - Tipo de Usuario \n D - Descrição")
    else:
        print(f'\n\n[ERRO] Algo deu errado na seleção de filtro para a tabela: {tabela}\n\n')
        sys.exit()

    filtro = input()

    

    return filtro

#----------------------CENTRALIZADOR----------------------# 

def create():
    tabela = getTabela('criar em')
    valores = getValores()

    comando = f'INSERT INTO `{tabela}` VALUES {valores}'
    cursor.execute(comando) 
    conexao.commit() 

    return 0

def read():
    tabela = getTabela('ler')
    campo = getCampo(tabela)
    filtro = getFiltro(tabela) 

    comando = f'SELECT {campo} FROM {tabela} WHERE {filtro}'
    cursor.execute(comando) 
    resultado = cursor.fetchall()

    print(resultado)
    return 0

def update():
    tabela = getTabela('atualizar')
    campo  = getCampo(tabela)
    filtro = getFiltro(tabela) 

    comando = f'UPDATE {tabela} SET {campo} = "{novo_valor}" WHERE {filtro}'
    cursor.execute(comando) 
    conexao.commit() 

    return 0

def delete():  
    tabela = getTabela('deletar em')
    filtro = getFiltro(tabela)

    comando = f'DELETE FROM {tabela} WHERE {filtro}'
    cursor.execute(comando) 
    conexao.commit() 

    return 0

#----------------------MAIN----------------------# 

print('\n\n\n\n\n\n\n\n\n******************************************\nSeja bem vindo ao CRUD em Python do Campeonato de Cara ou Coroa\n******************************************\n\n')
op = input('Insira a operação que deseja realizar(Create/Read/Update/Delete): ')

if op.lower() == "create":
    create()
elif op.lower() == "read":
    read()
elif op.lower() == "update":
    update()
elif op.lower() == "delete":
    delete()
else:
    print("Por favor, insira uma operação válida (Create, Read, Update ou Delete).")




# CRUD
# conexao.commit()               quando for editar o BD
# resultado = cursor.fetchall()  quando for ler o banco de dados

# CREATE
'''
max_inscritos  = 10
min_inscritos  = 2
tipocamp       = 2

comando = f'INSERT INTO campeonato VALUES (DEFAULT,DEFAULT,{max_inscritos},{min_inscritos},{tipocamp})'
cursor.execute(comando) 
conexao.commit() 
'''

# READ
'''
comando = 'SELECT * FROM campeonato'
cursor.execute(comando) 
resultado = cursor.fetchall()
print(resultado)
'''

# UPDATE
'''
antigo_tipousu = 99
novo_tipousu = 10

comando = f'UPDATE usuario SET tipousu = {novo_tipousu} WHERE tipousu = {antigo_tipousu}'
cursor.execute(comando) 
conexao.commit() 
'''

# DELETE
'''
tipocamp = 2

comando = f'DELETE FROM campeonato WHERE tipocamp = {tipocamp}'
cursor.execute(comando) 
conexao.commit() 
'''

cursor.close()
conexao.close()