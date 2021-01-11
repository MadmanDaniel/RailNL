from code.classes import station, load
import csv

if __name__ == "__main__":

    loading_in_files = load.Load("data/opdracht1/StationsHolland.csv")

    print(loading_in_files.get())