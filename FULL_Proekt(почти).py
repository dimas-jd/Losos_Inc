# перечисление переменных
S78n = complex(7.116, 3.77)
S912n = complex(13.937, 9.831)
S710 = complex(15.602, 10.757)
S1112 = complex(8.422, 4.522)

N1 = complex(-1)
N2 = complex(-2)
N3 = complex(0)
N4 = complex(-1)
N5 = complex(-9)
N6 = complex(-9)
N7 = complex(-9)
N8 = complex(-9)
N9 = complex(-1)
N10 = complex(-9)
N11 = complex(1)
N12 = complex(1)

# Страница 1
# Ввод с экрана мощностей в МВар
Qku1 = complex(input())
Qku2 = complex(input())
Qku3 = complex(input())
Qku4 = complex(input())
Qku5 = complex(input())
Qku6 = complex(input())
Qku7 = complex(input())
Qku8 = complex(input())
Qku9 = complex(input())
Qku10 = complex(input())
Qku11 = complex(input())
Qku12 = complex(input())

# Удельные сопротивления, проводимости и длины линий
zud185 = complex(0.198, 0.42)
zud150 = complex(0.204, 0.42)
zud120 = complex(0.244, 0.427)
bud185 = complex(2.7 * (10 ** (-6)))
bud150 = complex(2.707 * (10 ** (-6)))
bud120 = complex(2.658 * (10 ** (-6)))
n = complex(2)
Lip1 = complex(30)
L12 = complex(9)
L1011 = complex(14)
L23 = complex(5)
L34 = complex(13)
L912 = complex(18)
L45 = complex(37)
L56 = complex(45)
L1112 = complex(28)
L67 = complex(12)
L78 = complex(35)
L04 = complex(25)
L89 = complex(34)
L710 = complex(12)
L012 = complex(11)

# 2.Напряжения
U0 = complex(115)
UHH = complex(10)
UGEL = complex(10.5)
t = complex(0.0178)

# Параметры трансформатора
Z25 = complex(0.5 * (complex(2.54, 55.9)))
Z16 = complex(0.5 * (complex(4.38, 86.7)))
Z10 = complex(0.5 * (complex(7.95, 139)))
dSxx25 = complex(2 * complex(0.027, 0.175))
dSxx16 = complex(2 * complex(0.019, 0.112))
dSxx10 = complex(2 * complex(0.014, 0.07))
K25 = complex(115 / 11)
K16 = complex(115 / 11)
K10 = complex(115 / 11)

# Максимальные нагрузки подстанций
S1 = complex(16.77, (7.75 - Qku1))
S2 = complex(15.39, (10.3 - Qku2))
S3 = complex(10.5, (4.99 - Qku3))
S4 = complex(9.8, (4.37 - Qku4))
S5 = complex(17.38, (7.75 - Qku5))
S6 = complex(10.27, (4.5 - Qku6))
S7 = complex(5.98, (2.75 - Qku7))
S8 = complex(6.98, (3.18 - Qku8))
S9 = complex(13.8, (10.67 - Qku9))
S10 = complex(12.05, (10.34 - Qku10))
S11 = complex(11.83, (4.34 - Qku11))
S12 = complex(7.33, (5.03 - Qku12))

# функция для округления:
def Round (a):
    r = complex(round(a.real, 3), round(a.imag, 3))
    return r


# Страница 2
# Функция расчёта z
def z(zud, l):
    result = (zud * l)
    return result

# Функция расчёта zip
def Zip(zud, l, n):
    result = complex(zud * l / n)
    return result

# Обращение к функции z
Z710 = z(zud120, L710)
Z1112 = z(zud120, L1112)
Z1011 = z(zud120, L1011)
Z67 = z(zud120, L67)
Z45 = z(zud120, L45)
Z78 = z(zud120, L78)
Z912 = z(zud120, L912)
Z89 = z(zud120, L89)
Z56 = z(zud120, L56)
Z04 = z(zud185, L04)

print('')
print('Страница 2')
print('Z710 =', Round(Z710))
print('Z1112 =', Round(Z1112))
print('Z1011 =', Round(Z1011))
print('Z67 =', Round(Z67))
print('Z45 =', Round(Z45))
print('Z78 =', Round(Z78))
print('Z912 =', Round(Z912))
print('Z89 =', Round(Z89))
print('Z56 =', Round(Z56))
print('Z04 =', Round(Z04))

