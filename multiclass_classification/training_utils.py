import sys; sys.path.append("/afs/cern.ch/work/p/prsaha/public/XGBoost_train_v2/Higgs_NISER/Training/python")
import matplotlib.pyplot as plt
import os
import math
from math import sqrt
import numpy as np

import random as rnd

from sklearn.utils.extmath import cartesian
import scipy.stats as stats

import random


def deltaR_pandas(e1,p1,e2,p2):
    deta = e1 - e2
    dphi = abs(p1-p2)   
    dp = np.array(dphi.values.tolist())
    dphi = np.where(dp > 3.14, dp-2*3.14, dp)
    return np.sqrt(np.power(deta, 2) + np.power(dphi, 2))

def dr_by_2_indices(x,index1,index2):
    return x[index1],x[index2]

def dr_second_pair_index(min_index):
    if min_index==0 : return 3
    if min_index==3 : return 0
    if min_index==1 : return 2
    if min_index==2 : return 1

def dr_min_index(series):
    ar = np.array([np.array(v) for v in series.values])
    min_index = np.argmin(ar,axis=1)    
    return min_index.tolist()
           
    
# ---------------------------------------------------------------------------------------------------
class IO:
    ldata = os.path.expanduser("/eos/user/p/prsaha/Tprime_analysis/MVA_inputs/RunII")
    xdata = "/eos/user/p/prsaha/www/xgboost_outout"
    plotFolder = os.path.expanduser("/eos/user/p/prsaha/www/xgboost_outout/plots/")
    signalName = []
    signalMixOfNodes = False
    ggHHWhichMixOfNodes = []
    ggHHMixOfNodesNormalizations = dict()
    signalTreeName = []
    backgroundName = []
    bkgTreeName = []
    dataName = []
    dataTreeName = []
    sigProc = []
    bkgProc = []
    dataProc = []
    sigYear = []  ### year : 0-2016,1-2017,2-2018. Categorical var
    bkgYear = []
    dataYear = []
    nSig=0
    nBkg=0
    nData=0
    signal_df = []
    background_df = []
    data_df= []
    
    cross_sections = {}

    @staticmethod
    def use_signal_nodes(useNodes,whichNodes,normalizations):
        if useNodes :
            IO.signalMixOfNodes = True
            IO.ggHHWhichMixOfNodes = whichNodes
            IO.ggHHMixOfNodesNormalizations = normalizations

            
   
    @staticmethod
    def add_signal(ntuples,sig, proc, treeName,year=0):
        IO.signalName.append(IO.ldata+ntuples+"/"+''.join(sig))
        IO.sigProc.append(proc)
        IO.nSig+=1
        IO.signalTreeName.append(treeName)
        IO.sigYear.append(year)

        
    @staticmethod
    def add_background(ntuples,bkg,proc,treeName,year=0):
        IO.backgroundName.append(IO.ldata+ntuples+"/"+''.join(bkg))
        IO.bkgProc.append(proc)
        IO.nBkg+=1
        IO.bkgTreeName.append(treeName)
        IO.bkgYear.append(year)


    
    @staticmethod
    def add_data(ntuples,data,proc,treeName,year=0):
        IO.dataName.append(IO.ldata+ntuples+"/"+''.join(data))
        IO.dataProc.append(proc)
        IO.nData+=1
        IO.dataTreeName.append(treeName)
        IO.dataYear.append(year)





    


