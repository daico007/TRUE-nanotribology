import numpy as np
import mbuild as mb


class DualSurface(mb.Compound):
    """ A recipe for creating a system with two opposing surfaces.
    """
    def __init__(self, top, bottom, separation=0.8):
        super(DualSurface, self).__init__()
        
        top.spin(np.pi, around=[0, 1, 0])
        top_bounding = top.get_boundingbox()
        bot_bounding = bottom.get_boundingbox()
        top.translate([0, 0, bot_bounding.lengths[2] + separation])
        self.add(bottom)
        self.add(top)

        box = mb.Box(lengths=(bottom.box.lengths[0],
                              bottom.box.lengths[1],
                              bot_bounding.lengths[2] + separation + top_bounding.lengths[2]))
        self.box = box
