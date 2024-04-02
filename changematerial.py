import bpy


    
def ChangeMaterial(MaterialName):
    baseMesh = bpy.data.objects.get("Body")
    
    new_mat = bpy.data.materials.get(MaterialName)
    Eyelashes = bpy.data.materials.get("Eyelashes")
    slot_index_to_clear = 0
    if new_mat:
        #baseMesh.data.materials.clear()
        baseMesh.material_slots[slot_index_to_clear].material = new_mat
        #baseMesh.data.materials.append(new_mat)
        
    else:
        print("no material found")
        
ChangeMaterial("Full_Body3")
