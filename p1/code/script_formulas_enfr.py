import sys
import math


t0 = eval(sys.argv[1])
alpha = eval(sys.argv[2])

with open("../data/funciones_enfriamiento.txt", "w") as f:
    for it in range(1, 500, 5):
        t1 = t0 * (500 - it)/500
        t2 = alpha*t0 / math.log(1 + it)
        t3 = (alpha**it) * t0

        f.write(str(it) + "\t" + str(t1) + "\t" +
                str(t2) + "\t" + str(t3) + "\n")
