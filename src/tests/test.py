import numpy as np
from decision_tree import *

# test

def test_case(df):
    dtree = DecisionTree(dataset = df)
    print(dtree.depth)

def make_test_instances(instances_lb, instances_ub, n_lb , n_ub):
    instances = np.random.randint(instances_lb, instances_ub)
    n = np.random.randint(n_lb, n_ub)
    binaries = [0,1]
    dataset = [list(np.random.choice(binaries, n))]
    k = 0

    for i in range(instances-1):
        instance = list(np.random.choice(binaries, n))
        j = 0
        ind = True
        while instance in dataset:
            ind = False
            j+= 1
            if j > 100000:
                break
            change_index = int(np.random.randint(n))
            if instance[change_index] == 1:
                instance[change_index] = 0
                ind = True
            else:
                instance[change_index] = 1
                ind = True
        
        if ind:
            dataset.append(instance)
        else:
            k += 1
    
    dataset = np.array(dataset)
    objects = np.array([[i] for i in range(instances-k)])
    print("n: " ,n)
    print("instances: " , instances-k)
    dataset = np.array(np.append(dataset, objects, axis = 1))
    return dataset


def run_tests(n, instances_lb, instances_ub, n_lb , n_ub):
    for i in range(n):
        test_case(make_test_instances(instances_lb, instances_ub, n_lb , n_ub))
# make_test_instances(50,100,20,40)