from componentes.objetosConteiner import criar_quadroCentral


def inserirAss(quadro_central, quadro_principal):
    quadro_central.destroy()
    criar_quadroCentral(quadro_principal)