# Обращение к функции Zip
Zip1 = Zip(zud185, Lip1, n)
Z12 = Zip(zud185, L12, n)
Z012 = Zip(zud185, L012, n)
Z23 = Zip(zud185, L23, n)
Z34 = Zip(zud185, L34, n)

print('Zip1 =', Round(Zip1))
print('Z12 =', Round(Z12))
print('Z012 =', Round(Z012))
print('Z23 =', Round(Z23))
print('Z34 =', Round(Z34))

# функция расчёта Qc
def Qc(u, bud, l):
    result = 0.5 * (u * u) * bud * l
    return result

# Функция расчета Qcs
def Qcs(u, bud, l, n):
    result = 0.5 * (u * u) * bud * l * n
    return result

# Обращение к функции Qc
Qc04 = Qc(U0, bud185, L04)
Qc45 = Qc(U0, bud120, L45)
Qc56 = Qc(U0, bud120, L56)
Qc67 = Qc(U0, bud120, L67)
Qc78 = Qc(U0, bud120, L78)
Qc710 = Qc(U0, bud120, L710)
Qc89 = Qc(U0, bud120, L89)
Qc1011 = Qc(U0, bud120, L1011)
Qc912 = Qc(U0, bud120, L912)
Qc1112 = Qc(U0, bud120, L1112)

print('')
print('Qc04 =', Round(Qc04), 'Мвар')
print('Qc45 =', Round(Qc45), 'Мвар')
print('Qc56 =', Round(Qc56), 'Мвар')
print('Qc67 =', Round(Qc67), 'Мвар')
print('Qc78 =', Round(Qc78), 'Мвар')
print('Qc710 =', Round(Qc710), 'Мвар')
print('Qc89 =', Round(Qc89), 'Мвар')
print('Qc1011 =', Round(Qc1011), 'Мвар')
print('Qc912 =', Round(Qc912), 'Мвар')
print('Qc1112 =', Round(Qc1112), 'Мвар')

# Обращение к фукции Qcs
Qc012 = Qcs(U0, bud185, L012, n)
Qsip1 = Qcs(U0, bud185, Lip1, n)
Qc12 = Qcs(U0, bud185, L12, n)
Qc23 = Qcs(U0, bud185, L23, n)
Qc34 = Qcs(U0, bud185, L34, n)

print('Qc012 =', Round(Qc012), 'Мвар')
print('Qsip1 =', Round(Qsip1), 'Мвар')
print('Qc12 =', Round(Qc12), 'Мвар')
print('Qc23 =', Round(Qc23), 'Мвар')
print('Qc34 =', Round(Qc34), 'Мвар')


# Страница 3
# Функция рассчета Spr
def Spr(s, U, z, dsxx):
    result = s + (abs(s ** 2) / (U ** 2)) * z + dsxx
    return result

# Оращение к функции Spr
Spr1 = Spr(S1, U0, Z16, dSxx16)
Spr2 = Spr(S2, U0, Z16, dSxx16)
Spr3 = Spr(S3, U0, Z25, dSxx25)
Spr4 = Spr(S4, U0, Z25, dSxx25)
Spr5 = Spr(S5, U0, Z10, dSxx10)
Spr6 = Spr(S6, U0, Z16, dSxx16)
Spr7 = Spr(S7, U0, Z16, dSxx16)
Spr8 = Spr(S8, U0, Z16, dSxx16)
Spr9 = Spr(S9, U0, Z16, dSxx16)
Spr10 = Spr(S10, U0, Z16, dSxx16)
Spr11 = Spr(S11, U0, Z16, dSxx16)
Spr12 = Spr(S12, U0, Z16, dSxx16)

