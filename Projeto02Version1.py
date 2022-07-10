import csv
from sympy import *
from sympy.logic.inference import satisfiable

arquivo = open('arquivoCSV/column_bin_3a_4p.csv')

dados = csv.reader(arquivo)
dadosPacientes = []

for dado in dados:
    dadosPacientes.append(dado)


def Variaveis(arquivoPacientes):
    resultado = []
    for dado in arquivoPacientes:
        for d in dado:
            if d != '1' and d != '0' and d != 'P':
                d = d.replace(' ', '')
                if d is not resultado:
                    resultado.append(d)
    return resultado


def pegaValores(arquivoPacientes):
    resultado = []
    var = Variaveis(arquivoPacientes)
    var.append('P')
    cont = len(var)
    aux = []
    cont2 = 0
    for dado in arquivoPacientes:
        for d in dado:
            if d == '1' or d == '0':
                cont2 = cont2 + 1
                aux.append(d)
                if(cont2 == cont):
                    resultado.append(aux)
                    aux = []
                    cont2 = 0
    return resultado


def FormulaCNF(arquivoPacientes):
    variaveis = Variaveis(arquivoPacientes)
    valores = pegaValores(arquivoPacientes)
    tamanho = len(valores)
    cont = 0
    resultado = str()
    aux = str()

    for valor in valores:
        cont = cont + 1
        valor.pop()
        #print(valor)
        for var, val in zip(variaveis, valor):
            if val == '1':
                aux = aux + var
                if var != variaveis[-1]:
                    aux = aux + ' | '
            if val == '0':
                aux = aux + '~' + var
                if var != variaveis[-1]:
                    aux = aux + ' | '
        resultado = resultado + '(' + aux + ')'
        #if valor[-1] == '1':
            #resultado = resultado + ' >> p '
        #else:
            #resultado = resultado + ' >> ~p '
        if cont != tamanho:
            resultado = resultado + ' & '
        aux = ''
    return resultado


def ConvertendoFormula(arquivoPacientes):
    formula = FormulaCNF(arquivoPacientes)
    var = Variaveis(arquivoPacientes)
    tamanho = len(Variaveis(arquivoPacientes))

    #print(formula)

    for i in range(tamanho):
        globals()[f'x{i}'] = symbols(f'x{i}')
        formula = formula.replace(f'{var[i]}', f'x{i}')

    formula = S(formula)
    return formula


def Satisfatible(arquivoPacientes):
    formula = ConvertendoFormula(arquivoPacientes)
    sat = satisfiable(formula)
    return sat


sat = Satisfatible(dadosPacientes)

var = Variaveis(dadosPacientes)
tamanho = len(Variaveis(dadosPacientes))
regras = []

satKeys = list(sat.keys())
satValues = list(sat.values())
aux = ''


for k, v in zip(satKeys, satValues):
    if v:
        c = str(k)
        valor = int(c[1])
        regras.append(var[valor])

print(regras)
