import os
import sys
import datetime

class Logger:
    nome = ''
    version = ''

    def __init__(self, nome : str, version=''):
        
        self.nome = nome
        self.version = version

        try:
            os.rename('error.log', f'error-{datetime.date.today()}.log')
            os.rename('output.log', f'output-{datetime.date.today()}.log')
        except Exception as x:
            sys.stderr.write(f'\n\n {datetime.datetime.now()} ERRORE: {x}\n')

        try:
            sys.stderr = open('error.log', 'w')
            sys.stdout = open('output.log', 'w')
        except Exception as x:
            sys.stderr.write(f'\n\n {datetime.datetime.now()} ERRORE: {x}\n')

        print(f'===={datetime.datetime.now()} {self.nome} {self.version}====\nLog Output caricato')
        sys.stderr.write(f'===={datetime.datetime.now()} {self.nome} {self.version}====\nLog Errore caricato')
    
    def errore(x):
        sys.stderr.write(f'\n\n {datetime.datetime.now()} ERRORE: {x}\n')

    def info(x):
        print(f'\n {datetime.datetime.now()} EVENTO: {x}\n')
    
    def avviso(x):
        sys.stderr.write(f'\n\n {datetime.datetime.now()} AVVISO: {x}\n')