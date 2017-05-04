import numpy as np
from scipy.spatial import distance
import random
from matplotlib.pyplot import *


# i = 0
# perfectDay = np.zeros((96,18))
# realDay = perfectDay
# while i<10:
#     p = random.choice(Mindex)
#     q = random.choice(Mindex)
#     realDay[p][q] = 1
#     i = i+1
#
#
# #Mwindow = np.zeros((18,4))
# MwindowSlices = {}
#
# i = 0

#
# def monitoringFn(day,max):
#     i=0
#     j=i+4
#     while j<max:
#         Mwindow = day[i:j,:]
#         MwindowSlices["Window{0}".format(i)] = Mwindow
#         #axs[i].spy(Mwindow, markersize=5)
#         #print Mwindow
#         i=i+1
#         j=i+4
#     return MwindowSlices
#
# #plt.show()
# #Mwindow = realDay[1:5,:]
# #monitoringFn()
# #print (Mwindow)
# #print(MwindowSlices["Window4"])
#
#
# def rapidlyBadDay(perfectDay):
#     badDay = perfectDay
#     badDay[0][0] = 1 # password breach
#     #x = monitoringFn(badDay,5)
#     badDay[1:6,1] = 1 # config file changed
#     badDay[2:7][2] = 1 # config file changed
#     badDay[3:8][2] = 1
#     badDay[4:9][2] = 1
#     badDay[5:9][2] = 1
#     badDay[6:9][2] = 1
#     badDay[7:9][2] = 1
#     badDay[8:9][2] = 1
#
#
#     return badDay
#
#
# h = rapidlyBadDay(perfectDay)
# print(h)
#
# fig = figure(figsize=(20,10))
# ax1 = fig.add_subplot(111)
# #ax2 = fig.add_subplot(222)
#
# ax1.spy(h, markersize=5)
# show()



M = np.zeros((4,18))
M2 = np.zeros((4,18))
M3 = np.zeros((4,18))
M4 = np.zeros((4,18))
MB = np.zeros((4,18))
MB2 = np.zeros((4,18))
MB3 = np.zeros((4,18))
MB4 = np.zeros((4,18))

#Mbackup = M

i = 0
star = 6
Mindex = np.arange(4)
MMindex = np.arange(star)

while i<3:
    p = random.choice(Mindex)
    q = random.choice(MMindex)
    M[p][q] = 1
    MB[p][q] = 1
    i = i+1

i = 0
star = 9
Mindex = np.arange(4)
MMindex = np.arange(star)

while i<10:
    p = random.choice(Mindex)
    q = random.choice(MMindex)
    M2[p][q] = 1
    MB2[p][q] = 1
    i = i+1

i = 0
star = 12
Mindex = np.arange(4)
MMindex = np.arange(star)

while i<20:
    p = random.choice(Mindex)
    q = random.choice(MMindex)
    M3[p][q] = 1
    p = random.choice(Mindex)
    q = random.choice(MMindex)
    MB3[p][q] = 1
    i = i+1

i = 0
star = 18
Mindex = np.arange(4)
MMindex = np.arange(star)

while i<36:
    p = random.choice(Mindex)
    q = random.choice(MMindex)
    M4[p][q] = 1
    p = random.choice(Mindex)
    q = random.choice(MMindex)
    MB4[p][q] = 1
    i = i+1



#print(M)

fig = figure(facecolor="white")
fig.set_figheight(15)
fig.set_figwidth(15)
# ax1 = fig.add_subplot(511)
# ax2 = fig.add_subplot(512)
# ax3 = fig.add_subplot(513)
# ax4 = fig.add_subplot(514)
# ax5 = fig.add_subplot(515)
ax1 = fig.add_subplot(521)
ax2 = fig.add_subplot(523)
ax3 = fig.add_subplot(525)
ax4 = fig.add_subplot(527)
ax5 = fig.add_subplot(529)
ax6 = fig.add_subplot(522)
ax7 = fig.add_subplot(524)
ax8 = fig.add_subplot(526)
ax9 = fig.add_subplot(528)
ax10 = fig.add_subplot(5,2,10)



ax1.spy(np.zeros((4,18)), markersize=5)
ax2.spy(M, markersize=5)
ax3.spy(M2, markersize=5)
ax4.spy(M3, markersize=5)
ax5.spy(M4, markersize=5)
ax6.spy(np.zeros((4,18)), markersize=5)
ax7.spy(MB, markersize=5)
ax8.spy(MB2, markersize=5)
ax9.spy(MB3, markersize=5)
ax10.spy(MB4, markersize=5)

