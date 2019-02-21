import arcpy

arcpy.env.overwriteOutput=True
arcpy.env.workspace=r'D:\Grad_Spring2019\610-Programming\Exercise3\Exercise 3.gdb'

#create feature class
path=r'D:\Grad_Spring2019\610-Programming\Exercise3\Exercise 3.gdb'
featureClass= arcpy.CreateFeatureclass_management(path,'Question8')

#add a field
fieldName='Places'
arcpy.AddField_management(featureClass,fieldName,'TEXT')

#add a domain
gdb=r'D:\Grad_Spring2019\610-Programming\Exercise3\Exercise 3.gdb'
fc='Question8'
domain='Places'
field='Places'


arcpy.CreateDomain_management(gdb,domain,'places', 'TEXT', 'CODED')

domDict={'WLDNS':'Wilderness','LK':'Lake', 'RV':'River', 'CG':'Camp Ground', 'OT':'Other'}

for code in domDict:
    arcpy.AddCodedValueToDomain_management(gdb,domain,code, domDict[code])

arcpy.AssignDefaultToField_management(fc, field, domain)


