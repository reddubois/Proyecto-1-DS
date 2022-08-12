import pandas as pd
import numpy as np

#Se importan los csv de cada uno de los departamentos
ALTA_VERAPAZ = pd.read_csv('ALTA VERAPAZ.csv')
BAJA_VERAPAZ = pd.read_csv('BAJA VERAPAZ.csv')
CHIMALTENANGO = pd.read_csv('CHIMALTENANGO.csv')
CHIQUIMULA = pd.read_csv('CHIQUIMULA.csv')
CIUDAD_CAPITAL = pd.read_csv('CIUDAD CAPITAL.csv')
EL_PROGRESO = pd.read_csv('EL PROGRESO.csv')
ESCUINTLA = pd.read_csv('ESCUINTLA.csv')
GUATEMALA = pd.read_csv('GUATEMALA.csv')
HUEHUETENANGO = pd.read_csv('HUEHUETENANGO.csv')
IZABAL = pd.read_csv('IZABAL.csv')
JALAPA = pd.read_csv('JALAPA.csv')
JUTIAPA = pd.read_csv('JUTIAPA.csv')
PETEN = pd.read_csv('PETEN.csv')
QUETZALTENANGO = pd.read_csv('QUETZALTENANGO.csv')
QUICHE = pd.read_csv('QUICHE.csv')
RETALHULEU = pd.read_csv('RETALHULEU.csv')
SACATEPEQUEZ = pd.read_csv('SACATEPEQUEZ.csv')
SAN_MARCOS = pd.read_csv('SAN MARCOS.csv')
SANTA_ROSA = pd.read_csv('SANTA ROSA.csv')
SOLOLA = pd.read_csv('SOLOLA.csv')
SUCHITEPEQUEZ = pd.read_csv('SUCHITEPEQUEZ.csv')
TOTONICAPAN = pd.read_csv('TOTONICAPAN.csv')
ZACAPA = pd.read_csv('ZACAPA.csv')

#Se concatenan todos los 22 dataframes
df = pd.concat([ALTA_VERAPAZ,BAJA_VERAPAZ,CHIMALTENANGO,CHIQUIMULA,CIUDAD_CAPITAL,
                EL_PROGRESO,ESCUINTLA,GUATEMALA,HUEHUETENANGO,IZABAL,
                JALAPA,JUTIAPA,PETEN,QUETZALTENANGO,QUICHE,
                RETALHULEU,SACATEPEQUEZ,SAN_MARCOS,SANTA_ROSA,SOLOLA,
                SUCHITEPEQUEZ,TOTONICAPAN,ZACAPA], axis=0, ignore_index=True)

#Listamos los nombres de las columnas
list(df.keys())

#Se borran todas las filas duplicadas
df=df.drop_duplicates()

#Observamos los establecimientos y códigos nulos
df['ESTABLECIMIENTO'].isna().sum()
df['CODIGO'].isna().sum()


#Botamos todas las filas con valores nulos en el código o establecimiento
df=df.dropna(subset = ['CODIGO', 'ESTABLECIMIENTO'])

print(df)

#Contamos las repeticiones de establecimientos
print(df.ESTABLECIMIENTO.value_counts())

#Removemos acentos
cols = df.select_dtypes(include=[object]).columns
df[cols] = df[cols].apply(lambda x: x.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8'))
print("\n",df.ESTABLECIMIENTO.value_counts())








# ZONA
# Actualmente, los establecimientos de la ciudad capital tienen en sus entradas de DEPARTAMENTO y MUNICIPIO valores distintos
# a los esperados, i.e. GUATEMALA Y CIUDAD DE GUATEMALA. En su lugar, DEPARTAMENTO guarda el municipio del establecimiento,
# mientras que MUNICIPIO guarda la zona de la capital en la que recide. La informacion de la zona se traslada a
# una nueva variable llamada ZONA, cuyas entradas son None para establecimientos fuera de la ciudad capital.

df = df.assign(ZONA = lambda x: np.where(x.DEPARTAMENTO == "CIUDAD CAPITAL", x.MUNICIPIO, None))

# MUNICIPIO
# Ahora, procedemos a corregir la informacion sobre los municipios de la ciudad capital.
# Las entradas de la variable MUNICIPIO para establecimientos fuera de la capital quedan invariantes. 

df = df.assign(MUNICIPIO = lambda x: np.where(x.DEPARTAMENTO == "CIUDAD CAPITAL", x.DEPARTAMENTO, x.MUNICIPIO))

# DEPARTAMENTO
# Se corrige la entrada de DEPARTAMENTO de los establecimientos en la ciudad capital, la cual se redefine a "GUATEMALA".
# Las entradas de la variable DEPARTAMENTO para establecimientos fuera de la capital quedan invariantes. 

df = df.assign(DEPARTAMENTO = lambda x: np.where(x.DEPARTAMENTO == "CIUDAD CAPITAL", "GUATEMALA", x.DEPARTAMENTO))

# DIRECCION
# Esta variable viene en multiples formatos, con diversidad de tipos de errores. Múltiples direcciones son muy breves,
# indicando incluso solo el barrio o la avenida en la que se encuentran. Sin embargo, se opta por mantener esta poca
# informacion en lugar de invalidar la direccion. En general, no se valida si la direccion de los establecimientos
# en realidad existe. Nos limitamos a validar direcciones claramente erroneas, constituidas por un par de
# caracteres invalidos, como "---". Este grupo de direcciones se redefinen a None,
# manteniendo la entrada de establecimiento en el set de datos.
# Una breve exploracion muestra que la dirección se presenta como algun elemento en el siguiente conjunto
# {"-", "--", "---", ".", ""}

setFaltasDireccion = ['-', '--', '---', '.', ' ', '  ']
df.DIRECCION = df.DIRECCION.replace(setFaltasDireccion, None)

# TELEFONO
# Multiples entradas de esta variable se encuentran sin datos. La forma en la que se
# representa la falta de dato puede ser variada, ya sea con caracteres especiales como un único cero.
# En otras ocasiones, el número sí es válido pero queda guardado con decimales, como 12345678.0.
# En otros casos, un establecimiento posee dos números telefónicos. 
# Para lidiar con todas estas posibles circunstancias, se valida la longitud del número telefónico, el cual
# esperamos que sea 8. Si una entrada posee 8 caracteres o más, botamos la cola del dato y nos quedamos con
# los primeros 8 caracteres. En cualquier otro caso, el número no se considera válido y la entrada se reemplaza por None. 

df['TELEFONO'] = df['TELEFONO'].apply(lambda x: str(x))
df['TELEFONO'] = df['TELEFONO'].apply(lambda x: x[0:8] if len(x) >= 8  else None)


#Contamos las repeticiones de directores
#print(df['DIRECTOR'].unique())
print(df.DIRECTOR.value_counts())

df = df.drop(df[df.DIRECTOR=="---"].index)
df = df.drop(df[df.DIRECTOR=="."].index)
df = df.drop(df[df.DIRECTOR=="--"].index)
df = df.drop(df[df.DIRECTOR=="----"].index)
df = df.drop(df[df.DIRECTOR=="-"].index)
df = df.drop(df[df.DIRECTOR==" "].index)
df = df.drop(df[df.DIRECTOR=="-----"].index)
df = df.drop(df[df.DIRECTOR=="SIN DATO"].index)
df = df.drop(df[df.DIRECTOR=="--------------"].index)


print("\n",df.DIRECTOR.value_counts())