print('')
print('Страница 3')
print('Spr1 =', Round(Spr1), 'МВА')
print('Spr2 =', Round(Spr2), 'МВА')
print('Spr3 =', Round(Spr3), 'МВА')
print('Spr4 =', Round(Spr4), 'МВА')
print('Spr5 =', Round(Spr5), 'МВА')
print('Spr6 =', Round(Spr6), 'МВА')
print('Spr7 =', Round(Spr7), 'МВА')
print('Spr8 =', Round(Spr8), 'МВА')
print('Spr9 =', Round(Spr9), 'МВА')
print('Spr10 =', Round(Spr10), 'МВА')
print('Spr11 =', Round(Spr11), 'МВА')
print('Spr12 =', Round(Spr12), 'МВА')


# Cтраница 4
# Функция вычисления Sp1-3,5-6, 8-11
def Sp(Spr, Qcup, Qc):
    result = Spr - complex(0, 1) * Qcup - complex(0, 1) * Qc
    return result

# Функция вычисления Sp4, Sp7, Sp12
def Sp47(Spr, Qc, Qcc, Qccc):
    result = Spr - complex(0, 1) * Qc - complex(0, 1) * Qcc - complex(0, 1) * Qccc
    return result

# Обращение к функции Sp
Sr1 = Sp(Spr1, Qsip1, Qc12)
Sr2 = Sp(Spr2, Qc12, Qc23)
Sr3 = Sp(Spr3, Qc23, Qc34)
Sr5 = Sp(Spr5, Qc56, Qc45)
Sr6 = Sp(Spr6, Qc56, Qc67)
Sr8 = Sp(Spr8, Qc89, Qc78)
Sr9 = Sp(Spr9, Qc89, Qc912)
Sr10 = Sp(Spr10, Qc710, Qc1011)
Sr11 = Sp(Spr10, Qc1112, Qc1011)

# Обращение к функции Sp47
Sr4 = Sp47(Spr4, Qc34, Qc04, Qc45)
Sr7 = Sp47(Spr7, Qc67, Qc78, Qc710)
Sr12 = Sp47(Spr12, Qc912, Qc1112, Qc012)

print('')
print('Страница 4')
print('Sr1 =', Round(Sr1), 'МВА')
print('Sr2 =', Round(Sr2), 'МВА')
print('Sr3 =', Round(Sr3), 'МВА')
print('Sr4 =', Round(Sr4), 'МВА')
print('Sr5 =', Round(Sr5), 'МВА')
print('Sr6 =', Round(Sr6), 'МВА')
print('Sr7 =', Round(Sr7), 'МВА')
print('Sr8 =', Round(Sr8), 'МВА')
print('Sr9 =', Round(Sr9), 'МВА')
print('Sr10 =', Round(Sr10), 'МВА')
print('Sr11 =', Round(Sr11), 'МВА')
print('Sr12 =', Round(Sr12), 'МВА')

# Функция рассчета формулы
def Ss(Sp, Spp, z1, z2, z3):
    result = (Sp * (z1 + z2) + Spp * z2) / (z1 + z2 + z3)
    return result

# Обращение к функции рассчета формулы
S78 = Ss(Sr8, Sr9, Z89, Z912, Z78)
S912 = Ss(Sr9, Sr8, Z89, Z78, Z912)

# S89
S89 = S78 - Sr8

print('')
print('S78 =', Round(S78))
print('S912 =', Round(S912))
print('S89 =', Round(S89))


# страница 6
# создание функции
def Delta(a, b, c):
    delta = (abs(a * a) / (b * b)) * c
    return delta

# вычисление значений
# Потоки мощности на участке 7-10-11-12 с учетом потерь
S710k = S710
dS710 = Delta(S710k, U0, Z710)
S710n = S710k + dS710
S1011k = S710n + Sr10
dS1011 = Delta(S1011k, U0, Z1011)
S1011n = S1011k + dS1011
S1112k = S1112
dS1112 = Delta(S1112k, U0, Z1112)
S1112n = S1112k + dS1112

# Потоки мощности на участке ИП1-12 с учетом потерь
S012k = S1112n + S912n + Sr12
dS012 = Delta(S012k, U0, Z012)
S012n = S012k + dS012

# Потоки мощности на участке 6-7 с учетом потерь
S67k = S78n + S710n + Sr7
dS67 = Delta(S67k, U0, Z67)
S67n = S67k + dS67

