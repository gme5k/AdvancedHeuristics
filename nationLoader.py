def nationLoader(nation):
    '''
    Loads province adjacency text file and turn it into dictionary
    containing provincenames as key with list of their neighbors and
    transmitter number as dictionary value.
    Default transmitter is 0
    '''
    # Initialize dictionary
    provinces = {}
    
    # Load nation data txt file as text.
    with open(nation) as data:        
        for line in data:
           
            # Split rows by comma
            content = line.replace("\n", "").split(',')
            
            # Set first placename of row as key in dictionary. Set remaining names in list of neighbors.
            provinces[content[0]] = [content[1:], 0]

    return provinces