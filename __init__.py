def dummy_one(df, thresh = 20, drop = False):
    if thresh != 20:
        for d in df.columns:
            if df[d].dtype == object:
                if int(len(df[d].unique()) <= int(thresh)):
                    df[d] = df[d].replace(df[d].unique(),range(len(df[d].unique())))
                else:
                    if drop == True:
                        df = df.drop(d, axis=1)
                    else:
                        pass
    else:
        for d in df.columns:
            if df[d].dtype == object:
                if int(len(df[d].unique()) <= 20):
                    df[d] = df[d].replace(df[d].unique(),range(len(df[d].unique())))
                else:
                    if drop == True:
                        df = df.drop(d, axis=1)
                    else:
                        pass
    return df

