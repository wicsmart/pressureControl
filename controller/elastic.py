from time import gmtime, strftime
    

def envia_dado(psi, pneu, status):
    data_hora = strftime('%Y/%m/%d %H:%M:%S', gmtime())
    doc = {
        "psi" : psi,
        "pneu" : pneu,
        "status": status,
        "data_hora" : data_hora
    }

if __name__ == "__main__":
    pass


