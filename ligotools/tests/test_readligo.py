import numpy
from ligotools import readligo as rl
import json

def test_read_frame():
    assert len(rl.loaddata('data/'+json.load(open("data/BBH_events_v3.json","r"))['GW150914']['fn_H1'],'H1'[1])) == 3 

def test__loaddata():
    assert len(rl.loaddata('data/'+json.load(open("data/BBH_events_v3.json","r"))['GW150914']['fn_H1'],'H1')[2]) == 13

def test_dq2segst():
    assert type(rl.loaddata('data/'+json.load(open("data/BBH_events_v3.json","r"))['GW150914']['fn_H1'],'H1')[2]) == dict

def test_dq_channel_to_seglist():
    assert type(rl.loaddata('data/'+json.load(open("data/BBH_events_v3.json","r"))['GW150914']['fn_H1'],'H1')[2]) == dict

def test_whiten():
    assert len(rl.loaddata('data/'+json.load(open("data/BBH_events_v3.json","r"))['GW150914']['fn_H1'],'H1')[0]) == 131072

def test_write_wavfile():
    assert type(rl.loaddata('data/'+json.load(open("data/BBH_events_v3.json","r"))['GW150914']['fn_H1'],'H1')[0]) == numpy.ndarray

def test_reqshift():
    assert type(rl.loaddata('data/'+json.load(open("data/BBH_events_v3.json","r"))['GW150914']['fn_H1'],'H1')[0]) == numpy.ndarray

def test_plotting_results():
    assert len(rl.loaddata('data/'+json.load(open("data/BBH_events_v3.json","r"))['GW150914']['fn_H1'],'H1')[1]) == 131072
    