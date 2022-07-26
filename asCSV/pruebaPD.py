import pandas as pd


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


df = pd.concat([ALTA_VERAPAZ,BAJA_VERAPAZ,CHIMALTENANGO,CHIQUIMULA,CIUDAD_CAPITAL,
                EL_PROGRESO,ESCUINTLA,GUATEMALA,HUEHUETENANGO,IZABAL,
                JALAPA,JUTIAPA,PETEN,QUETZALTENANGO,QUICHE,
                RETALHULEU,SACATEPEQUEZ,SAN_MARCOS,SANTA_ROSA,SOLOLA,
                SUCHITEPEQUEZ,TOTONICAPAN,ZACAPA], axis=0, ignore_index=True)

print(df.ESTABLECIMIENTO.value_counts())

list(df.keys())