# вывод результатов на экран
print('Страница 6')
print('Потеря мощности:', '           Поток в ЛЭП мощности:')
print('dS710 =', Round(dS710), 'MBA', '  S710n =', Round(S710n), 'MBA')
print('dS1011 =', Round(dS1011), 'MBA', 'S1011n =', Round(S1011n), 'MBA')
print('dS1112 =', Round(dS1112), 'MBA', 'S1112n =', Round(S1112n), 'MBA')
print('dS012 =', Round(dS012), 'MBA', ' S012n =', Round(S012n), 'MBA')
print('dS67 =', Round(dS67), 'MBA', '  S67n =', Round(S67n), 'MBA')


# Страница 7
# вычисление значений
# Потоки мощности на участке 5-6 с учетом потерь
S56k = S67n + Sr6
dS56 = Delta(S56k, U0, Z56)
S56n = S56k + dS56

# Потоки мощности на участке 4-5 с учетом потерь
S45k = S56n + Sr5
dS45 = Delta(S45k, U0, Z45)
S45n = S45k + dS45

# Потоки мощности на участке 7-10-11-12 без учета потерь
Sip1 = ((Sr1 * (Z12.conjugate() + Z23.conjugate() + Z34.conjugate() + Z04.conjugate()))
        + (Sr2 * (Z23.conjugate() + Z34.conjugate() + Z04.conjugate())) + (Sr3 * (Z34.conjugate() + Z04.conjugate()))
        + (Sr4 + S45n) * Z04.conjugate()) / (Zip1.conjugate() + Z12.conjugate() + Z23.conjugate()
                                             + Z34.conjugate() + Z04.conjugate())
S04 = ((Sr4 + S45n) * (Z12.conjugate() + Z23.conjugate() + Z34.conjugate() + Zip1.conjugate()) +
       (Sr3 * (Z23.conjugate() + Z12.conjugate() + Zip1.conjugate())) + (Sr2 * (Z12.conjugate() + Zip1.conjugate()))
       + Sr1 * Zip1.conjugate()) / (Zip1.conjugate() + Z12.conjugate() + Z23.conjugate()
                                    + Z34.conjugate() + Z04.conjugate())
S12 = Sip1 - Sr1
S23 = S12 - Sr2
S34 = S23 - Sr3

# вывод результатов на экран
print('')
print('Страница 7')
print('Потеря мощности:', '           Поток в ЛЭП мощности:')
print('dS56 =', Round(dS56), 'MBA', '  S56n =', Round(S56n), 'MBA')
print('dS45 =', Round(dS45), 'MBA', '  S45n =', Round(S45n), 'MBA')
print('')
print('Sip1 =', Round(Sip1), 'MBA')
print('S04 =', Round(S04), 'MBA')
print('S12 =', Round(S12), 'MBA')
print('S23 =', Round(S23), 'MBA')
print('S34 =', Round(S34), 'MBA')


# Страница 8
# создание функции
def S (S_n, U_n, Z_n):
    sss = abs((S_n**2)) / (U_n**2) * Z_n
    return sss

# вычисление значений
# Потоки мощности на участке 0-4 с учетом потерь:
S04k = S04
dS04 = S(S04k, U0, Z04)
S04n = S04k + dS04

# Потоки мощности на участке 3-4 с учетом потерь:
S34k = S34
dS34 = S(S34k, U0, Z34)
S34n = S34k + dS34

# Потоки мощности на участке 2-3 с учетом потерь:
S23k = S34n + Sr3
dS23 = S(S23k, U0, Z23)
S23n = S23k + dS23

# Потоки мощности на участке 1-2 с учетом потерь:
S12k = S23n + Sr2
dS12 = S(S12k, U0, Z12)
S12n = S12k + dS12

# Потоки мощности на участке ип-1 с учетом потерь:
Sip1k = S12n + Sr1
dSip1 = S(Sip1k, U0, Zip1)
Sip1n = Sip1k + dSip1

