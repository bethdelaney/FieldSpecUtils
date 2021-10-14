def NDVI(spectra):
    ndvi = ((spectra.iloc[550,] - spectra.iloc[330,])/(spectra.iloc[550,] + spectra.iloc[330,]))
    return ndvi

def RENDVI(spectra):
    rendvi = (spectra.iloc[400,] - spectra.iloc[355,])/(spectra.iloc[400,] + spectra.iloc[355,])
    return rendvi

def MRENDVI(spectra):
    mrendvi = (spectra.iloc[400,] - spectra.iloc[355,])/(spectra.iloc[400,] + spectra.iloc[355,] -(2 * spectra.iloc[95,]))
    return mrendvi

def AVRI(spectra):
    gamma = float(input("Please input an atmospheric scaling factor (gamma) = "))
    avri = ((spectra.iloc[450,] - (spectra.iloc[355,] - (gamma * (spectra.iloc[100,] - spectra.iloc[330,]))))/
            spectra.iloc[450,] + (spectra.iloc[355,] - (gamma * (spectra.iloc[100,] - spectra.iloc[330,]))))
    return avri
