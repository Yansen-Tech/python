class   A:
    def show (self):
        print("Ini adalah show info A")

class B(A):
    pass

class C(A):
    def show(self):
        print("Si C")

class D(B,C):
    pass


gundaka= D()
gundaka.show()        

        

        