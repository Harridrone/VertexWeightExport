# My first python file
# bpy.ops.wm.addon_expand(module="io_vertex_weight")

import bpy

bl_info = {
    "name": "Vertex Weight Export",
    "author": "Harrison Andrews",
    "description": "An ascii exporter that stores just a meshs's vertex weights to their skeleton",
    "location": "File > Import-Export",
    "version": (2, 0),
    "blender": (2, 81, 6),
    "warning": "", # used for warning icon and text in addons panel
    "category": "Import-Export",
    "support": 'COMMUNITY',
}

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
    out.write("#Harry's Vertex Weight Export Version 2.0\n\n")

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
        bpy.ops.object.vertex_group_normalize_all()
        writefile(self)      
        return {'FINISHED'}

def menu_func_export(self, context):
    self.layout.operator(ExportWeights.bl_idname, text="Harry Vertex Weight (.hvw)")

def register():
    bpy.utils.register_class(ExportWeights)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)

def unregister():
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)
    bpy.utils.unregister_class(ExportWeights)

if __name__ == "__main__":
    register()