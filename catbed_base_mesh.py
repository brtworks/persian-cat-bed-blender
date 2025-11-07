import bpy
from math import pi

# Remove default cube
def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    for block in bpy.data.meshes:
        bpy.data.meshes.remove(block)
    for block in bpy.data.materials:
        bpy.data.materials.remove(block)
    for block in bpy.data.images:
        bpy.data.images.remove(block)

# Create donut base (torus)
def create_bed_base():
    bpy.ops.mesh.primitive_torus_add(major_radius=0.34, minor_radius=0.13, major_segments=64, minor_segments=24, location=(0,0,0))
    bed = bpy.context.active_object
    bed.name = "CatBedBase"
    # Flatten inside faces
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.mesh.select_non_manifold()
    bpy.ops.mesh.region_to_loop()
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.object.mode_set(mode='OBJECT')
    return bed

# Main
clear_scene()
bed = create_bed_base()
