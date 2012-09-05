from netCDF4 import Dataset
import numpy
from numpy.core.numeric import array

class NetCDFFacade:

    def __init__(self, filename):
        self.dataSet = Dataset(filename, 'r', format='NETCDF4_CLASSIC')

    def getDimSize(self, dimName):
        dimensions = self.dataSet.dimensions
        for currentDimName in dimensions:
            if currentDimName == dimName:
                return len(dimensions[currentDimName])

    def getGlobalAttribute(self, attributeName):
        globalAttributes = self.dataSet.ncattrs
        for currentAttribute in globalAttributes():
            if currentAttribute == attributeName:
                return self.dataSet.__getattribute__(attributeName)

    def getVariable(self, variableName):
        variables = self.dataSet.variables
        for currentVarName in variables:
            if currentVarName == variableName:
                return variables[currentVarName]

    def getVariableAttribute(self, variableName, attributeName):
        variable = self.getVariable(variableName)
        return variable.__getattribute__(attributeName)

    def getDimensionString(self, variableName):
        variable = self.getVariable(variableName)
        dimensionString = ""
        for dimName in variable._getdims():
            dimensionString = dimensionString + dimName + " "
        dimensionString = dimensionString.strip()
        return dimensionString

    def getDimLength(self, variableName, index):
        variable = self.getVariable(variableName)
        variableDimensions = variable._getdims()
        for i in range(len(variableDimensions)):
            if i == index:
                dimName = variableDimensions[i]
                return self.getDimSize(dimName)

    def getData(self, variableName, origin, shape):
        variable = self.getVariable(variableName)
        dimCount = len(variable._getdims())
        if dimCount != len(origin) or dimCount != len(shape):
            raise ValueError("len(origin) and len(shape) must be equal to number of dimensions of variable '" + variableName + "'")
        indexArray = range(0, dimCount)
        for dimIdx in range(dimCount):
            j = 0
            innerArray = range(0, shape[dimIdx])
            for index in range(origin[dimIdx], origin[dimIdx] + shape[dimIdx]):
                innerArray[j] = index
                j += 1
            indexArray[dimIdx] = innerArray
        return variable[indexArray]

    def getDataForLatLonTime(self, variableName, minTime, maxTime, minLat, maxLat, minLon, maxLon):
        variable = self.getVariable(variableName)
        time = numpy.array(self.getVariable("time"))
        lat = numpy.array(self.getVariable("latitude"))
        lon = numpy.array(self.getVariable("longitude"))

        return variable[(minTime <= time) & (time <= maxTime), (minLat <= lat) & (lat <= maxLat), (minLon <= lon) & (lon <= maxLon)]

    def close(self):
        self.dataSet.close()