import numpy as np
from lmfit import minimize, Minimizer, Parameters, Parameter, report_fit
import pandas as pd
import matplotlib.pyplot as plt

def modeldd(a, b, corrt):
    return (a*(np.sqrt(1/(1+((corrt/b))))))


def modeld(params, corrt, ta):
    
    fn = 0
    param_set = []
    
    for i in enumerate(ta):
        #if i[0]>0:
        fn += modeldd(params['a'+str(i[0])], i[1], corrt)

    #fn = (1/params['N'])*modeldd(params['a0'], ta[7], corrt)
    return fn+params['N1']

def var(Gt):
    array = pd.Series(Gt)
    #array.plot(style='k--')
    var = array.rolling(window = 9, center = True).std()
    #array.rolling(window = 9, center = True).std().plot(style='b')
    return var

def residual(params, corrt, Gt, ta):

    for i in enumerate(corrt):
        if i[0] < 1:
            model = modeld(params, i[1], ta)
        else:
            model = np.append(model, modeld(params, i[1], ta))
    resid = (Gt - model)[4:-4]/var(Gt)[4:-4]

    #print(Gt,model,resid)
    '''f= open("E:\guru99.txt","a+")

    f.write("\r\n G \r\n")
    for i in range(np.size(Gt)):
        f.write("%d," %Gt[i]*1000)
        print(Gt[i])

    f.write("\r\n modelGt \r\n")
    for i in range(np.size(model)):
        f.write("%d," %model[i]*1000)

    f.write("\r\n resid \r\n")
    for i in range(np.size(resid)):
        f.write("%d," %resid[i]*1000)

    f.write("\r\n ta \r\n")
    for i in range(np.size(ta)):
        f.write("%d," %params['a'+str(i)].value*1000)
        

    f.close()'''
    
    chi2 = (resid*resid)/np.size(resid)
    '''chi2 = np.append(chi2,2)'''

    
    for i in range(0, np.size(ta)):
        if i < 1:
            param_set = params['a'+str(i)]
        else:
            param_set = np.append(param_set, params['a'+str(i)])

    '''for i in range(0, np.size(ta)):
        if(i>0):
            a_combined += '+a' + str(i)
        else:
            a_combined = 'a' + str(i)
    
    #params['N'].set(expr='%s'%a_combined)'''
    #print(np.sum(chi2),entropy(params, ta),np.sum(param_set)-np.mean(Gt[:20]))
    
    
    #print(np.sum(chi2),entropy(params, ta))
    #return np.append(chi2,np.append(entropy(params, ta),np.sum(param_set)-np.mean(Gt[:20])))
    return np.append(chi2,np.sum(param_set)-np.mean(Gt[:20]))

def entropy(params, ta):
    param_set = []
    for i in range(0, np.size(ta)):
        if i < 1:
            param_set = params['a'+str(i)]
        else:
            param_set = np.append(param_set, params['a'+str(i)])
    p = param_set/np.sum(param_set)
    S = np.sum(p*np.log(p))
    return S

def normalize(Gt, corrt):
    s = next(i[0] for i in enumerate(corrt) if i[1] > 100)
    p = len(corrt)-next(i[0] for i in enumerate(reversed(corrt)) if i[1] < 0.001)
    return Gt[p:s], corrt[p:s]

def clean_data(data, fileiter):
    datas = data.values
    error = 0
    try:
        corrt, Gt = datas.T
    except ValueError:
        print(wbname[-1]+" has more than 1 channel")
        fileiter += 1
        error = 1
    corrt = pd.to_numeric(corrt, errors='coerce')
    Gt = pd.to_numeric(Gt, errors='coerce')
    if np.max(Gt) > 1:
        Gt = (Gt*0.001)
    G, corr = normalize(Gt, corrt)
    return Gt, corrt, G, corr, fileiter, error

def generate_parameters(ta, Gt):
    a_combined = 0
    params = Parameters()
    for i in range(0, np.size(ta)):
        params.add('a'+str(i), value=np.mean(Gt[:20])/(np.size(ta)), min=0)
    for i in range(1, np.size(ta)):
        if(i>1):
            a_combined += '+a' + str(i)
        else:
            a_combined = 'a' + str(i)
    params.add('N', value=np.mean(Gt[:20]), expr='%s'%a_combined)
    #params.add('N', value=np.mean(Gt[:20]), min=np.max(Gt[:30]), max=np.min(Gt[:30]), expr='%s'%a_combined)
    params.add('N1', value=0)
    return params
