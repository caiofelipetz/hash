#Caio Felipe Trindade Zehnder


class teste:
    def __init__(self, empno,):
        self.empno = empno
        

    def __eq__(self, other):
        return self.empno == other.empno

    def __hash__(self):
        return hash((self.empno))


teste2 = teste('jorge')
print(hash(teste2))

