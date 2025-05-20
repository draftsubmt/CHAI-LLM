import pickle

filename = 'HinGE.pkl'

with open(filename, 'rb') as f:
  df = pickle.load(f)

df.head()