The scripts below are designed to process Raptor reports saved as csv that are saved locally. Updating how files are handled may be necessary.

Note: format of ONE declines changed in fall 2015 to include an additional column for GUID - adding a blank column to existing reports (or re-running them) addresses this.

### top-30.py

Provides the percentage of manuscripts picked up by invitation group.

input: 

- AE Invitation Queue

output: 

- pick up rate for invites 1-3, 4-6, 7-30, 1-30

### papers-per-ed.py

Provides the number of editors who accept invitations to handle manuscripts. When a filename is provided, a file is created showing the number of manuscripts picked up by each editor

input: 

- AE Invitation Queue

output: 

- number of editors handling manuscripts
- file with number of manuscripts picked up by each editor

### declines.py , get_totals.py

Provides counts relating to the number of times editors indicate that they are declining invitations to handle manuscripts because they fall outside their area of expertise.

input:

- ONE Decines
- number of docs queued (found in AE Invitation Queue Summary report)

output:

- total out of area declines
- out of area declines per 100 docs queued
- manuscripts with 6 or more out of area declines
- file with out of area declines per editor
- percent of excessive declines (total declines not including the first 5 declines for each manuscript)

### queue-position.py

input:

- AE Invitation Queue

output:

- creates file with number of ms assigned by queue position

### grouped_declines.py

input:

- 

output:

- 
