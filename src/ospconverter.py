# -*- coding: utf-8 -*-
# Copyright 2018 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import glob
import thinkdsp

def catOrDog(filename):
    if 'dog_barking' in fileName:
        return 'dog'
    else:
        return 'cat'

def searchInArray(last, freq, data):
    curr = last
    #print('Looking for %d' % freq)
    for s in range(last, data.size):
        if freq < int(data[s]):
            if s > 0:
                 curr = s
                 break
    return curr


def writeSpectogramToFile(file, spectrum):
    pos = 0
    #print('In writeSpectoramToFile')
    for freq in range(10, 8000, 53):
        pos = searchInArray(pos, freq, spectrum.fs)
        file.write(str(spectrum.hs[pos].real))
        file.write(',')
    file.write('\n')
    #print('Last Postion found at %d' % pos)

def writeSignatureToFile(file, spectrum):
    #print('In writeSignatureToFile')
    for e in spectrum:
        file.write(str(e['fs']))
        file.write(',')
        file.write(str(e['hs']))
        file.write(',')
    file.write('\n')    

def runOSP(spectrumFile, signatureFile, fileName):
    test_wave = thinkdsp.read_wave(fileName)
    spectrum = test_wave.make_spectrum()
    spectrumFile.write(catOrDog(fileName))
    spectrumFile.write(',')
    signatureFile.write(catOrDog(fileName))
    signatureFile.write(',')
    writeSpectogramToFile(spectrumFile, spectrum)
    signature = spectrum.make_signature(20)
    writeSignatureToFile(signatureFile, signature)

    #print(signature)

    #print('New Spectrum with')
    #print('hs array shape ', spectrum.hs.shape)
    #print('fs array shape ', spectrum.fs.shape)
    #print('fs array last entry is ', spectrum.fs.size)
    #print('fs array entry 0 is ', spectrum.fs[0])
    #print('hs array entry 0 is ', spectrum.hs[0])
    #print('fs array entry 1 is ', spectrum.fs[1])
    #print('hs array entry 1 is ', spectrum.hs[1])
    #print('fs array entry 2 is ', spectrum.fs[2])
    #print('hs array entry 2 is ', spectrum.hs[2])
    #print('fs array 2nd last entry is ', spectrum.fs[-2])
    #print('hs array 2nd last entry is ', spectrum.hs[-2])
    #print('fs array last entry is ', spectrum.fs[-1])
    #print('hs array last entry is ', spectrum.hs[-1])

print('OSP Converter Application is starting')

fileListCats = glob.glob("../audio/cats_dogs/train/cat/*.wav")
fileListDogs = glob.glob("../audio/cats_dogs/train/dog/*.wav")

spectrumFile = open('../output/spectrum.csv', 'w')
signatureFile = open('../output/signature.csv', 'w')

print('Writing Column Headers')
for c in range(1, 153):
    colName = "COLUMN{}".format(c)
    spectrumFile.write(colName)
    spectrumFile.write(',')

print('Writing Column Headers')
for c in range(1, 42):
    colName = "COLUMN{}".format(c)
    signatureFile.write(colName)
    signatureFile.write(',')

spectrumFile.write('\n')
signatureFile.write('\n')

for animalList in [fileListCats, fileListDogs]:
    for fileName in animalList:
        runOSP(spectrumFile, signatureFile, fileName)
        # print(fileName)

spectrumFile.close()
signatureFile.close()

print('OPS Converter Application is completing')
