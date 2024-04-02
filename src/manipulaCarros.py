import manipulaCSV as mcsv
import apresentacao

def carregar() -> list :
    '''
    Carrega o arquivo de Carro.csv numa lista
    
    Retorno
    -------
    Retorna uma lista vazia caso o arquivo não exista ou 
    uma lista de dicionários contendo os dados dos clientes
    '''
    lista = mcsv.carregarDados("LocadoradeCarros/Carro.csv")
    return lista


def cadastrar( listaCarros : list) -> bool :
    '''
    Rotina para cadastrar um carro

    Parâmetros
    ----------
    listaClientes: Lista atual dos carros

    Retorno
    -------
    Retorna True se o carro foi cadastrado com sucesso
    '''
    carro = apresentacao.CadastrarCarro()
    listaCarros.append(carro)
    print(listaCarros)
    return mcsv.gravarDados('LocadoradeCarros/Carro.csv', carro.keys(), listaCarros )