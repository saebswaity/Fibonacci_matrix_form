import numpy as np
import matplotlib.pyplot as plt

# Function to calculate the Fibonacci sequence using matrix exponentiation
def fibonacci_matrix(n):
    phi = (1 + np.sqrt(5)) / 2
    phi_inv = 1 / phi
    P = np.array([[phi, phi_inv], [1, 1]])
    D = np.array([[1j * phi, 0], [0, -1j * phi_inv]])

    # Diagonalization
    A_n = np.dot(np.dot(P, (1j*D)**n), np.linalg.inv(P))

    # Extracting the Fibonacci numbers
    F_n = A_n.dot(np.array([1, 0]))

    return F_n[0]

# Calculate the Fibonacci numbers for a range of n values
n_values = np.linspace(1, 5, num=100)


# Calculate complex Fibonacci numbers
fibonacci_complex = np.array([fibonacci_matrix(n) for n in n_values])

# Plot the points in the complex plane
#plt.scatter(np.real(fibonacci_complex), np.imag(fibonacci_complex), label='Fibonacci Points', color='blue')

# Connect the points with lines
#plt.plot(np.real(fibonacci_complex), np.imag(fibonacci_complex), linestyle=':', marker='o', color='blue')
X = np.real(fibonacci_complex)
Y = np.imag(fibonacci_complex)
fig, ax = plt.subplots()
ax.scatter(X,Y , label='Fibonacci Points', c=(X**2 + Y**2)**.5, cmap='rainbow', s=20, alpha=1,marker='*')
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_aspect(1)
plt.title('Complex Fibonacci Sequence as 2D Points in the Complex Plane')
ax.legend()
plt.show()
