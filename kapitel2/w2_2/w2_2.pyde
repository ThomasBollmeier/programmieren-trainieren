# Weihnachtsbaum

def line(size, i, ch):
    padding = size - 1 - i
    return " " * padding + ch * (2*i+1) + " " * padding

def print_tree(size, ch):
    for i in range(size):
        print(line(size, i, ch))
    print(line(size, 1, ch))
    
print_tree(7, "*")
        
        
