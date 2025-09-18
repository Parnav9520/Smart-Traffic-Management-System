import traci

PORT = 8873
traci.init(PORT)   # or traci.connect(port=PORT)

step = 0
while step < 1000:  # run for 1000 steps
    traci.simulationStep()   # advance simulation by 1 step
    
    # ---- Read detector data every step ----
    try:
        vehicles = traci.lanearea.getLastStepVehicleIDs("e2_0")
        occupancy = traci.lanearea.getLastStepOccupancy("e2_0")
        print(f"Step {step}: e2_0 vehicles = {vehicles}, occupancy = {occupancy}")
    except traci.exceptions.TraCIException:
        print("e2_0 not found or not a lane area detector")

    try:
        vehicles = traci.lanearea.getLastStepVehicleIDs("e2_1")
        occupancy = traci.lanearea.getLastStepOccupancy("e2_1")
        print(f"Step {step}: e2_1 vehicles = {vehicles}, occupancy = {occupancy}")
    except traci.exceptions.TraCIException:
        print("e2_1 not found or not a lane area detector")

    try:
        vehicles = traci.lanearea.getLastStepVehicleIDs("e2_3")
        occupancy = traci.lanearea.getLastStepOccupancy("e2_3")
        print(f"Step {step}: e2_3 vehicles = {vehicles}, occupancy = {occupancy}")
    except traci.exceptions.TraCIException:
        print("e2_3 not found or not a lane area detector")
    
    step += 1

traci.close()
