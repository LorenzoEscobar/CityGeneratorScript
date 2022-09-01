import bpy
import random

### CITY GENERATOR SCRIPT ###

#Generate a quick set of buildings in a predetermined area set by LOCATION,
#Easily adjust the range of SCALE for buildings you would like to have. 
#Adjust total size range with SIZE, (recommended to keep default [2,5])
#All buildings will have a small box representing a generator on top as well as an antenna.
#Materials are provided but can easily be modified to your liking.

#Contact LE.LorenzoEscobar@gmail.com for any assistance or questions!

for x in range(15): #Change amount of buildings you want to generate here. [Default: 15]
    
    locx = random.randint(1,400)  #LOCATION [XYZ]
    locy = random.randint(1,250)
    locz = random.randint(10,25)

    scax = random.randint(5,9)    #SCALE    [XYZ]
    scay = random.randint(5,9)
    scaz = random.randint(5,35)
    
    SIZE = random.randint(2,5)    # SIZE
   
    LOC = (locx,locy,locz)        # LOCATION
    SCA = (scax,scay,scaz)        # SCALE
      
      
    BUILDING = bpy.ops.mesh.primitive_cube_add(size=SIZE, enter_editmode=False, align='WORLD', location=(LOC), scale=(SCA)) #CUBE - BUILDING
    
   
    ## Applies material to first set of objects, [the BUILDING]
    ob = bpy.context.active_object

    matlist = ["building.001","building.002","building.003","building.004"]
    
    ranlist = random.choice(matlist) 
    
    
    mat = bpy.data.materials.get(ranlist) #GET MATERIAL
    ob.data.materials.append(mat)         #ASSIGN MATERIAL TO OBJ
    ##
    
    
  
    ### ROOF VARIABLES
    LOCROOF = (locx,locy,locz+.1)            #LOCATION
    SCAROOF = (scax-.2,scay-.2,scaz+.5)      #SIZE
   
    ROOF = bpy.ops.mesh.primitive_cube_add(size=SIZE, enter_editmode=False, align='WORLD', location=(LOCROOF), scale=(SCAROOF)) #CUBE - ROOF
    
    
    
    ## Applies material to second set of objects, [the ROOF]
    ob = bpy.context.active_object

    matlist = ["roof.001","roof.002","roof.003","roof.004"]
    
    ranlist = random.choice(matlist) 
    
    
    mat = bpy.data.materials.get(ranlist) #GET MATERIAL
    ob.data.materials.append(mat)         #ASSIGN MATERIAL TO OBJ
    ##
    
   
    ANTRAN =  random.randint(9,15)
    
    #ANTENNA 
    LOCANT = (locx-2,locy+2,locz+ANTRAN)      
    SCAANT = (.09,.09,scaz-1.5) 
   
    ANT = bpy.ops.mesh.primitive_cube_add(size=SIZE, enter_editmode=False, align='WORLD', location=(LOCANT), scale=(SCAANT)) #CUBE - ANTENNA
   
    ## Applies material to third set of objects, [the ANTENNA] (uses same roof materials)
    ob = bpy.context.active_object

    matlist = ["roof.001","roof.002","roof.003","roof.004"]
    
    ranlist = random.choice(matlist) 
    
    
    mat = bpy.data.materials.get(ranlist) #GET MATERIAL
    ob.data.materials.append(mat)         #ASSIGN MATERIAL TO OBJ
    ##

    #GENERATOR
    GENRAN =  random.randint(2,5)
    
    LOCGEN = (locx+GENRAN,locy-GENRAN,locz+4)      
    SCAGEN = (1,1,scaz) 
    
    GEN = bpy.ops.mesh.primitive_cube_add(size=SIZE, enter_editmode=False, align='WORLD', location=(LOCGEN), scale=(SCAGEN)) #CUBE - GENERATOR
    
    ## Applies material to forth set of objects, [the GENERATOR]
    ob = bpy.context.active_object

    matlist = ["gen.001","gen.002","gen.003","gen.004"]
    
    ranlist = random.choice(matlist) 
    
    
    mat = bpy.data.materials.get(ranlist) #GET MATERIAL
    ob.data.materials.append(mat)         #ASSIGN MATERIAL TO OBJ
    ##