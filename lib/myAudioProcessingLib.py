import wave # para reproduzir arquivos WAV
from music21 import midi # para reproduzir arquivos MIDI
import numpy as np
from IPython.display import Audio

def audioread(filename):
    '''
       Carrega os dados do som em um arquivo e retorna os dados no array 'soundx'
       com tipo de dado 'numpy.float', junto com a frequencia de amostragem 'fs'
       Cada canal de som será uma coluna do array.
    '''
    ifile = wave.open(filename)
    fs = ifile.getframerate()
    frames = ifile.getnframes()
    x = ifile.readframes(frames)
    x = np.fromstring(x, dtype='uint16')
    x = x.astype('int16')
    
    max_amplitude = np.iinfo('uint16').max # 2**NUM_BITS-1
    x = x.astype(float) / max_amplitude
    
    channels = ifile.getnchannels()
    if channels > 1:
        x = x.reshape((int(len(x) / channels), channels))

    return x, fs

def play(x, fs=None):
    '''
       Reproduz arquivos de Audio (WAV, OGG)
    '''
    display(Audio(data=x, rate=fs))

def playMIDI(filename):
    '''
       Reproduz um arquivo MIDI
    '''
    mf = midi.MidiFile()
    mf.open(filename)
    mf.read()
    mf.close()
    s = midi.translate.midiFileToStream(mf)
    s.show('midi')
