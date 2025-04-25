from incident import Incident
from resources import Resource
import datetime

class Dispatcher:
    def __init__(self):
        self.incidents = []
        self.resources = []

    def log(self, message):
        print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}")

    def add_incident(self, incident):
        self.incidents.append(incident)
        self.incidents.sort(key=lambda x: x.priority)
        self.log(f"Incident added: {incident.incident_type} at {incident.location}")

    def add_resource(self, resource):
        self.resources.append(resource)
        self.log(f"Resource added: {resource.resource_type} at {resource.location}")

    def view_incidents(self):
        for i in self.incidents:
            print(f"{i.incident_type:<15}{i.location:<15}{i.priority:<10}{i.status:<15}")

    def view_resources(self):
        for r in self.resources:
            print(f"{r.resource_type:<15}{r.location:<15}{'Yes' if r.available else 'No':<10}")

    def assign_resources(self):
        self.incidents.sort(key=lambda x: x.priority)
        for incident in self.incidents:
            if incident.status == "Assigned":
                continue
            allocated = []
            for needed in incident.resources_needed:
                for resource in self.resources:
                    if resource.resource_type == needed and resource.available:
                        resource.mark_assigned(incident)
                        allocated.append(resource)
                        break
            if len(allocated) == len(incident.resources_needed):
                incident.status = "Assigned"
                incident.assigned_resources = allocated
                self.log(f"Resources assigned to {incident.incident_type} at {incident.location}")
            else:
                for r in allocated:
                    r.mark_available()
                self.reallocate_resources(incident)

    def reallocate_resources(self, critical_incident):
        self.log(f"Attempting reallocation for {critical_incident.incident_type} at {critical_incident.location}")
        for lower_incident in reversed(self.incidents):
            if lower_incident.priority > critical_incident.priority and lower_incident.status == "Assigned":
                for res in lower_incident.assigned_resources:
                    if res.resource_type in critical_incident.resources_needed:
                        self.log(f"Reallocating {res.resource_type} from {lower_incident.incident_type} to {critical_incident.incident_type}")
                        res.mark_available()
                        lower_incident.assigned_resources.remove(res)
                        lower_incident.status = "Unassigned"
                        self.assign_resources()
                        return
