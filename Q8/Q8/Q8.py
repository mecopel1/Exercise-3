import arcpy

arcpy.env.workspace=r'D:\Grad_Spring2019\610-Programming\Exercise3\Exercise 3.gdb'
recordCount=arcpy.GetCount_management('CallsforService')
print(recordCount) 