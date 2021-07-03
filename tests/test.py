import pickle
import pytest
import hashlib
import pandas as pd
import numpy as np

def hashit(f):
    f=str(f).encode()
    m=hashlib.md5()
    m.update(bytes(f))
    return m.hexdigest()
    

def unpick(fname):
    with open(fname,'rb') as f:
        db=pickle.load(f)
    return db
        

def test1():
    db=unpick('f2.pickle')
    assert hashit(db[0])=='bb3a8b2e390142074e49741a0121d623'
    
def test2():
    db=unpick('f3.pickle')
    assert hashit(db[2017][3])=='15649cdc816c5f50475138ea0a48086b'
    
def test3():
    db=unpick('f4.pickle')
    assert hashit(db['East'])=='1cd138d0499a68f4bb72bee04bbec2d7'
    
def test4():
    db=unpick('f5.pickle')
    assert hashit(db[1])=='7effe80425095de4d5b996a01e4f00a3'

    
def test5():
    db=unpick('f8.pickle')
    assert hashit(db[2018]['East'])=='955372bb109dbaa6c45020c0c59ad018'
