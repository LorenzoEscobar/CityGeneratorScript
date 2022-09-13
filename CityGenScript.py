
import bpy
import random

### CITY GENERATOR SCRIPT ###

#Generate a quick set of buildings in a defined area set by user length using a GUI,
#Choose how many buildings you want to generate and the length of the area.
#All buildings will have a small box representing a generator on top as well as an antenna.
#Materials are provided but can easily be modified to your liking.

#Contact LE.LorenzoEscobar@gmail.com for any assistance or questions!

class CityGen(bpy.types.Operator):
    
    bl_label = "|||City Generator Script||| -Hover over values for tooltips!-" 
    bl_idname = "citygen.myop"                                                 
   
    
    #GUI 
    amt:bpy.props.IntProperty(name="Amount: ", min=5, max=100,default=15,description="This is the amount of buildings you want to generate. [Default:15]")  
    userlenx:bpy.props.IntProperty(name="  X Length: ", min=1, max=9999,default=400,description="This is how long you want X to be for where the buildings will generate. [Default:400]")
    userleny:bpy.props.IntProperty(name="  Y Length: ", min=1, max=9999,default=250,description="This is how long you want Y to be for where the buildings will generate. [Default:250]")
    
  
    def execute(self,context):
         #Preparing User inputted variables
         amt = self.amt
         userlenx =self.userlenx
         userleny =self.userleny
        
         
         
         ### MAIN SCRIPT START ###
         for x in range(amt): #Change amount of buildings you want to generate here. [Default: 15]
            
            lenx = random.randint(1,userlenx)  #LENGTH [XYZ]
            leny = random.randint(1,userleny)
            lenz = random.randint(10,25)

            scax = random.randint(5,9)         #SCALE  [XYZ]
            scay = random.randint(5,9)
            scaz = random.randint(5,35)
            
            SIZE = random.randint(2,5)         # SIZE
        
            len = (lenx,leny,lenz)             # LENGTH, combined values
            SCA = (scax,scay,scaz)             # SCALE,  combined values
            
            
            BUILDING = bpy.ops.mesh.primitive_cube_add(size=SIZE, enter_editmode=False, align='WORLD', location=(len), scale=(SCA)) #CUBE - BUILDING
            
        
            ## Applies material to first set of objects, [the BUILDING]
            ob = bpy.context.active_object

            matlist = ["building.001","building.002","building.003","building.004"] #This is the list of materials that can be used, they are chosen randomly.
                                                                                    #You may add more and remove some, Make sure your materials have the same name as in the list.
                                                                                
            
            ranlist = random.choice(matlist) 
            
            
            mat = bpy.data.materials.get(ranlist) #GET MATERIAL
            ob.data.materials.append(mat)         #ASSIGN MATERIAL TO OBJ
            ##
            
            
        
            ### ROOF VARIABLES
            lenROOF = (lenx,leny,lenz+.1)         #LENGTH
            SCAROOF = (scax-.2,scay-.2,scaz+.5)   #SIZE
        
            ROOF = bpy.ops.mesh.primitive_cube_add(size=SIZE, enter_editmode=False, align='WORLD', location=(lenROOF), scale=(SCAROOF)) #CUBE - ROOF
            
            
            
            ## Applies material to second set of objects, [the ROOF]
            ob = bpy.context.active_object

            matlist = ["roof.001","roof.002","roof.003","roof.004"]
            
            ranlist = random.choice(matlist) 
            
            
            mat = bpy.data.materials.get(ranlist) #GET MATERIAL
            ob.data.materials.append(mat)         #ASSIGN MATERIAL TO OBJ
            ##
            
        
            ANTRAN =  random.randint(9,15)
            
            #ANTENNA 
            lenANT = (lenx-2,leny+2,lenz+ANTRAN)      
            SCAANT = (.09,.09,scaz-1.5) 
        
            ANT = bpy.ops.mesh.primitive_cube_add(size=SIZE, enter_editmode=False, align='WORLD', location=(lenANT), scale=(SCAANT)) #CUBE - ANTENNA
        
            ## Applies material to third set of objects, [the ANTENNA] (uses same roof materials)
            ob = bpy.context.active_object

            matlist = ["roof.001","roof.002","roof.003","roof.004"]
            
            ranlist = random.choice(matlist) 
            
            
            mat = bpy.data.materials.get(ranlist) #GET MATERIAL
            ob.data.materials.append(mat)         #ASSIGN MATERIAL TO OBJ
            

            #GENERATOR
            GENRAN =  random.randint(2,5)
            
            lenGEN = (lenx+GENRAN,leny-GENRAN,lenz+4)      
            SCAGEN = (1,1,scaz) 
            
            GEN = bpy.ops.mesh.primitive_cube_add(size=SIZE, enter_editmode=False, align='WORLD', location=(lenGEN), scale=(SCAGEN)) #CUBE - GENERATOR
            
            ## Applies material to forth set of objects, [the GENERATOR]
            ob = bpy.context.active_object

            matlist = ["gen.001","gen.002","gen.003","gen.004"]
            
            ranlist = random.choice(matlist) 
            
            
            mat = bpy.data.materials.get(ranlist) #GET MATERIAL
            ob.data.materials.append(mat)         #ASSIGN MATERIAL TO OBJ
            ### MAIN SCRIPT END ###
            
        
       

    def invoke(self,context,event):               #Opens UI
        
        return context.window_manager.invoke_props_dialog(self)
    
def register():                                   #Blender functions that activate and deactivate the script/addon.
    bpy.utils.register_class(CityGen)
    
def unregister():
    bpy.utils.unregister_class(CityGen)
    
    
if __name__ == "__main__":
    register()                                    #Activates the script/addon.
    bpy.ops.CityGen.myop('INVOKE_DEFAULT')        #Opens UI