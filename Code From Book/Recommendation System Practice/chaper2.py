def SplitData(data, M, k, seed):
    '''将用户行为数据data按照均匀分布随机分成M份，
       挑选其中的第k份作为测试集，seed为随机数的种子值'''
    test = []
    train = []
    random.seed(seed)
    for user, item in data:
        if random.randint(0,M) == k:
            test.append([user,item])
        else:
            train.append([user,item])
    return train, test
