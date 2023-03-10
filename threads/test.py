from threading import Thread
from threading import Lock
from time import sleep

class process(Thread):
    def __init__(self, texto, tempo) -> None:
        self.texto = texto
        self.tempo = tempo
        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)

class Ingressos:
    def __init__(self, estoque) -> None:
        self.estoque = estoque
        self.lock = Lock()
    
    def comprar(self, quantidade):
        self.lock.acquire()
        if self.estoque < quantidade:
            print("nao temos ingressos suficientes")
            self.lock.release()
            return
        
        sleep(1)

        self.estoque -= quantidade
        print(f"Voce comprou {quantidade} ingressos, ainda temos {self.estoque}")
        self.lock.release()
        
        

# p1 =  process('Thread 1', 4)
# p1.start()

# for i in range(20):
#     sleep(1)
#     print(i)

ingressos = Ingressos(10)
for i in range(1, 20):
    t = Thread(target=ingressos.comprar, args=(i,))
    t.start()

print(ingressos.estoque)