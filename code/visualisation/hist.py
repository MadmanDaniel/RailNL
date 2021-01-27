import matplotlib.pyplot as plt
import csv

def get_dist():
    """
    Making a Histogram
    out of the outcome CSV file
    """
    with open("data/output/output.csv", 'r') as infile:
            reader = csv.reader(infile)
            header = next(infile)

            x = []
            for line in reader:
                x.append(float(line[1]))

    plt.hist(x=x, bins=50)
    plt.title('Histogram: Verdeling Gebruikte algoritme')
    plt.xlabel('Quality')
    plt.ylabel('Aantal')
    plt.savefig("data/output/histogram.png")
