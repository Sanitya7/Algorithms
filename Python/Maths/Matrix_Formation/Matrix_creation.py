#function for defining a n X n matrix
def create_matrix(dim):
    for i in range(0,dim):
        for j in range(0,dim):
            if i == j :
                if j == (dim - 1):
                    print("1")
                else :
                    print("1", end=",")
            else :
                if j == (dim - 1) :
                    print("0")
                else :
                    print("0", end=",")

n = int(input("Enter the Dimension: "))
create_matrix(n)