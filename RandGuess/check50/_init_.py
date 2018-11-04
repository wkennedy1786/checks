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
        """input of Dr Bill yields output of 4"""
        self.spawn("./randguess").stdin("Hi, Dr Bill! Guess a number between 1 and 100.\n").stdout("4\n", "4\n").exit(0)