# вывод результатов на экран
print('')
print('Страница 8')
print('Потеря мощности:', '           Поток в ЛЭП мощности:')
print('dS04 =', Round(dS04), 'МВА', '  S04n =', Round(S04n), 'МВА')
print('dS34 =', Round(dS34), 'МВА', '  S34n =', Round(S34n), 'МВА')
print('dS23 =', Round(dS23), 'МВА', '  S23n =', Round(S23n), 'МВА')
print('dS12 =', Round(dS12), 'МВА', '  S12n =', Round(S12n), 'МВА')
print('dSip1 =', Round(dSip1), 'МВА', ' Sip1n =', Round(Sip1n), 'МВА')


# Страница 9
# Определяем напряжения в узлах на высоких сторонах подстанций

# создание функции
def U (U_n, S_n, U_n2, Z_n):
    qwe = U_n - (S_n.conjugate() / U_n2.conjugate() * Z_n)
    return qwe

# вычисление значений
U1 = U(U0, Sip1n, U0, Zip1)
U2 = U(U1, S12n, U1, Z12)
U3 = U(U2, S23n, U2, Z23)
U4 = U(U0, S04n, U0, Z04)
U5 = U(U4, S45n, U4, Z45)
U6 = U(U5, S56n, U5, Z56)
U7 = U(U5, S56n, U6, Z56)
U8 = U(U7, S78n, U7, Z78)
U10 = U(U7, S710n, U7, Z710)
U12 = U(U0, S012n, U0, Z710)
U11 = U(U12, S1112n, U12, Z1112)
U9 = U(U12, S912n, U12, Z912)

# вывод результатов на экран
print()
print('Страница 9')
print('Напряжениe в узлах:')
print('U1 =', Round(U1), 'кВ', '', '|U1| =', round(abs(U1), 3), 'кВ')
print('U2 =', Round(U2), 'кВ', '', '|U2| =', round(abs(U2), 3), 'кВ')
print('U3 =', Round(U3), 'кВ', '', '|U3| =', round(abs(U3), 3), 'кВ')
print('U4 =', Round(U4), 'кВ', '', '|U4| =', round(abs(U4), 3), 'кВ')
print('U5 =', Round(U5), 'кВ', ' ', '|U5| =', round(abs(U5), 3), 'кВ')
print('U6 =', Round(U6), 'кВ', '', '|U6| =', round(abs(U6), 3), 'кВ')
print('U7 =', Round(U7), 'кВ', '', '|U7| =', round(abs(U7), 3), 'кВ')
print('U8 =', Round(U8), 'кВ', '', '|U8| =', round(abs(U8), 3), 'кВ')
print('U9 =', Round(U9), 'кВ', '', '|U9| =', round(abs(U9), 3), 'кВ')
print('U10 =', Round(U10), 'кВ', '|U10| =', round(abs(U10), 3), 'кВ')
print('U11 =', Round(U11), 'кВ', '|U11| =', round(abs(U11), 3), 'кВ')
print('U12 =', Round(U12), 'кВ', '|U12| =', round(abs(U12), 3), 'кВ')


# Страница 10
# Сравниваем полученные значения напряжений в узлах на высоких сторонах подстанций с использованным начальным приближением
# создание функции
def U01 (U_ABS, U_0):
    UUU = (abs(U_ABS) - U_0) / U_0 * 100
    return UUU

# вычисление значений
UFirst = U01(U1, U0)
USecond = U01(U2, U0)
UThird = U01(U3, U0)
UFourth = U01(U4, U0)
UFifth = U01(U5, U0)
USixth = U01(U6, U0)
USeventh = U01(U7, U0)
UEighth = U01(U8, U0)
UNinth = U01(U9, U0)
UTenth = U01(U10, U0)

# вывод результатов на экран
print('')
print('Страница 10')
print('Отклонение напряжения в узлах:')
print("1.1 =", complex(round(UFirst.real, 4)), '%')
print("1.2 =", complex(round(USecond.real, 4)), '%')
print("1.3 =", complex(round(UThird.real, 4)), '%')
print("1.4 =", complex(round(UFourth.real, 4)), '%')
print("1.5 =", complex(round(UFifth.real, 4)), '%')
print("1.6 =", complex(round(USixth.real, 4)), '%')
print("1.7 =", complex(round(USeventh.real, 4)), '%')
print("1.8 =", complex(round(UEighth.real, 4)), '%')
print("1.9 =", complex(round(UNinth.real, 4)), '%')
print("1.10 =", complex(round(UTenth.real, 4)), '%')

