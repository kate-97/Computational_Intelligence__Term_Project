import numpy as np
import math
import copy

class DecisionTree:
    @staticmethod
    def make_path(i):
        path = [i]
        
        while i > 0:
            i = (i-1)//2
            path.append(i)
        
        path = path[::-1]
        return path

    def test_in_node(self, i):
        s_intances = copy.deepcopy(self.dataset)
        path = DecisionTree.make_path(i)
        tests = list(range(self.dataset.shape[1] - 1))

        for j in range(len(path) - 1):
            value = path[j+1] % 2
            test = tests[ self.content[ path[j] ] ]
            s_intances = [s for s in s_intances if s[test] == value]
            tests.remove(test)
        
        return s_intances



    def __init__(self, dataset, content = None):
        self.dataset = dataset

        if content is not None:
            self.content = content
            self.depth = math.floor(math.log2(len(content)))
            
        
        else:
            (instances, n) = dataset.shape
            n -= 1
            self.depth = 0
            self.content = []
            i = 0
            recognized = 0

            while(True):
                self.depth = math.floor(math.log2(i + 1))
                if i > 0:
                    if isinstance(self.content[(i-1) // 2], str):
                        self.content.append("*")
                        i += 1
                        continue

                    s_instances = self.test_in_node(i)

                    if len(s_instances) == 1:
                        self.content.append(str(s_instances[0][n]))
                        i += 1
                        recognized += 1
                        # print(self.content)

                        if recognized == instances:
                            break

                        else:
                            continue
                    
                n_avaiable = n - self.depth
                # print(n_avaiable)
                new_test = np.random.randint(n_avaiable)
                self.content.append(new_test)
                # print(self.content)
                i += 1