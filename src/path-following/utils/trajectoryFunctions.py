import numpy as np

def computeEuclidianDistance(x0,y0,x1,y1):
    return ((x0-x1)**2 + (y0-y1)**2)**0.5
#end-def

def distance2line(Ax, Ay, Bx, By, Px, Py):
    #Line with two end points: A and B
    A = np.array([Ax, Ay])
    B = np.array([Bx, By])
    P = np.array([Px, Py])
    
    # Calculate the unit vector u
    u = (B - A) / np.linalg.norm(B - A)

    # Compute the normal vector n
    n = np.array([-u[1], u[0]])

    # Solve the linear system to find lambda1 and lambda2
    matrix = np.array([[u[0], -n[0]], [u[1], -n[1]]])
    solution = np.linalg.solve(matrix, P - A)

    lambda1 = solution[0]
    lambda2 = solution[1]
    
    #print("l1: ", lambda1)
    #print("l2: ", lambda2)
    
    Q = A + lambda1*u;
    Q = P + lambda2*n;
    
    Qx = Q[0];
    Qy = Q[1];
    
    distance = computeEuclidianDistance(Qx,Qy,Px,Py)
    
    #print(Qx)
    #print(Qy)
    #print(d)
    
    #Slope between the two lines
    try:
        m1 = (Ay-By) / (Ax-Bx);
        m2 = (Py-Qy) / (Px-Qx);
        theta = np.arctan((m1 - m2) / (1 + m1 * m2))
        #print(theta)
    except:
        theta = float('inf')
    #end-try-except
    
    
    return distance, lambda1, lambda2, theta, Q
#end-def