# Находим значения потоков мощностей, втекающих в обмотку ВН трансформаторов
# создание функции
def SVN (Spr, Sxx):
    Transformator = Spr - Sxx
    return Transformator

# вычисление значений
SVN_1 = SVN(Spr1, dSxx16)
SVN_2 = SVN(Spr2, dSxx16)
SVN_3 = SVN(Spr3, dSxx25)
SVN_4 = SVN(Spr4, dSxx25)
SVN_5 = SVN(Spr5, dSxx10)
SVN_6 = SVN(Spr6, dSxx16)
SVN_7 = SVN(Spr7, dSxx16)
SVN_8 = SVN(Spr8, dSxx16)
SVN_9 = SVN(Spr9, dSxx16)
SVN_10 = SVN(Spr10, dSxx16)
SVN_11 = SVN(Spr11, dSxx16)
SVN_12 = SVN(Spr12, dSxx16)

# вывод результатов на экран
print('')
print('Потоки мощностей, втекающих в обмотку ВН трансформаторов:')
print('SVN_1 =', Round(SVN_1), 'МВА')
print('SVN_2 =', Round(SVN_2), 'МВА')
print('SVN_3 =', Round(SVN_3), 'МВА')
print('SVN_4 =', Round(SVN_4), 'МВА')
print('SVN_5 =', Round(SVN_5), 'МВА')
print('SVN_6 =', Round(SVN_6), 'МВА')
print('SVN_7 =', Round(SVN_7), 'МВА')
print('SVN_8 =', Round(SVN_8), 'МВА')
print('SVN_9 =', Round(SVN_9), 'МВА')
print('SVN_10 =', Round(SVN_10), 'МВА')
print('SVN_11 =', Round(SVN_11), 'МВА')
print('SVN_12 =', Round(SVN_12), 'МВА')


# Страница 11
# Напряжение на низкой стороне подстанций, приведенные к стороне ВН
# создание функции
def zxc (U_n, a, b, z_n):
    Uhh_bh = abs(U_n - (a.conjugate() / b.conjugate()) * z_n)
    return Uhh_bh

# вычисление значений
UNN_VN1 = zxc(U1, SVN_1, U1, Z16)
UNN_VN2 = zxc(U2, SVN_2, U2, Z16)
UNN_VN3 = zxc(U3, SVN_3, U3, Z25)
UNN_VN4 = zxc(U4, SVN_4, U4, Z25)
UNN_VN5 = zxc(U5, SVN_5, U5, Z10)
UNN_VN6 = zxc(U6, SVN_6, U6, Z16)
UNN_VN7 = zxc(U7, SVN_7, U7, Z16)
UNN_VN8 = zxc(U8, SVN_8, U8, Z16)
UNN_VN9 = zxc(U9, SVN_9, U9, Z16)
UNN_VN10 = zxc(U10, SVN_10, U10, Z16)
UNN_VN11 = zxc(U11, SVN_11, U11, Z16)
UNN_VN12 = zxc(U12, SVN_12, U12, Z16)

# вывод результатов на экран
print('')
print('Страница 11')
print('Напряжение на низкой стороне подстанций, приведенные к стороне ВН:')
print('UNN_VN1 =', Round(UNN_VN1), 'кВ')
print('UNN_VN3 =', Round(UNN_VN3), 'кВ')
print('UNN_VN4 =', Round(UNN_VN4), 'кВ')
print('UNN_VN5 =', Round(UNN_VN5), 'кВ')
print('UNN_VN6 =', Round(UNN_VN6), 'кВ')
print('UNN_VN7 =', Round(UNN_VN7), 'кВ')
print('UNN_VN8 =', Round(UNN_VN8), 'кВ')
print('UNN_VN9 =', Round(UNN_VN9), 'кВ')
print('UNN_VN10 =', Round(UNN_VN10), 'кВ')
print('UNN_VN11 =', Round(UNN_VN11), 'кВ')
print('UNN_VN12 =', Round(UNN_VN12), 'кВ')


# Страница 12
# Определение напряжения на шинах НН подстанций
def Unn (Un, Kn):
    asdfg = Un / Kn
    return asdfg

