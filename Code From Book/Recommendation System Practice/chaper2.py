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
    
def Recall(train, test, N):
    '''召回率：给用户推荐N个物品，有多少比例的用户-物品评分记录包含在最终的推荐列表中'''
    hit = 0
    all = 0
    for user in train.keys():
        tu = test[user]
        rank = GetRecommendation(user, N)
        for item, pui in rank:
            if item in tu:
                hit += 1
        all += len(tu)
    return hit / (all + 1.0)
    
def Precision(train, test, N):
    '''准确率：给用户推荐N个物品，有多少比例的用户-物品评分记录是包含在发生过的用户-物品评分记录中'''
    hit = 0
    all = 0
    for user in train.keys():
        tu = test[user]
        rank = GetRecommendation(user, N)
        for item, pui in rank:
            if item in tu:
                hit += 1
        all += N
    return hit / (all + 1.0)
