# TABLA DE VERDAD
#   E400    E100     E4     S
#     0       0      0      0
#     0       0      1      1
#     0       1      0      0
#     0       1      1      0
#     1       0      0      0
#     1       0      1      0
#     1       1      0      0
#     1       1      1      1
#
#   Solo tenemos dos casos, nE400·nE100·E4 + E4·E100·E400 = S
#   La salida de la función será la operación lógica anterior
#   Comprobamos si es o no es bisiesto usando una lista de todos los años bisiestos desde el 1584. Si en algún momento da FALSE, rompemos el bucle y lloramos en un rincón :(
#   Testeo2 tiene un año "troll", comprobar el funcionamiento de bisiesto() con las dos listas.
#   Pido disculpas de antemano por las bromas sin gracia. 

testeo =  [1584, 1588, 1592, 1596, 1600, 1604, 1608, 1612, 1616, 1620, 1624, 1628, 1632, 1636, 1640, 1644, 1648, 1652, 1656, 1660, 1664, 1668, 1672, 1676, 1680, 1684, 1688, 1692, 1696, 1704, 1708, 1712, 1716, 1720, 1724, 1728, 1732, 1736, 1740, 1744, 1748, 1752, 1756, 1760, 1764, 1768, 1772, 1776, 1780, 1784, 1788, 1792, 1796, 1804, 1808, 1812, 1816, 1820, 1824, 1828, 1832, 1836, 1840, 1844, 1848, 1852, 1856, 1860, 1864, 1868, 1872, 1876, 1880, 1884, 1888, 1892, 1896, 1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]
testeo2 =  [1584, 1588, 1592, 1596, 1600, 1604, 1608, 1612, 1616, 1620, 1624, 1628, 1632, 1636, 1640, 1644, 1648, 1652, 1656, 2001, 1660, 1664, 1668, 1672, 1676, 1680, 1684, 1688, 1692, 1696, 1704, 1708, 1712, 1716, 1720, 1724, 1728, 1732, 1736, 1740, 1744, 1748, 1752, 1756, 1760, 1764, 1768, 1772, 1776, 1780, 1784, 1788, 1792, 1796, 1804, 1808, 1812, 1816, 1820, 1824, 1828, 1832, 1836, 1840, 1844, 1848, 1852, 1856, 1860, 1864, 1868, 1872, 1876, 1880, 1884, 1888, 1892, 1896, 1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]

def bisiesto(anio):
    entre4      =   anio % 4 == 0
    entre100    =   anio % 100 == 0
    entre400    =   anio % 400 == 0  
    return (entre4 & (not entre100) & (not entre400)) | (entre4 & entre100 & entre400) 

#   Comprobación
for anio in range(0,len(testeo)):
    if(bisiesto(testeo[anio])):
        print("ok")
    else:
        print("(ノಠ益ಠ)ノ彡┻━┻")
        break
else:
    print("Todos los anios son bisiestos. Regocíjate, tu función funciona... jeje... ¿lo pillas? tu función... funciona... ejejejejeje")