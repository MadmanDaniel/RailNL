import matplotlib.pyplot as plt
import csv

def get_greedy_dist():

    with open("data/quality/greedy_output.csv", 'r') as infile:
            reader = csv.reader(infile)
            header = next(infile)

            x = []
            for line in reader:
                x.append(float(line[1]))

    plt.hist(x=x, bins=10)
    plt.title('Histogram: Verdeling Greedy algoritme')
    plt.xlabel('q')
    plt.ylabel('Aantal')
    plt.savefig("data/quality/hist_greedy.png")


def get_random_dist():

    with open("data/quality/random_output.csv", 'r') as infile:
            reader = csv.reader(infile)
            header = next(infile)

            x = []
            for line in reader:
                x.append(float(line[1]))
            

    plt.hist(x=x, bins=10)
    plt.title('Histogram: Verdeling Random algoritme')
    plt.xlabel('q')
    plt.ylabel('Aantal')
    plt.savefig("data/quality/hist_random.png")