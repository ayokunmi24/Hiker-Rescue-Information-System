

#Import
import csv
import datetime
from operator import itemgetter 
CSVFILE = 'Hiker-Rescues-PE6.csv'

#Assignment header goes here

BANNER_LINE1 = '*' * 70
LINE1 = '-' * 25
INDENT_1 = ' ' * 3

BANNER_LINE2 = '=' * 30
LINE2 = '-' * 21 #List of trails
LINE3 = '-' * 20
LINE4 = '-' * 16
LINE5 = '-' * 10
LINE6 = '-' * 7
LINE7 = '-' * 11
LINE8 = '-' * 16 
LINE9 = '-' * 11
BANNER_LINE3 = '-' * 55
APPLICATION_NAME  = 'Victorino Hiker Rescue Information System'


#1D LIST ---------------

TRAIL_NAMES = ['Aspen Pass', 'Crystal Canyon Trail', 'Shadow Trail', 'Granite Loop', 'River Overlook', 'Maple Loop', 'Mossy Trail', 'Thunder Summit', 'Cedar Canyon Trail', 'Mossy Pass', 
    'Sunset Overlook', 'Redrock Summit', 'Willow Trail', 'Shadow Loop', 'Silver Pass', 'Golden Trail', 'Bear Overlook', 'Sage Loop', 'Thunder Pass', 'Canyon Summit', 
    'Hidden Trail', 'River Loop', 'Aspen Summit', 'Crystal Pass', 'Cedar Loop', 'Golden Summit', 'Maple Canyon Trail', 'Silver Overlook', 'Hidden Pass', 'River Trail', 
    'Mossy Overlook', 'Redrock Trail', 'Pine Loop', 'Canyon Pass', 'Eagle Summit', 'Willow Pass', 'Golden Canyon Trail', 'River Pass', 'Aspen Loop', 'Golden Pass', 
    'Hidden Summit', 'Crystal Loop', 'Redrock Overlook', 'Sage Trail', 'Silver Loop', 'Bear Pass', 'Crystal Summit', 'Thunder Loop', 'Bluebonnet Trail', 'Granite Pass']

#2D LIST ---------------

