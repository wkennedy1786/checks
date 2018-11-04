from check50 import *

class Hello(Checks):
    
    @check()
    def exists(self):
        """test.c exists"""
        self.require("randguess.c")
        
    @check("exists")
    def compiles(self):
        """test.c compiles"""
        self.spawn("clang -o randguess randguess.c -lcs50 -lm").exit(0)
        
    @check("compiles")
    def test_name(self):
        """output of Hello, world!"""
        self.spawn("./test")("Hello, world!\n", "Hello, world!\n").exit(0)
