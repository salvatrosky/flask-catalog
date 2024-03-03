class Prize:
    def __init__(self, id, catalog_id, title, description, image):
        self.id = id
        self.catalog_id = catalog_id
        self.title = title
        self.description = description
        self.image = image

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'image': self.image
        }