TRAILS = [
['Aspen Pass', 'Flagstaff', 'AZ', 35.19, -111.68, 'Meadow Station', 35.18, -111.67, 'Falls Station', 35.22, -111.65, 'forest', 'Moderate', 2045, 0],
    ['Crystal Canyon Trail', 'Fort Collins', 'CO', 40.61, -105.07, 'Ridge Station', 40.63, -105.05, 'Fork Station', 40.59, -105.11, 'wildflowers', 'Moderate', 7740, 0],
    ['Shadow Trail', 'Sedona', 'AZ', 34.89, -111.73, 'Creek Station', 34.87, -111.74, 'Meadow Station', 34.9, -111.7, 'wildlife', 'Moderate', 5886, 0],
    ['Granite Loop', 'Bozeman', 'MT', 45.68, -111.04, 'Falls Station', 45.67, -111.01, 'Falls Station', 45.7, -111.09, 'rocky path', 'Hard', 7162, 0],
    ['River Overlook', 'Jackson', 'WY', 43.49, -110.76, 'Bench Station', 43.48, -110.75, 'Bridge Station', 43.46, -110.78, 'river', 'Moderate', 5202, 0],
    ['Maple Loop', 'Salt Lake City', 'UT', 40.76, -111.88, 'Bridge Station', 40.75, -111.86, 'Falls Station', 40.78, -111.83, 'lake view', 'Moderate', 8294, 0],
    ['Mossy Trail', 'Moab', 'UT', 38.58, -109.55, 'Saddle Station', 38.57, -109.57, 'Ridge Station', 38.59, -109.52, 'meadows', 'Moderate', 7168, 0],
    ['Thunder Summit', 'Denver', 'CO', 39.75, -104.98, 'Overlook Station', 39.76, -105.0, 'Falls Station', 39.74, -105.03, 'steep climb', 'Hard', 9184, 0],
    ['Cedar Canyon Trail', 'Jackson', 'WY', 43.48, -110.79, 'Creek Station', 43.46, -110.75, 'Saddle Station', 43.51, -110.82, 'forest', 'Moderate', 6479, 0],
    ['Mossy Pass', 'Fort Collins', 'CO', 40.61, -105.07, 'Falls Station', 40.61, -105.07, 'Cave Station', 40.62, -105.11, 'wildlife', 'Moderate', 5896, 0],
    ['Sunset Overlook', 'Sedona', 'AZ', 34.86, -111.76, 'Fork Station', 34.85, -111.78, 'Bridge Station', 34.88, -111.72, 'lake view', 'Moderate', 6032, 0],
    ['Redrock Summit', 'Moab', 'UT', 38.56, -109.52, 'Bench Station', 38.54, -109.53, 'Falls Station', 38.59, -109.48, 'steep climb', 'Hard', 8431, 0],
    ['Willow Trail', 'Denver', 'CO', 39.77, -104.96, 'Creek Station', 39.75, -104.98, 'Ridge Station', 39.78, -105.01, 'wildflowers', 'Moderate', 7028, 0],
    ['Shadow Loop', 'Salt Lake City', 'UT', 40.77, -111.85, 'Saddle Station', 40.78, -111.83, 'Bench Station', 40.79, -111.82, 'forest', 'Moderate', 7814, 0],
    ['Silver Pass', 'Bozeman', 'MT', 45.69, -111.05, 'Bridge Station', 45.68, -111.07, 'Meadow Station', 45.71, -111.0, 'bluffs', 'Moderate', 5275, 0],
    ['Golden Trail', 'Fort Collins', 'CO', 40.6, -105.09, 'Ridge Station', 40.61, -105.1, 'Falls Station', 40.58, -105.12, 'meadows', 'Moderate', 6681, 0],
    ['Bear Overlook', 'Jackson', 'WY', 43.47, -110.8, 'Falls Station', 43.46, -110.78, 'Bench Station', 43.49, -110.76, 'waterfall', 'Moderate', 7359, 0],
    ['Sage Loop', 'Boulder', 'CO', 40.01, -105.28, 'Creek Station', 40.0, -105.3, 'Saddle Station', 39.99, -105.31, 'lake view', 'Moderate', 6824, 0],
    ['Thunder Pass', 'Salt Lake City', 'UT', 40.79, -111.9, 'Bridge Station', 40.78, -111.91, 'Falls Station', 40.8, -111.93, 'rocky path', 'Hard', 8576, 0],
    ['Canyon Summit', 'Flagstaff', 'AZ', 35.22, -111.63, 'Fork Station', 35.21, -111.66, 'Ridge Station', 35.18, -111.67, 'wildlife', 'Moderate', 5112, 0],
    ['Hidden Trail', 'Sedona', 'AZ', 34.87, -111.75, 'Bridge Station', 34.86, -111.77, 'Falls Station', 34.88, -111.73, 'caves', 'Hard', 6241, 0],
    ['River Loop', 'Moab', 'UT', 38.55, -109.57, 'Bench Station', 38.54, -109.58, 'Saddle Station', 38.57, -109.55, 'river', 'Moderate', 7094, 0],
    ['Aspen Summit', 'Fort Collins', 'CO', 40.62, -105.08, 'Overlook Station', 40.63, -105.1, 'Saddle Station', 40.6, -105.06, 'forest', 'Moderate', 7521, 0],
    ['Crystal Pass', 'Jackson', 'WY', 43.5, -110.79, 'Cave Station', 43.52, -110.8, 'Bench Station', 43.49, -110.77, 'rocky path', 'Hard', 8033, 0],
    ['Cedar Loop', 'Salt Lake City', 'UT', 40.78, -111.87, 'Ridge Station', 40.75, -111.88, 'Falls Station', 40.8, -111.84, 'meadows', 'Moderate', 7411, 0],
    ['Golden Summit', 'Denver', 'CO', 39.77, -104.99, 'Creek Station', 39.76, -105.01, 'Overlook Station', 39.79, -105.02, 'steep climb', 'Hard', 10014, 0],
    ['Maple Canyon Trail', 'Flagstaff', 'AZ', 35.2, -111.69, 'Meadow Station', 35.18, -111.71, 'Saddle Station', 35.21, -111.67, 'wildflowers', 'Moderate', 5127, 0],
    ['Silver Overlook', 'Bozeman', 'MT', 45.7, -111.08, 'Falls Station', 45.69, -111.05, 'Ridge Station', 45.71, -111.03, 'waterfall', 'Moderate', 6128, 0],
    ['Hidden Pass', 'Moab', 'UT', 38.59, -109.53, 'Bridge Station', 38.57, -109.54, 'Fork Station', 38.61, -109.51, 'bluffs', 'Moderate', 6980, 0],
    ['River Trail', 'Boulder', 'CO', 40.0, -105.27, 'Creek Station', 39.99, -105.29, 'Falls Station', 40.02, -105.25, 'river', 'Moderate', 6795, 0],
    ['Mossy Overlook', 'Salt Lake City', 'UT', 40.74, -111.89, 'Saddle Station', 40.72, -111.9, 'Bridge Station', 40.76, -111.87, 'meadows', 'Moderate', 7358, 0],
    ['Redrock Trail', 'Moab', 'UT', 38.57, -109.56, 'Falls Station', 38.55, -109.58, 'Meadow Station', 38.59, -109.54, 'rocky path', 'Hard', 8519, 0],
    ['Pine Loop', 'Boulder', 'CO', 40.03, -105.26, 'Creek Station', 40.02, -105.28, 'Saddle Station', 40.01, -105.24, 'forest', 'Moderate', 6812, 0],
    ['Canyon Pass', 'Flagstaff', 'AZ', 35.21, -111.67, 'Falls Station', 35.2, -111.64, 'Bench Station', 35.18, -111.69, 'lake view', 'Moderate', 4985, 0],
    ['Eagle Summit', 'Denver', 'CO', 39.78, -104.97, 'Overlook Station', 39.8, -105.0, 'Ridge Station', 39.77, -105.02, 'steep climb', 'Hard', 10112, 0],
    ['Willow Pass', 'Fort Collins', 'CO', 40.63, -105.1, 'Bridge Station', 40.62, -105.12, 'Bench Station', 40.64, -105.08, 'wildlife', 'Moderate', 7431, 0],
    ['Golden Canyon Trail', 'Sedona', 'AZ', 34.88, -111.78, 'Cave Station', 34.87, -111.76, 'Saddle Station', 34.9, -111.75, 'caves', 'Hard', 6345, 0],
    ['River Pass', 'Jackson', 'WY', 43.48, -110.81, 'Bench Station', 43.47, -110.79, 'Falls Station', 43.49, -110.83, 'river', 'Moderate', 5444, 0],
    ['Aspen Loop', 'Bozeman', 'MT', 45.67, -111.03, 'Creek Station', 45.66, -111.01, 'Saddle Station', 45.69, -111.05, 'forest', 'Moderate', 6991, 0],
    ['Golden Pass', 'Salt Lake City', 'UT', 40.75, -111.9, 'Falls Station', 40.77, -111.88, 'Overlook Station', 40.73, -111.89, 'bluffs', 'Moderate', 7234, 0],
    ['Hidden Summit', 'Flagstaff', 'AZ', 35.23, -111.66, 'Bridge Station', 35.22, -111.68, 'Meadow Station', 35.25, -111.64, 'forest', 'Moderate', 5288, 0],
    ['Crystal Loop', 'Fort Collins', 'CO', 40.59, -105.06, 'Falls Station', 40.58, -105.09, 'Bench Station', 40.61, -105.07, 'wildflowers', 'Moderate', 7241, 0],
    ['Redrock Overlook', 'Moab', 'UT', 38.6, -109.54, 'Ridge Station', 38.58, -109.56, 'Falls Station', 38.62, -109.52, 'rocky path', 'Hard', 8612, 0],
    ['Sage Trail', 'Boulder', 'CO', 40.02, -105.29, 'Creek Station', 40.04, -105.28, 'Ridge Station', 40.01, -105.32, 'meadows', 'Moderate', 6399, 0],
    ['Silver Loop', 'Denver', 'CO', 39.76, -104.99, 'Meadow Station', 39.77, -105.01, 'Saddle Station', 39.74, -105.0, 'lake view', 'Moderate', 8714, 0], 
    ['Bear Pass', 'Fort Collins', 'CO', 40.64, -105.09, 'Fork Station', 40.63, -105.11, 'Bridge Station', 40.62, -105.12, 'wildlife', 'Moderate', 7581, 0],
    ['Crystal Summit', 'Salt Lake City', 'UT', 40.73, -111.88, 'Creek Station', 40.75, -111.9, 'Falls Station', 40.72, -111.87, 'waterfall', 'Moderate', 8023, 0],
    ['Thunder Loop', 'Jackson', 'WY', 43.51, -110.77, 'Overlook Station', 43.5, -110.78, 'Bench Station', 43.49, -110.75, 'lake view', 'Moderate', 5998, 0],
    ['Bluebonnet Trail', 'Bozeman', 'MT', 45.65, -111.02, 'Falls Station', 45.64, -110.99, 'Ridge Station', 45.66, -111.04, 'forest', 'Moderate', 6721, 0],
    ['Granite Pass', 'Sedona', 'AZ', 34.91, -111.74, 'Bridge Station', 34.9, -111.75, 'Saddle Station', 34.93, -111.72, 'steep climb', 'Hard', 6577, 0]
]



