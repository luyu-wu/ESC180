import numpy as np
import matplotlib.pyplot as plt

def plot_sin(a):
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(a * x)
    #plt.plot(x, y)
    #plt.show()

if __name__ == "__main__":
    plot_sin(2)


print("PART 2")
def generate_data_noisy(a, num_points):
    x = np.linspace(0, 2 * np.pi, num_points)
    y = np.sin(a * x) + 0.1 * np.random.randn(num_points)
    return y

def generate_data(a, num_points):
    x = np.linspace(0, 2 * np.pi, num_points)
    y = np.sin(a * x)
    return y
    
def sum_squared_differences(y1, y2):
    s = 0
    for i in range(len(y1)):
        s += (y1[i] - y2[i]) ** 2
    return s
    
if __name__ == "__main__":
    secret_a = 2.5
    y = generate_data_noisy(secret_a,100)

    best_a = 0
    best_a_ssq = 1e+99
    for i in range(2000):
        a_test = np.random.rand()*5
        len_test = generate_data(a_test,100)
        if sum_squared_differences(y,len_test) < best_a_ssq:
            print("new best value",a_test)
            best_a = a_test
            best_a_ssq = sum_squared_differences(y,generate_data(a_test,100)) < best_a_ssq

    plt.plot(y)
    plt.plot(generate_data(best_a,100))
    plt.show()
    # Your code here: try different a’s and find the one that makes
    # sum_squared_differences(y, generate_data(a, len(y))) small.
    # Your code here: plot y together with the best fit sin(ax).


# Problem 3