fig.suptitle('Coordinated Cyber Attack Simulation', fontsize=20)
ax1.set_ylabel('Window 1')
ax2.set_ylabel('Window 2')
ax3.set_ylabel('Window 3')
ax4.set_ylabel('Window 4')
ax5.set_ylabel('Window 5')
ax5.set_xlabel('Monitored Bits of Bus 9')
ax10.set_xlabel('Monitored Bits of Bus 10')

#DISTANCE BETWEEN CORRESPONDING WINDOWS
dist1 = np.linalg.norm(MB-M)
dist2 = np.linalg.norm(MB2-M2)
dist3 = np.linalg.norm(MB3-M3)
dist4 = np.linalg.norm(MB4-M4)
show()

fig2 = figure(facecolor="white")
fig.suptitle('Coordinated Cyber Attack Heat Map Progress', fontsize=20)
axe = fig2.add_subplot(221)
axe2 = fig2.add_subplot(222)
axe3 = fig2.add_subplot(223)
axe4 = fig2.add_subplot(224)

data1= np.dot(MB.transpose(),M)
data2= np.dot(MB2.transpose(),M2)
data3= np.dot(MB3.transpose(),M3)
data4= np.dot(MB4.transpose(),M4)

heatmap = axe.pcolor(data1,  cmap=cm.Blues, alpha = 0.8)
heatmap2 = axe2.pcolor(data2, cmap=cm.Blues, alpha = 0.8)
heatmap3 = axe3.pcolor(data3, cmap=cm.Blues, alpha = 0.8)
heatmap4 = axe4.pcolor(data4, cmap=cm.Blues, alpha = 0.8)

axe.set_yticks(np.arange(data1.shape[0])+0.5, minor=False)
axe.set_xticks(np.arange(data1.shape[1])+0.5, minor=False)
axe.set_xlabel('Window2')
axe2.set_yticks(np.arange(data2.shape[0])+0.5, minor=False)
axe2.set_xticks(np.arange(data2.shape[1])+0.5, minor=False)
axe2.set_xlabel('Window3')
axe3.set_yticks(np.arange(data3.shape[0])+0.5, minor=False)
axe3.set_xticks(np.arange(data3.shape[1])+0.5, minor=False)
axe3.set_xlabel('Window4')
axe4.set_yticks(np.arange(data4.shape[0])+0.5, minor=False)
axe4.set_xticks(np.arange(data4.shape[1])+0.5, minor=False)
axe4.set_xlabel('Window5')

column_labels = list('ABCDEFGHIJKLMNOPQR')
row_labels = list('ABCDEFGHIJKLMNOPQR')

axe.set_xticklabels(row_labels, minor=False)
axe.set_yticklabels(column_labels, minor=False)
axe2.set_xticklabels(row_labels, minor=False)
axe2.set_yticklabels(column_labels, minor=False)
axe3.set_xticklabels(row_labels, minor=False)
axe3.set_yticklabels(column_labels, minor=False)
axe4.set_xticklabels(row_labels, minor=False)
axe4.set_yticklabels(column_labels, minor=False)




def simulateAttack():
    pass


print(dist1,dist2,dist3,dist4)
show()

from sklearn.cluster.bicluster import SpectralBiclustering
from sklearn.metrics import consensus_score
from matplotlib import pyplot as plt

from sklearn.datasets import make_checkerboard
from sklearn.datasets import samples_generator as sg

n_clusters = (2, 2)
data, rows, columns = make_checkerboard(
    shape=(18, 18), n_clusters=n_clusters, noise=10,
    shuffle=False, random_state=0)

plt.matshow(data, cmap=plt.cm.Blues)
plt.title("Original dataset")

data, row_idx, col_idx = sg._shuffle(data4, random_state=0)
plt.matshow(data4, cmap=plt.cm.Blues)
plt.title("Shuffled dataset")

model = SpectralBiclustering(n_clusters=n_clusters, method='log',
                             random_state=0)
model.fit(data4)
score = consensus_score(model.biclusters_,(rows[:, row_idx], columns[:, col_idx]))

print("consensus score: {:.1f}".format(score))

fit_data = data4[np.argsort(model.row_labels_)]
fit_data = fit_data[:, np.argsort(model.column_labels_)]

#plt.matshow(fit_data, cmap=plt.cm.Blues)
#plt.title("After biclustering; rearranged to show biclusters")

plt.matshow(np.outer(np.sort(model.row_labels_) + 1,
                     np.sort(model.column_labels_) + 1),
            cmap=plt.cm.Blues)
plt.title("Co-clustering of Coordinated Attack Matrix")

plt.show()
