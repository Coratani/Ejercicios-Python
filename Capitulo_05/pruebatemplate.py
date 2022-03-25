from string import Template

plantilla=Template(
    'la ciudad de $ciudad aporta $$$cantidad al proyecto ${proyecto}landia.')
ciudad1=plantilla.substitute(ciudad='New York', proyecto="Cepi",
                             cantidad='150000')
ciudad2=plantilla.substitute(cantidad='1570000',ciudad='boston',
                            proyecto='python')
print(ciudad1)
print(ciudad2)

plantilladev= Template('Devolver $articulo a $origen')
devol1=plantilladev.safe_substitute(articulo='Exprimidor phillips',
                                    origen='enteramarkt')
devol2=plantilladev.safe_substitute(articulo='cafetera clooney')
print(devol1)
print(devol2)