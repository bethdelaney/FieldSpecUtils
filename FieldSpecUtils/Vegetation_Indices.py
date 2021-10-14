"""A selection of vegetation indices, taken from https://www.l3harrisgeospatial.com/docs/NarrowbandGreenness.html"""

def NDVI(spectra):
    """Normalized Difference Vegetation Index"""
    ndvi = ((spectra.iloc[550,] - spectra.iloc[330,])/(spectra.iloc[550,] + spectra.iloc[330,]))
    return ndvi

def RENDVI(spectra):
    """Red Edge Normalized Difference Vegetation Index"""
    rendvi = (spectra.iloc[400,] - spectra.iloc[355,])/(spectra.iloc[400,] + spectra.iloc[355,])
    return rendvi

def MRENDVI(spectra):
    """Modified Red Edge Normalized Difference Vegetation Index"""
    mrendvi = (spectra.iloc[400,] - spectra.iloc[355,])/(spectra.iloc[400,] + spectra.iloc[355,] -(2 * spectra.iloc[95,]))
    return mrendvi

def AVRI(spectra):
    """Atmospherically Resistant Vegetation Index"""
    gamma = float(input("Please input an atmospheric scaling factor (gamma) = "))
    avri = ((spectra.iloc[450,] - (spectra.iloc[355,] - (gamma * (spectra.iloc[100,] - spectra.iloc[330,]))))/
            spectra.iloc[450,] + (spectra.iloc[355,] - (gamma * (spectra.iloc[100,] - spectra.iloc[330,]))))
    return avri

def MCARI(spectra):
    """Modified Chlorophyll Absorption Ratio Index"""
    mcari = = ((spectra.iloc[350,] - spectra.iloc[320,]) - (0.2*(spectra.iloc[350,] - spectra.iloc[200,]))) * (spectra.iloc[350,] / spectra.iloc[320,])
