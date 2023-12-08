import numpy as np
import matplotlib.pyplot as plt

def fibonacci_matrix(n):
    # Constants
    phi = (1 + np.sqrt(5)) / 2
    phi_inv = 1 / phi
    P = np.array([[phi, phi_inv], [1, 1]])
    D = np.array([[1j * phi, 0], [0, -1j * phi_inv]])

    # Matrix exponentiation for Fibonacci sequence
    A_n = np.dot(np.dot(P, (1j * D) ** n), np.linalg.inv(P))

    # Extract the Fibonacci numbers
    F_n = A_n.dot(np.array([1, 0]))

    return F_n[0]

def calculate_fibonacci_sequence(n_values):
    # Calculate complex Fibonacci numbers for a range of n values
    fibonacci_complex = np.array([fibonacci_matrix(n) for n in n_values])
    return np.real(fibonacci_complex), np.imag(fibonacci_complex)

def plot_complex_sequence(X, Y):
    # Plot the points in the complex plane
    fig, ax = plt.subplots()
    scatter = ax.scatter(X, Y, label='Fibonacci Points', c=(X**2 + Y**2)**.5, cmap='rainbow', s=20, alpha=1, marker='*')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_aspect(1)
    plt.title('Complex Fibonacci Sequence as 2D Points in the Complex Plane')
    ax.legend()
    plt.show()

def main():
    # Input values
    n_values = np.linspace(1, 5, num=100)

    # Calculate Fibonacci sequence
    X, Y = calculate_fibonacci_sequence(n_values)

    # Plot the complex Fibonacci sequence
    plot_complex_sequence(X, Y)

if __name__ == "__main__":
    main()
