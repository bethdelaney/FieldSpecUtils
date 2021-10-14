"""Functions to convolve hyperspectral data to the equivalent bands of a selection of common satellite based sensors"""

import os
import numpy as np
import pandas as pd

def S2(spectra):
    """Sentinel-2 convolution""" 
    os.chdir(bands_Dir)
    for column in spectra:
        f = Bands.mul(spectra[column],axis = 0)
        f.to_csv('Bands_' + column + '.csv')
        
    for band_file in os.scandir(bands_Dir):
        file_name = pathlib.Path(band_file).stem
        convolution_process = pd.read_csv(band_file, index_col=0, header=0)
        Band_2 = (np.trapz((convolution_process.iloc[89:184, 1]), axis = 0)) / (np.trapz((Bands.iloc[89:184, 1]), axis = 0))
        Band_3 = (np.trapz((convolution_process.iloc[188:233, 2]), axis = 0)) / (np.trapz((Bands.iloc[188:233, 2])))
        Band_4 = (np.trapz((convolution_process.iloc[296:344, 3]), axis = 0)) / (np.trapz((Bands.iloc[296:344, 3]), axis = 0))
        Band_5 = (np.trapz((convolution_process.iloc[345:364, 4]), axis = 0)) / (np.trapz((Bands.iloc[345:364, 4]), axis = 0))
        Band_6 = (np.trapz((convolution_process.iloc[381:399, 5]), axis = 0)) / (np.trapz((Bands.iloc[381:399, 5]), axis = 0))
        Band_7 = (np.trapz((convolution_process.iloc[419:447, 6]), axis = 0)) / (np.trapz((Bands.iloc[419:447, 6]), axis = 0))
        Band_8 = (np.trapz((convolution_process.iloc[423:557, 7]), axis = 0)) / (np.trapz((Bands.iloc[423:557, 7]), axis = 0))
        Band_8a = (np.trapz((convolution_process.iloc[497:531, 8]), axis = 0)) / (np.trapz((Bands.iloc[497:531, 8]), axis = 0))
        Band_11 = (np.trapz((convolution_process.iloc[1189:1332, 11]), axis = 0)) / (np.trapz((Bands.iloc[1189:1332, 11]), axis = 0))
        Band_12 = (np.trapz((convolution_process.iloc[1728:1970, 12]), axis = 0)) / (np.trapz((Bands.iloc[1728:1970, 12]), axis = 0))
        convolved = {'Band name and centre wavelength (nm)': ["Band 2 - 490", "Band 3 - 560", "Band 4 - 665", "Band 5 - 705",
                                   "Band 6 - 740","Band 7 - 783", "Band 8 - 842", "Band 8a - 865",
                                   "Band 11 - 1610", "Band 12 - 2190"],
                         file_name+'SRF': [Band_2, Band_3, Band_4, Band_5, Band_6, Band_7, Band_8, Band_8a, Band_11, Band_12]}
        convolved_product = pd.DataFrame(convolved)
        convolved_product.set_index('Band name and centre wavelength (nm)', inplace = True)
        os.chdir(convolved_Dir)
        convolved_product.to_csv('convolved_' + file_name + '.csv') 
    
    collated_list = []
    for convolved_file in os.scandir(convolved_Dir):
        df = pd.read_csv(convolved_file, index_col=0, header=0)
        collated_list.append(df)

    collated_convolved = pd.concat(collated_list, axis=1)

    os.chdir(Home_Dir)
    collated_convolved.to_csv('Plots_with_convolved_bands.csv')