UHH1 = Unn(UNN_VN1, K16)
UHH2 = Unn(UNN_VN2, K16)
UHH3 = Unn(UNN_VN3, K25)
UHH4 = Unn(UNN_VN4, K25)
UHH5 = Unn(UNN_VN5, K10)
UHH6 = Unn(UNN_VN6, K16)
UHH7 = Unn(UNN_VN7, K16)
UHH8 = Unn(UNN_VN8, K16)
UHH9 = Unn(UNN_VN9, K16)
UHH10 = Unn(UNN_VN10, K16)
UHH11 = Unn(UNN_VN11, K16)
UHH12 = Unn(UNN_VN12, K16)

print('')
print('Страница 12')
print('UHH1 =', Round(UHH1), 'кВ')
print('UHH2 =', Round(UHH2), 'кВ')
print('UHH3 =', Round(UHH3), 'кВ')
print('UHH4 =', Round(UHH4), 'кВ')
print('UHH5 =', Round(UHH5), 'кВ')
print('UHH6 =', Round(UHH6), 'кВ')
print('UHH7 =', Round(UHH7), 'кВ')
print('UHH8 =', Round(UHH8), 'кВ')
print('UHH9 =', Round(UHH9), 'кВ')
print('UHH10 =', Round(UHH10), 'кВ')
print('UHH11 =', Round(UHH11), 'кВ')
print('UHH12 =', Round(UHH12), 'кВ')

# Отклонение напряжения на стороне низкого напряжения
def qwe (UHH_1, UH_H):
    qwerty = (((abs(UHH_1) - UH_H)) / UH_H) * 100
    return qwerty

UH1 = qwe(UHH1, UHH)
UH2 = qwe(UHH2, UHH)
UH3 = qwe(UHH3, UHH)
UH4 = qwe(UHH4, UHH)
UH5 = qwe(UHH5, UHH)
UH6 = qwe(UHH6, UHH)
UH7 = qwe(UHH7, UHH)
UH8 = qwe(UHH8, UHH)
UH9 = qwe(UHH9, UHH)
UH10 = qwe(UHH10, UHH)
UH11 = qwe(UHH11, UHH)
UH12 = qwe(UHH12, UHH)

print('')
print("UH1 =", Round(UH1), "%")
print("UH2 =", Round(UH2), "%")
print("UH3 =", Round(UH3), "%")
print("UH4 =", Round(UH4), "%")
print("UH5 =", Round(UH5), "%")
print("UH6 =", Round(UH6), "%")
print("UH7 =", Round(UH7), "%")
print("UH8 =", Round(UH8), "%")
print("UH9 =", Round(UH9), "%")
print("UH10 =", Round(UH10), "%")
print("UH11 =", Round(UH11), "%")
print("UH12 =", Round(UH12), "%")

# Страница 13
# Определение желаемых коэффициентов трансформации
def asd (UHHVN_1, U_GEL):
    rewq = (UHHVN_1 / U_GEL)
    return rewq

KGEL1 = asd(UNN_VN1, UGEL)
KGEL2 = asd(UNN_VN2, UGEL)
KGEL3 = asd(UNN_VN3, UGEL)
KGEL4 = asd(UNN_VN4, UGEL)
KGEL5 = asd(UNN_VN5, UGEL)
KGEL6 = asd(UNN_VN6, UGEL)
KGEL7 = asd(UNN_VN7, UGEL)
KGEL8 = asd(UNN_VN8, UGEL)
KGEL9 = asd(UNN_VN9, UGEL)
KGEL10 = asd(UNN_VN10, UGEL)
KGEL11 = asd(UNN_VN11, UGEL)
KGEL12 = asd(UNN_VN12, UGEL)

print("")
print('Страница 13')
print("KGEL1 =", complex(round(KGEL1.real, 3)))
print("KGEL2 =", complex(round(KGEL2.real, 3)))
print("KGEL3 =", complex(round(KGEL3.real, 3)))
print("KGEL4 =", complex(round(KGEL4.real, 3)))
print("KGEL5 =", complex(round(KGEL5.real, 3)))
print("KGEL6 =", complex(round(KGEL6.real, 3)))
print("KGEL7 =", complex(round(KGEL7.real, 3)))
print("KGEL8 =", complex(round(KGEL8.real, 3)))
print("KGEL9 =", complex(round(KGEL9.real, 3)))
print("KGEL10 =", complex(round(KGEL10.real, 3)))
print("KGEL11 =", complex(round(KGEL11.real, 3)))
print("KGEL12 =", complex(round(KGEL12.real, 3)))

