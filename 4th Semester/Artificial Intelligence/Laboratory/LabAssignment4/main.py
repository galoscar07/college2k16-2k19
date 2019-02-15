import random
import math
import operator

CLASSES = ['normal', 'suspect', 'pathological']
SPLIT = 0.99


def read_data(path, training, test):
    # 0 - b
    # 1 - e
    # 2 - LBE
    # 3 - LB
    # 4 - AC
    # 5 - FM
    # 6 - UC
    # 7 - ASTV
    # 8 - MSTV
    # 9 - ALTV
    # 10 - MLTV
    # 11 - DL
    # 12 - DS
    # 13 - DP
    # 14 - Width
    # 15 - Min
    # 16 - Max
    # 17 - Nmax
    # 18 - Nzeros
    # 19 - Mode
    # 20 - Mean
    # 21 - Median
    # 22 - Variance
    # 23 - NSP - RESULT

    li = []

    with open(path) as file:
        lines = [line.split(",") for line in file]
        for line in lines:
            li.append(line)

    for i in range(len(li)):
        li[i] = [float(j) for j in li[i]]

    for i in li:
        i[-1] = CLASSES[int(i[-1]) - 1]

    for i in li:
        if random.random() < SPLIT:
            training.append(i)
        else:
            test.append(i)


def euclidean_distance(instance1, instance2, length):
    distance = 0
    for i in range(length):
        distance += pow((instance1[i] - instance2[i]), 2)
    return math.sqrt(distance)


def get_neighbors(training, test_instance, _k):
    distances = []
    length = len(test_instance) - 1
    for i in range(len(training)):
        dist = euclidean_distance(test_instance, training[i], length)
        distances.append((training[i], dist))
    distances.sort(key=operator.itemgetter(1))
    neigh = []
    for i in range(_k):
        neigh.append(distances[i][0])
    return neigh


def get_response(neigh):
    class_votes = {}
    for i in range(len(neigh)):
        response = neigh[i][-1]
        if response in class_votes:
            class_votes[response] += 1
        else:
            class_votes[response] = 1
    sorted_votes = sorted(class_votes.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_votes[0][0]


def get_accuracy(test, pred):
    correct = 0
    for i in range(len(test)):
        if test[i][-1] == pred[i]:
            correct += 1
    return (correct / float(len(test))) * 100.0


if __name__ == '__main__':
    # prepare data
    training_set = []
    test_set = []
    read_data('data.txt', training_set, test_set)
    print('Train set: ' + repr(len(training_set)))
    print('Test set: ' + repr(len(test_set)))

    # generate predictions
    predictions = []
    k = 3
    for x in range(len(test_set)):
        neighbors = get_neighbors(training_set, test_set[x], k)
        result = get_response(neighbors)
        predictions.append(result)
        print('Predicted = ' + repr(result) + ' Actual = ' + repr(test_set[x][-1]))
    accuracy = get_accuracy(test_set, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')
