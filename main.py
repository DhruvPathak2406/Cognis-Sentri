from alert_module.alert import AlertSystem
alert_system = AlertSystem()
# Example simulation
while True:
    action = int(input("Enter action (0-3): "))
    alert_system.execute(action)