# MAIN

 
def main():

    #Pre-initialized with empty string
    menu_selection =''
    
    while menu_selection != 'X':

        #Display headers
        display_application_header()
        display_menu_options()

        #Validate user menu selection
        menu_selection = input('Enter a selection: ').upper()

        if menu_selection == '1':
            
            #FN1
            display_all_trails()
            
        elif menu_selection == '2':
            
            #FN2
            search_value = input('Enter name: ').title()

            is_found = search_value in TRAIL_NAMES

            if is_found:
                
                display_a_trail(search_value)
           

        elif menu_selection == '3':
            print()

            #FN3
            view_all_rescues()
        elif menu_selection == '4':

            #FN4
            filter_rescues()
        elif menu_selection == 'X':
            break

        else:
            print('Selection Value, not found!')


    #Thank you message for using app
    print('Thank you very much for using',APPLICATION_NAME)


# FUNCTIONS


def display_application_header():
    print()
    print(BANNER_LINE1)
    print(f'{"Victorino Trail Rescue and Safety Bureau":^70}')
    print(f'{"Hiker Rescue Information System":^70}')
    print(BANNER_LINE1)

def display_menu_options():
    print()
    print(f'{INDENT_1}Menu Options')
    print(f'{INDENT_1}{LINE1}')
    print(f'{INDENT_1}1: View all trails')
    print(f'{INDENT_1}2: View a trail')
    print(f'{INDENT_1}3: View all rescue missions')
    print(f'{INDENT_1}4: View filtered rescue mission stats')
    print()
    print(f'{INDENT_1}X: Press to exit')
    print()

