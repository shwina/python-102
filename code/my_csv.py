import pandas

def read_csv(fname):
    with open(fname) as f:
        col_names = f.readline().rstrip().split(',')
        df = pandas.DataFrame(columns=col_names)
        for line in f:
            record = pandas.DataFrame([line.rstrip().split(',')], columns=col_names)
            df = df.append(record, ignore_index=True)
    return df
