import datetime

class Incident:
    def __init__(self, incident_type, location, priority, resources_needed):
        self.incident_type = incident_type
        self.location = location
        self.priority = priority
        self.resources_needed = resources_needed
        self.status = "Unassigned"
        self.assigned_resources = []
        self.timestamp = datetime.datetime.now()

    def update_priority(self, new_priority):
        self.priority = new_priority
