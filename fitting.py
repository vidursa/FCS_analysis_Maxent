import numpy as np
from lmfit import minimize, Minimizer, Parameters, Parameter, report_fit
import pandas as pd
import matplotlib.pyplot as plt
import math

def modeld(params, corrt):
    return (1/params['N'])*((params['N2']*(np.sqrt(1/(1+((corrt/params['td']))**params['Alpha1']))))+((1-params['N2'])*(np.sqrt(1/(1+((corrt/params['td2']))**params['Alpha2'])))))
    #return (1/params['N'])*(1+(params['T']*math.exp(-corrt/params['tT'])/(1-params['T'])))*(params['N2']*(np.sqrt(1/(1+((corrt/params['td'])**params['Alpha1'])))))*((1-params['N2'])*(np.sqrt(1/(1+((corrt/params['td2'])**params['Alpha2'])))))


def residual(params, corrt, Gt):
    for i in enumerate(corrt):
        if i[0]<1:
            model = modeld(params, i[1])
        else:
            model = np.append(model,modeld(params, i[1]))
    resid = (Gt - model)
    #print(np.sum(Gt),np.sum(resid))
    return resid

def normalize(Gt, corrt):
    s = next(i[0] for i in enumerate(corrt) if i[1] > 40)
    p = len(corrt)-next(i[0] for i in enumerate(reversed(corrt)) if i[1] < 0.0025)
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
    if "10{^-3}" in data.columns.levels[1][1]:
        Gt = (Gt*0.001)
    G, corr = normalize(Gt, corrt)
    return Gt, corrt, G, corr, fileiter, error

def generate_parameters(Gt):
    params = Parameters()
    params.add('N', value=1/np.mean(Gt[:20]), min=1/np.max(Gt[:20]), max=1/np.min(Gt[:20]))
    #print(1/np.mean(Gt[:30]),1/np.min(Gt[:30]),1/np.max(Gt[:30]))
    params.add('Alpha1', value=1, min=0, max=2 ,vary=False)
    params.add('Alpha2', value=1, min=0, max=2 ,vary=False)
    params.add('Offset', value=0)
    params.add('td', value=0.1, min=0.001, max=0.6)
    params.add('N2', value=0.4, min=0, max=1)# ,vary=False)
    params.add('td2', value=1, min=0.3, max=20)
    params.add('T', value=0.1, min=0, max=1)
    params.add('tT', value=0.001, min=0.0001, max=0.01)
    return params