#FN1 – VIEW ALL TRAILS
def display_all_trails():
    print(BANNER_LINE2)
    print( 'List of Trails')
    print(BANNER_LINE2)
    print()
    print(f"{'Name':<23}{'City, State':<22}{'Trailhead':^18}{'Difficulty':<12}{'Elev-ft':<9}{'Features':<14}")
    print(f'{LINE2}  {LINE3}  {LINE4}  {LINE5}  {LINE6}  {LINE7}')
    for row in TRAILS:
        name = row[0]
        city = row[1]
        state = row[2]
        trailhead_lat = row[3]
        trailhead_long = row[4]
        difficulty = row[12]
        elevation_feet = row[13]
        features = row[11]

        #Display the data
        print(f'{name:<23}{city + ', ' + state:<22}{'('}{trailhead_lat:<6}{trailhead_long:<7}{')':<3}{difficulty:<10} {elevation_feet:>8,}  {features.title()}') 

    print()
    input('Press enter to continue...')

#FN2 - VIEW A TRAIL
def display_a_trail(search_value):
    print(BANNER_LINE2)
    print( 'Trail Details')
    print(BANNER_LINE2)
    print()
    print(BANNER_LINE3)

    #Display related value using serach_value

    
    for i in range(0,len(TRAILS)):
        if TRAIL_NAMES[i] == search_value:
            
        
        #Extract value from row
            trail_name = TRAILS[i][0]
            city = TRAILS[i][1]
            state = TRAILS[i][2]
            trailhead_lat = TRAILS[i][3]
            trailhead_long = TRAILS[i][4]
            station1_name = TRAILS[i][5]
            station1_lat = TRAILS[i][6]
            station1_long = TRAILS[i][7]
            station2_name = TRAILS[i][8]
            station2_lat = TRAILS[i][9]
            station2_long = TRAILS[i][10]
            difficulty = TRAILS[i][12]
            elevation_feet = TRAILS[i][13]
            features = TRAILS[i][11]

        #Display the data
            print(f"{'Trail Name:':15}{trail_name}")
            print(f"{'City, State:':15}{city}{','}{state}")
            print(f"{'Trail head:':15}{'('}{trailhead_lat}{','} {trailhead_long}{')'}")
            print(f"{'Station #1:':15}{station1_name}{'('}{station1_lat}{','} {station1_long}{')'}")
            print(f"{'Station #2:':15}{station2_name}{'('}{station2_lat}{','} {station2_long}{')'}")
            print(f"{'Difficulty:':15}{difficulty}")
            print(f"{'Elev. (ft):':15}{elevation_feet:,}")
            print(f"{'Features:':15}{features}")
            print(BANNER_LINE3)

    print()
    print()
    print(BANNER_LINE2)
    print('Filter Rescue Missions')
    print(BANNER_LINE2)
    print()


