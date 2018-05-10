from datetime import datetime
from datetime import timedelta

aumentos = {
    datetime(day=1, month=6, year=2017): 7000,
    datetime(day=1, month=9, year=2016): 6000,
    datetime(day=1, month=1, year=2014): 4200,
    datetime(day=1, month=6, year=2011): 2500,
    datetime(day=2, month=8, year=2005): 1000,
}

hoje = datetime.today()
dia = list(sorted(aumentos.keys()))[0]
salario_atual = aumentos[dia]
um_dia = timedelta(days=1)
total = 0

def aumentar_salario_se_houve_aumento_no_dia(dia, salario_atual):
    novo_salario = aumentos.get(dia, None)
    return novo_salario or salario_atual

def eh_epoca_de_ferias(dia):
    return dia.day == 1 and dia.month == 12

def eh_dia_de_pagamento(dia):
    return dia.day == 7

def eh_dia_do_duodecimo(dia):
    return dia.day == 20 and dia.month == 12

while dia <= hoje:
    salario_atual = aumentar_salario_se_houve_aumento_no_dia(dia, salario_atual)
    dia_formatado = dia.strftime('%d/%m/%y')

    if eh_epoca_de_ferias(dia):
        total += round(salario_atual * 1.33, 2)
        print(dia_formatado, 'férias', total) 

    if eh_dia_de_pagamento(dia):
        total += salario_atual
        print(dia_formatado, 'paguei salario', salario_atual, total)

    if eh_dia_do_duodecimo(dia):
        total += salario_atual
        print(dia_formatado, 'paguei 13o de', salario_atual, total)

    dia = dia + um_dia

print(total)


    