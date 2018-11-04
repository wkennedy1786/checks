from check50 import *

class RandGuess(Checks):
    
    @check()
    def exists(self):
        """randguess.c exists"""
        self.require("randguess.c")
        
    @check("exists")
    def compiles(self):
        """randguess.c compiles"""
        self.spawn("clang -o randguess randguess.c -lcs50 -lm").exit(0)
        
    @check("compiles")
    def test_name(self):
        """input of Dr Bill yields output of Hi, Dr Bill!"""
        self.spawn("./randguess").stdin("Dr Bill").stdout("Hi, Dr Bill!\n", "Hi, Dr Bill!\n").exit(0)
