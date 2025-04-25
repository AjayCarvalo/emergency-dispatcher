from incident import Incident
from resources import Resource
from dispatcher import Dispatcher

def main():
    dispatcher = Dispatcher()

    while True:
        print("\n--- Emergency Dispatcher System ---")
        print("1. Add Incident")
        print("2. Add Resource")
        print("3. View Incidents")
        print("4. View Resources")
        print("5. Allocate Resources")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            itype = input("Incident Type (fire/medical): ")
            location = input("Location: ")
            priority = int(input("Priority (1 = highest): "))
            needed = input("Resources needed (comma-separated): ").split(",")
            incident = Incident(itype.strip(), location.strip(), priority, [x.strip() for x in needed])
            dispatcher.add_incident(incident)

        elif choice == "2":
            rtype = input("Resource Type (ambulance/fire_truck): ")
            location = input("Location: ")
            resource = Resource(rtype.strip(), location.strip())
            dispatcher.add_resource(resource)

        elif choice == "3":
            print(f"{'Type':<15}{'Location':<15}{'Priority':<10}{'Status':<15}")
            dispatcher.view_incidents()

        elif choice == "4":
            print(f"{'Type':<15}{'Location':<15}{'Available':<10}")
            dispatcher.view_resources()

        elif choice == "5":
            dispatcher.assign_resources()

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
