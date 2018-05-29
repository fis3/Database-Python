#TABLA  => string   |   CAMPOS => list  |   WHERE  => list  |   LIMIT => number
def select(tabla, campos="*", where="", limit=""):
    if campos != None : campos = str(campos).strip('[]') 
    if where : where = " WHERE {0} ".format(" AND ".join(where))
    if limit : limit = " LIMIT ", limit
    return """SELECT {campos} FROM {tabla} {where} {limit};""".format(campos=campos,tabla=tabla,where=where,limit=limit)

#TABLA  => string   |   CAMPOS => dict
def insert(tabla, campos):
    return """INSERT IGNORE INTO {tabla} ({campos}) VALUES ({valores});""".format(tabla=tabla, campos=str(campos.keys()).strip('[]'), valores=str(campos.values()).strip('[]'))

#TABLA  => string   |   WHERE  => list
def delete(tabla, where=""):
    if where : where = " WHERE {0} ".format(" AND ".join(where))
    return """DELETE FROM {tabla} {where};""".format(tabla=tabla,where=where)

## EJEMPLOS DE USO ##
#print insert("tabla1", {"id":"111","campo1":""})
#print select(tabla="tabla2",campos=["id","campo2"])
#print delete(tabla="tabla3",where=["1=1","True!=False"])
