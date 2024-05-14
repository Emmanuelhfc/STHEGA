
from numpy import array
def avaliacao_trocador_mono():
    ...

def bin(matrix):
    """ Converte a matrix de bin para int

    Args:
        matrix (_type_): _description_

    Returns:
        _type_: _description_
    """
    coluns_number = matrix.shape[1]
    line_number = matrix.shape[0]
    cnt = array([2 ** i for i in range(coluns_number)]) #   vetor com potências para 2. 2^0 2^1 2^2 ...

    return array([(cnt * matrix[i, :]).sum() for i in range(line_number)])

def normalizacao(populacao, index_ini, index_end, n_max, n_min) -> float:
    colunas = populacao.shape[1]
    
    size_bin = index_end - index_ini
    maior_bin = 2 ** size_bin - 1.0

    const_nomalizacao = (n_max - n_min) / maior_bin

    carac_norm = n_min + const_nomalizacao * bin(populacao[:, index_ini:index_end+1])
    return carac_norm


