import config
from shape import shape_object

class world_object:
    def __init__(self) -> None:
        self.shapes = []


    def add_shape(self, position, vertices):
        new_shape = shape_object(position, vertices) 
        self.shapes.append(new_shape)
        return new_shape


    def handle_collisions(self):
        for i, shape1 in enumerate(self.shapes):
            for j in range(i+1, len(self.shapes)):
                shape2 = self.shapes[j]
                if shape1 is not shape2 and shape1.handle_collisions(shape2):
                    return self.update_variables()


    def update_variables(self):
        self.handle_collisions()

        for shape in self.shapes:
            shape.velocity = 0


    def draw(self, surface):
        for shape in self.shapes:
            shape.draw(surface)

