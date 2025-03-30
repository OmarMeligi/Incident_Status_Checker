#!/bin/bash

echo "Enter Your INC:"
read inc


# Fetch incident details
tic=$(awk -F, -v search="$inc" '$1 == search {print $1; exit}' Tickets_Status.txt)
tic_st=$(awk -F, -v search="$inc" '$1 == search {print $2; exit}' Tickets_Status.txt)
ev_id=$(awk -F, -v search="$inc" '$1 == search {print $2; exit}' incident_Event.txt)
ev_st=$(awk -F, -v search="$ev_id" '$1 == search {print $2; exit}' Events_Status.txt)

if ! grep -q "^$inc," incident_Event.txt; then
    echo "ERROR: Incident $inc not found in incident_Event.txt."
    exit 1
fi

# Debugging: Check existing values
echo "DEBUG: Incident ID: $tic"
echo "DEBUG: Incident Status: $tic_st"
echo "DEBUG: Event ID: $ev_id"
echo "DEBUG: Event Status: $ev_st"


echo "Now we are checking."

# If the incident exists but its status is Closed
if [[ "$tic_st" == "Closed" ]]; then
    if [[ "$tic_st" == "$ev_st" ]]; then
        echo "Closed, no update needed."
        exit 0
    else
        echo "Incident is closed but event status is not updated. Modifying the event status ..."

        # Backup before modifying
        cp Events_Status.txt Events_Status_backup.txt

        # Debugging: Check if event ID is empty
        if [[ -z "$ev_id" ]]; then
            echo "ERROR: Event ID not found for Incident $inc."
            exit 1
        fi

        # Update event status safely
        awk -F, -v search="$ev_id" -v new_status="Closed" 'BEGIN {OFS=","} 
        {if ($1 == search) $2 = new_status} 1' Events_Status.txt > temp_file && mv temp_file Events_Status.txt

        echo "Event: $ev_id status updated to Closed in Events_Status.txt"
    fi
else
    echo "Incident still in progress."
fi
