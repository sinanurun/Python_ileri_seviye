class futbolcu():
    kazanc = 550
    kosu = "hızlı koşabilir"
    def __init__(self):
        self.depar = "depar atar"

class basketbolcu():
    kazanc = 750
    ziplama = "yükseğe zıplayabilir"
    def __init__(self,boy = 190):
        self.boy = boy
        self.turnike = "turnike atabilir"
class multisporcu(futbolcu,basketbolcu):
    def __init__(self):
        futbolcu.__init__(self)
        # basketbolcu.__init__(self)
        basketbolcu.__init__(self,185)
mahmut = multisporcu()
print(mahmut.boy)
print(mahmut.depar)
print(mahmut.turnike)
print(mahmut.kazanc)
print(mahmut.kosu)
print(mahmut.ziplama)