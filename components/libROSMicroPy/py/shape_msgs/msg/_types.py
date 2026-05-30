_TYPE_DEFS = {
    'Mesh': ('Mesh', 'shape_msgs::msg', (('triangles', 'MeshTriangle', (('vertex_indices', 'uint32', (), True, False, 3),), False, True, 0), ('vertices', 'Point', (('x', 'float64', (), False, False, 0), ('y', 'float64', (), False, False, 0), ('z', 'float64', (), False, False, 0)), False, True, 0))),
    'MeshTriangle': ('MeshTriangle', 'shape_msgs::msg', (('vertex_indices', 'uint32', (), True, False, 3),)),
    'Plane': ('Plane', 'shape_msgs::msg', (('coef', 'float64', (), True, False, 4),)),
    'SolidPrimitive': ('SolidPrimitive', 'shape_msgs::msg', (('type', 'uint8', (), False, False, 0), ('polygon', 'Polygon', (('points', 'Point32', (('x', 'float32', (), False, False, 0), ('y', 'float32', (), False, False, 0), ('z', 'float32', (), False, False, 0)), False, True, 0),), False, False, 0))),
}
