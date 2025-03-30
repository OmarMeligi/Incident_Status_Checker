import csv
import random
import uuid

# Declare Incident Numbers
def INC():                       
    num = []
    for i in range(10):
        x = f"INC{random.randint(10**9, 10**10 - 1)}"
        num.append(x)
    return num  

# Declare Status
def Stat():
    Status = []
    values = ["Open", "Closed"]
    for i in range(10):
        Status.append(random.choice(values))
    return Status  

# Declare Description
def Des():
    Describtion = []
    val = [
        "User unable to log in",
        "Server downtime issue",
        "Printer not working",
        "Email delivery failure",
        "Software crash on startup",
        "VPN connection issue",
        "Network connectivity slow",
        "Database backup failed",
        "Password reset request",
        "Website loading error"
    ]
    for i in range(10):
        Describtion.append(random.choice(val)) 
    return Describtion  

#============================== Asking user about File name ===========================================
Tickets_name = input("Enter the file name of tickets (without extension): ") + ".csv"

#==================================     Write Csv File  =====================================
# Call Functions
Inc = INC()
Status = Stat()
Desc = Des()

# Write Ticket file
with open(Tickets_name, "w", newline="") as ti:
    x = csv.writer(ti)
    x.writerow(["Incident Number", "Status", "Description"])  # Write header
    for i in range(10):
        x.writerow([Inc[i], Status[i], Desc[i]])

#========================================= Read ticket File  ============================================
with open(Tickets_name, "r", newline="") as ti:
    y = csv.reader(ti)
    for i in y:
        print(",".join(i))

#================================= Create Event table ====================
# Creation of Events Id
def events():
    Events = []
    for i in range(10):
        Events.append(str(uuid.uuid4()))
    return Events

#=============================== Asking for events file name ===============
Events_name = input("Enter the file name of Events (without extension): ") + ".csv"

# Use the same incident numbers from the ticket file
eve = events()

# Write Event file
with open(Events_name, "w", newline="") as nv:
    n = csv.writer(nv)
    n.writerow(["Incident Number", "Event_ID"])  # Write header
    for i in range(10):
        n.writerow([Inc[i], eve[i]])  # Use the same Inc list

#========================================= Read Event file  ============================================
with open(Events_name, "r", newline="") as ns:
    h = csv.reader(ns)
    for i in h:
        print(",".join(i))

#================================= Create Third File: Event_Status ==========================
Event_Status_name = input("Enter the file name for Event Status (without extension): ") + ".csv"

# Generate Status for Events
Event_Status = Stat()  # Reuse Status function for Event Status

# Write Event Status file
with open(Event_Status_name, "w", newline="") as es:
    es_writer = csv.writer(es)
    es_writer.writerow(["Event_ID", "Status"])  # Write header
    for i in range(10):
        es_writer.writerow([eve[i], Event_Status[i]])  # Match Event_ID with Status

#========================================= Read Event Status file  ============================================
with open(Event_Status_name, "r", newline="") as es:
    es_reader = csv.reader(es)
    for i in es_reader:
        print(",".join(i))
