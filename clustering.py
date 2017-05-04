from scipy.io import loadmat
from coclust.coclustering import CoclustMod

file_name = "/home/sayon/Dropbox/MyModules/Canvass/cclust_package/datasets/som.mat"
matlab_dict = loadmat(file_name)
X = matlab_dict['fea']

model = CoclustMod(n_clusters=4)
model.fit(X)

print(model.modularity)
predicted_row_labels = model.row_labels_
predicted_column_labels = model.column_labels_