#FN3 - VIEW ALL RESCUE MISSIONS
def view_all_rescues():
    with open(CSVFILE, 'r') as infile:
        reader = csv.reader(infile)
        fields = next(reader)

        print(f"{'Incident ID':<23}{'Hiker Name':<22}{'Trail Name':<18}{' '*8}{'Incident Date':<22}{'Criticality':<2}{' '*6}{'Status':<9}")
        print(f"{LINE8:<23}{LINE8:<22}{LINE8:<18}{' '*8}{LINE8:<21} {LINE9}{' '*6}{LINE9:<9}")

        for row in reader:
            IncidentId = row[0]
            HikerLastName = row[1]
            HikerFirstName = row[2]
            TrailName = row[3]
            IncidentDate = row[6]
            Criticality = row[8]
            Status = row[10]

            full_name = f"{HikerLastName}, {HikerFirstName}"

            print(f'{IncidentId:<23}{full_name:<22}{TrailName:<24}{' '*2}{IncidentDate:<20} {Criticality:^12}{' '*6}{Status:<8}')

    print()
    input('Press enter to continue...')



#FN4 – VIEW FILTERED RESCUE MISSIONS
def filter_rescues():
    with open(CSVFILE, 'r') as infile:
        reader = csv.reader(infile)
        fields = next(reader)

        print('\nEnter Filter Criteria')
        print('-' * 20)
        filter_Incident_ID = input('\nIncidentID: ').strip()
        filter_LastName = input('\nLast Name: ').title().strip()
        filter_FirstName = input('\nFirst Name: ').title().strip()
        filter_TrailName = input('\nTrail Name: ').title().strip()

        crit_input = input('\nCriticality: ').strip()
        filter_Criticality = int(crit_input) if crit_input.isdigit() else None

        filter_Status = input('\nStatus: ').title().strip()

        filtered_rescue_mission = []

        for row in reader:
            IncidentId = row[0]
            HikerLastName = row[1].strip()
            HikerFirstName = row[2].strip()
            TrailName = row[3].strip()
            Latitude = float(row[4])
            Longitude = float(row[5])
            IncidentDate = row[6]
            IncidentTime = row[7]
            Criticality = int(row[8])
            InjuryType = row[9]
            Status = row[10].strip()

            if (not filter_Incident_ID or str(IncidentId).strip().lower().startswith(filter_Incident_ID.lower())) and \
               (not filter_LastName or HikerLastName.lower().startswith(filter_LastName.lower())) and \
               (not filter_FirstName or HikerFirstName.lower().startswith(filter_FirstName.lower())) and \
               (not filter_TrailName or TrailName.lower().startswith(filter_TrailName.lower())) and \
               (filter_Criticality is None or Criticality == filter_Criticality) and \
               (not filter_Status or Status.lower().startswith(filter_Status.lower())):

                new_row = [IncidentId, HikerLastName, HikerFirstName, TrailName,
                           Latitude, Longitude, IncidentDate, IncidentTime,
                           Criticality, InjuryType, Status]
                filtered_rescue_mission.append(new_row)

        filtered_rescue_mission = sorted(filtered_rescue_mission, key=itemgetter(1))
        filtered_rescue_mission = sorted(filtered_rescue_mission, key=itemgetter(2))

        if filtered_rescue_mission:
            display_filtered_rescues(filtered_rescue_mission)
        else:
            print('No rescue missions matched your filter criteria')
            input('Press Enter to return to the menu...')


def display_filtered_rescues(filtered_rescue_mission):
    print(f"{'Incident ID':<23}{'Hiker Name':<22}{'Trail Name':<18}{'     '}{'Incident Date':<22}{'Criticality':<2} {' '*8}{'Status':<9}")
    print(f"{LINE8:<23}{LINE8:<22}{LINE8:<18}{' '*4}{LINE8:<22} {LINE9} {' '*6}{LINE9:<9}")

    for row in filtered_rescue_mission:
        # Extract values from row
        IncidentId = row[0]
        HikerLastName = row[1]
        HikerFirstName = row[2]
        TrailName = row[3]
        Latitude = row[4]
        Longitude = float(row[5])
        IncidentDate = row[6]
        IncidentTime = row[7]
        Criticality = int(row[8])
        InjuryType = row[9]
        Status = row[10]

        
        print(f'{IncidentId:<23}{HikerLastName +', '+ HikerFirstName:<22}{TrailName:<18}{' '*4} {IncidentDate:<20}{Criticality:>8}{' '*13}{Status:^9}')

    print()
    input('Press enter to continue...')

        
main() 
    
