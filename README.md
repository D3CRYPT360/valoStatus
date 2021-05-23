# valoStatus
valoStatus is a Python module to check for Riot Games server status for **VALORANT** [VALORANT Server Status Page](https://status.riotgames.com/valorant?locale=en_US)

This is not fully complete check **TODO** section

If you like this please star the repo. :)

If you would like to contribute to the project feel free to make a PR and fix bugs or make the code even better. :D

# Python Version
- Python 3.6 and above should work

# Installation
`pip install valoStatus`


# Region List
```
NA - North America
EU - Europe
BR - Brazil
AP - Asia Pacific
KR - Korea
LATAM - Latin America
```

# Example code (we will use NA region as an example)

### Check if there is an issue with the server
```python
"""
`self.get_status_issue()` would
return either:
True == There is an issue
False == There is no issue
"""
from valoStatus import Region

region = Region("NA")
if region.get_status_issue() == True:
    # code
else:
    # code
```

### Check if the Issue is either an incident or a Maintenance
```python
"""
`self.incident_check()` and `self.maintenance_check()` would return:
True == There is an issue.
False == There is no issue
"""
from valoStatus import Region

region = Region("NA")
if region.get_status_issue() == True:
    
    if region.incident_check() == True:
        # code
    elif region.maintenance_check() == True:
        # code 
else:
    # code
```

### Incidents
```python
from valoStatus import Region

region = Region("NA")

#to get the title of the incident:
print(region.incident_title())

#to get the date of the incident:
print(region.incident_date())

#to get the reason of the incident:
print(region.incident_reason())
```

### Maintenances
```python
from valoStatus import Region

region = Region("NA")

#to get the title of the maintenance:
print(region.maintenance_title())

#to get the date of the maintenance:
print(region.maintenance_date())

#to get the reason of the maintenance:
print(region.maintenance_reason())
```
# TODO
- Add function for affected platforms
- Add function for time (currently shows date only)
- Colour status function? (may or may not add, basically each type of status has a different colour)

# Links

**[PyPi](https://pypi.org/project/valoStatus/)**

**[Github](https://github.com/D3CRYPT360/valoStatus)**

# Support
**[Github Profile](https://github.com/D3CRYPT360)**

**[Example Discord bot](https://github.com/D3CRYPT360/valorant-server_status_checker-discord_bot)**

DM `@D3crypt360` on Twitter

DM DΞCRYPT#9779 on Discord