# My first python file
# bpy.ops.wm.addon_expand(module="io_vertex_weight")

import bpy

bl_info = {
    "name": "Vertex Weight Export",
    "author": "Harrison Andrews",
	"description": "An ascii exporter that stores just a meshs's vertex weights to their skeleton",
	"location": "File > Export",
	"version": (1, 0),
    "blender": (2, 6, 4),
    "warning": "", # used for warning icon and text in addons panel
    "category": "Import-Export"}
	
from bpy_extras.io_utils import (ExportHelper,
                                 ImportHelper,
                                 path_reference_mode,
                                 axis_conversion,
                                 )
								 
def writefile(self):

    filename = self.filepath
    out = open(filename, 'w')
    sce = bpy.data.scenes[0]
    mesh = bpy.data.meshes[0]
    out.write("#Harry's Vertex Weight Export Version 1.0\n\n")
	
    for vert in mesh.vertices:
        out.write("w")

        for i in range(0,4):
            try:
                out.write(" %i %f" % (vert.groups[i].group,vert.groups[i].weight))
            except:
                out.write(" %i %f" % (0,0))			
        out.write("\n")
				
    out.close()      
	

class ExportWeights(bpy.types.Operator, ExportHelper):
    
    bl_idname = "export_weights.hvw" 
    bl_label = 'Vertex Weight Export'
    bl_options = {'PRESET'}
	
    filename_ext = ".hvw"
	
    def execute(self, context):
        writefile(self)      
        return {'FINISHED'}
	
def menu_func_export(self, context):
    self.layout.operator(ExportWeights.bl_idname, text="Harry Vertex Weight (.hvw)")
	
def	register():
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_file_export.append(menu_func_export)

def	unregister():
    bpy.types.INFO_MT_file_export.remove(menu_func_export)	
	
if __name__ == "__main__":
    register()