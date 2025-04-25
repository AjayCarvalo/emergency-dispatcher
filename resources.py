class Resource:
    def __init__(self, resource_type, location):
        self.resource_type = resource_type
        self.location = location
        self.available = True
        self.assigned_to = None

    def mark_assigned(self, incident):
        self.available = False
        self.assigned_to = incident

    def mark_available(self):
        self.available = True
        self.assigned_to = None
