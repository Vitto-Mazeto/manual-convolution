import numpy as np

def convolution_step_by_step(matrix, kernel, stride=1):
    """
    Aplica a operação de convolução de forma manual e printa cada passo do cálculo.
    """
    m, n = matrix.shape
    k_m, k_n = kernel.shape
    out_rows = (m - k_m) // stride + 1
    out_cols = (n - k_n) // stride + 1
    result = np.zeros((out_rows, out_cols), dtype=int)
    
    print("Iniciando a Convolução:")
    for i in range(out_rows):
        for j in range(out_cols):
            # Define os índices da região em que o kernel será aplicado
            row_start = i * stride
            row_end = row_start + k_m
            col_start = j * stride
            col_end = col_start + k_n
            region = matrix[row_start:row_end, col_start:col_end]
            
            # Multiplicação elemento a elemento
            product = region * kernel
            conv_value = np.sum(product)
            result[i, j] = conv_value
            
            print(f"\nJanela (posição [{i}, {j}] da saída):")
            print("Região extraída:")
            print(region)
            print("Multiplicação com o kernel:")
            print(product)
            print(f"Soma dos valores = {conv_value}")
    
    print("\nMatriz resultante da Convolução:")
    print(result)
    return result

def max_pooling_step_by_step(matrix, pool_size=2, stride=2):
    """
    Aplica a operação de max pooling e printa cada etapa, mostrando a janela e o valor máximo.
    """
    m, n = matrix.shape
    out_rows = (m - pool_size) // stride + 1
    out_cols = (n - pool_size) // stride + 1
    result = np.zeros((out_rows, out_cols), dtype=int)
    
    print("Iniciando o Max Pooling:")
    for i in range(out_rows):
        for j in range(out_cols):
            row_start = i * stride
            row_end = row_start + pool_size
            col_start = j * stride
            col_end = col_start + pool_size
            window = matrix[row_start:row_end, col_start:col_end]
            max_val = np.max(window)
            result[i, j] = max_val
            
            print(f"\nJanela (posição [{i}, {j}] da saída):")
            print("Região considerada:")
            print(window)
            print(f"Valor máximo nesta janela: {max_val}")
    
    print("\nMatriz resultante após o Max Pooling:")
    print(result)
    return result

def main():
    # Matriz original (imagem em tons de cinza)
    image = np.array([[1, 3, 2, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12],
                      [13, 14, 15, 16]])
    
    print("Matriz original (imagem):")
    print(image)
    print("\n----------------------------------------\n")
    
    # Parte (a): Convolução com kernel para destacar ervas daninhas
    # Kernel: [-1  0]
    #         [ 0  1]
    kernel_a = np.array([[-1, 0],
                         [ 0, 1]])
    print("Parte (a): Convolução com o kernel:")
    print(kernel_a)
    print("\n")
    
    conv_result = convolution_step_by_step(image, kernel_a, stride=1)
    
    print("\n----------------------------------------\n")
    
    # Parte (b): Explicação de como a convolução ajuda a detectar ervas daninhas
    print("Parte (b): Explicação sobre a operação de convolução:")
    print("""
A operação de convolução com o kernel [-1  0; 0  1] realiza a seguinte operação:
    - Multiplica o pixel do canto superior esquerdo por -1 e o do canto inferior direito por +1,
      ignorando os outros dois pixels.
    
Em regiões onde a imagem apresenta intensidade uniforme (como em uma plantação homogênea),
a diferença entre os pixels tende a ser pequena e o resultado da convolução é próximo de zero.
Porém, se houver uma mudança abrupta de intensidade – por exemplo, devido à presença de uma erva daninha
com características (formato ou tom) diferentes –, a diferença entre o pixel inferior direito e o superior esquerdo será maior.
Dessa forma, o filtro realça essas transições, ajudando a identificar áreas possivelmente contendo ervas daninhas.
    """)
    
    print("\n----------------------------------------\n")
    
    # Parte (c): Operação de Max Pooling
    print("Parte (c): Aplicando Max Pooling na matriz original com janela 2x2 e stride 2")
    pool_result = max_pooling_step_by_step(image, pool_size=2, stride=2)
    
    print("""
A operação de max pooling reduz a dimensão da imagem ao selecionar, em cada janela, o valor máximo,
preservando assim as características mais salientes (por exemplo, bordas ou picos de intensidade).
Isso diminui a complexidade da imagem, facilitando o processamento posterior sem perder informações importantes.
    """)
    
    print("\n----------------------------------------\n")
    
    # Parte (d): Convolução utilizando um kernel especializado em detecção de bordas
    # Novo kernel: [ 1  -1]
    #             [-1   1]
    kernel_d = np.array([[1, -1],
                         [-1, 1]])
    print("Parte (d): Convolução com o kernel especializado em bordas:")
    print(kernel_d)
    print("\n")
    
    conv_result_d = convolution_step_by_step(image, kernel_d, stride=1)
    
    print("""
Utilizando o kernel [1 -1; -1 1], os sinais das operações são invertidos em relação ao kernel anterior.
Esse filtro enfatiza as transições de intensidade de forma diferente, realçando ainda mais as bordas.
Assim, regiões com mudanças abruptas – possivelmente correspondentes aos contornos das ervas daninhas – podem ficar ainda mais destacadas.
    """)

if __name__ == "__main__":
    main()
