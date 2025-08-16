class Segment: 
    def __init__(self, seg_id, slot):
        self.id = seg_id
        self.slot = slot

    def get_base_limit(self):
        base, limit = self.slot
        return base, limit

    def __str__(self):
        return f"Segment=[id={self.id},slot={self.slot}]"

    def __repr__(self):
        return f"Segment=[id={self.id},slot={self.slot}]"


