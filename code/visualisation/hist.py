import matplotlib.pyplot as plt
import csv

def get_greedy_dist():
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


# def get_random_dist():

#     with open("data/output/output.csv", 'r') as infile:
#             reader = csv.reader(infile)
#             header = next(infile)

#             x = []
#             for line in reader:
#                 x.append(float(line[1]))
            

#     plt.hist(x=x, bins=100)
#     plt.title('Histogram: Verdeling Random algoritme')
#     plt.xlabel('Quality')
#     plt.ylabel('Aantal')
#     plt.savefig("data/quality/hist_random.png")

# def get_all_dist():

#     with open("data/quality/output.csv", 'r') as infile:
#             reader = csv.reader(infile)
#             header = next(infile)

#             r = []
#             for line in reader:
#                 r.append(float(line[1]))

#     with open("data/quality/output.csv", 'r') as infile:
#             reader = csv.reader(infile)
#             header = next(infile)

#             g = []
#             for line in reader:
#                 g.append(float(line[1]))


    
    # plt.hist(x=r, bins=15, alpha = 0.5, label = 'Random')
    # plt.hist([r, g], bins=100, label=['Random', 'Greedy'])

    # plt.title('Histogram: Verdeling Greedy en Random')
    # plt.xlabel('Quality')
    # plt.ylabel('Aantal')
    # plt.legend(loc='upper right')
    # plt.savefig("data/quality/hist_GenR.png")