# Определение требуемых номеров отпаек РПН, округляя желаемые значения номеров отпаек до ближайших возможных стандартных значений
def asd (KGEL, K_16, t):
    reqw = (KGEL / K_16 - 1) * 1 / t
    return reqw

NGEL1 = asd(KGEL1, K16, t)
NGEL2 = asd(KGEL2, K16, t)      
NGEL3 = asd(KGEL3, K25, t)  
NGEL4 = asd(KGEL4, K25, t)  
NGEL5 = asd(KGEL5, K10, t) 
NGEL6 = asd(KGEL6, K16, t)  
NGEL7 = asd(KGEL7, K16, t)  
NGEL8 = asd(KGEL8, K16, t)  
NGEL9 = asd(KGEL9, K16, t)  
NGEL10 = asd(KGEL10, K16, t)  
NGEL11 = asd(KGEL11, K16, t)  
NGEL12 = asd(KGEL12, K16, t) 

print("")
print("NGEL1 = ", complex(round(NGEL1.real, 3)))
print("NGEL2 = ", complex(round(NGEL2.real, 3)))
print("NGEL3 = ", complex(round(NGEL3.real, 3)))
print("NGEL4 = ", complex(round(NGEL4.real, 3)))
print("NGEL5 = ", complex(round(NGEL5.real, 3)))
print("NGEL6 = ", complex(round(NGEL6.real, 3)))
print("NGEL7 = ", complex(round(NGEL7.real, 3)))
print("NGEL8 = ", complex(round(NGEL8.real, 3)))
print("NGEL9 = ", complex(round(NGEL9.real, 3)))
print("NGEL10 = ", complex(round(NGEL10.real, 3)))
print("NGEL11 = ", complex(round(NGEL11.real, 3)))
print("NGEL12 = ", complex(round(NGEL12.real, 3)))

# Страница 14
# Находим фактические напряжения на шинах подстанций на стороне НН после регулирования:
# Вывод на экран: напряжение на низкой стороне
def asd (UHHBH_1, K_1, N, t):
    erwq = (UHHBH_1 / (K_1 * (1 + N * t)))
    return erwq

UHH_1 = asd(UNN_VN1, K16, N1, t)
UHH_2 = asd(UNN_VN2, K16, N2, t)
UHH_3 = asd(UNN_VN3, K25, N3, t)
UHH_4 = asd(UNN_VN4, K25, N4, t)
UHH_5 = asd(UNN_VN5, K10, N5, t)
UHH_6 = asd(UNN_VN6, K16, N6, t)
UHH_7 = asd(UNN_VN7, K16, N7, t)
UHH_8 = asd(UNN_VN8, K16, N8, t)
UHH_9 = asd(UNN_VN9, K16, N9, t)
UHH_10 = asd(UNN_VN10, K16, N10, t)
UHH_11 = asd(UNN_VN11, K16, N11, t)
UHH_12 = asd(UNN_VN12, K16, N12, t)

print("")
print('Страница 14')
print("UHH_1 =", complex(round(UHH_1.real, 3)))
print("UHH_2 =", complex(round(UHH_2.real, 3)))
print("UHH_3 =", complex(round(UHH_3.real, 3)))
print("UHH_4 =", complex(round(UHH_4.real, 3)))
print("UHH_5 =", complex(round(UHH_5.real, 3)))
print("UHH_6 =", complex(round(UHH_6.real, 3)))
print("UHH_7 =", complex(round(UHH_7.real, 3)))
print("UHH_8 =", complex(round(UHH_8.real, 3)))
print("UHH_9 =", complex(round(UHH_9.real, 3)))
print("UHH_10 =", complex(round(UHH_10.real, 3)))
print("UHH_11 =", complex(round(UHH_11.real, 3)))
print("UHH_12 =", complex(round(UHH_12.real, 3)))