last_service_km = int(input("Enter last service KM: "))
current_km = int(input("Enter current KM: "))

if current_km - last_service_km >= 3000:
    print("Service Due")
else:
    print("No Service Needed")
