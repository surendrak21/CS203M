import matplotlib.pyplot as plt

def calculate_students(p):
    if p > 1 or p < 0:
        print("Probability entered is either less than 0 or greater than 1, this is not possible!")
        return None

    prob_unique = 1.0  # Probability of all unique birthdays
    days_in_year = 365
    k = 0  # initially Number of students
    probabilities = []

    # Calculate the number of students required
    while prob_unique >= 1 - p:
        k += 1
        prob_unique *= (days_in_year - k + 1) / days_in_year
        probabilities.append(1 - prob_unique)

    return k, probabilities

def plot_probability_vs_students(probabilities):
    plt.plot(range(1, len(probabilities) + 1), probabilities)
    plt.xlabel('Number of Students')
    plt.ylabel('Probability of at least two students sharing a birthday')
    plt.title('Probability vs Number of Students')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    p = float(input("Enter the required probability (e.g., 0.5 for 50%): "))
    k, probabilities = calculate_students(p)
    if k:
        print("Number of students required:", k)
        plot_probability_vs_students(probabilities)
