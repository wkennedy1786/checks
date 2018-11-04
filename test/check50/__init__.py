from check50 import *

class test(Checks):
    
    @check()
    def exists(self):
        """test.c exists"""
        self.require("test.c")
        
    @check("exists")
    def compiles(self):
        """test.c compiles"""
        self.spawn("clang -o test test.c -lcs50 -lm").exit(0)
        
    @check("compiles")
    def test_name(self):
        """Output of Hello World!"""
        self.spawn("./test").stdout("Hello, world!\n", "Hello, world!\n").exit(0)
