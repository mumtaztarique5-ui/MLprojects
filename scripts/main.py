from utils import greet_user

def main():
    name = input("Enter your name: ")
    greet_user(name)

if __name__ == "__main__":
    main()

from load_data import load_csv
from clean_data import clean_dataframe
from analyze_data import get_basic_stats, correlation_matrix
from visualize_data import plot_distributions, plot_heatmap, plot_missing

def main():
    file_path = "             "

    # Step 1: Load
    df = load_csv(file_path)

    # Step 2: Clean
    df = clean_dataframe(df)

    # Step 3: Analyze
    get_basic_stats(df)
    correlation_matrix(df)

    # Step 4: Visualize
    plot_missing(df)
    plot_distributions(df)
    plot_heatmap(df)

if __name__ == "__main__":
    main()
