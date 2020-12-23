# valoStatus
A python library to check for Riot Games server status for **VALORANT** [valorant server status website](https://status.riotgames.com/valorant?locale=en_US)

# Installation
`pip install valoStatus`

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

**we are not doing False here
since we already have a check for that
via `self.get_status_issue()`**
"""
from valoStatus import Region

region = Region("NA")
if region.get_status_issue() == True:
    # code
else:
    if region.incident_check() == True:
        # code
    elif region.maintenance_check() == True:
        # code 
```

### Incidents
```python
from valoStatus import Region

region = Region("NA")

#to get the title of the incident:
print(region.incidents_title())

#to get the date of the incident:
print(region.incidents_date())

#to get the reason of the incident:
print(region.incidents_reason())
```

### Maintenances
```python
from valoStatus import Region

region = Region("NA")

#to get the title of the maintenance:
print(region.maintenances_title())

#to get the date of the maintenance:
print(region.maintenances_date())

#to get the reason of the maintenance:
print(region.maintenances_reason())
```

# Links

**[PyPi](https://pypi.org/project/valoStatus/)**
**[Github](https://github.com/D3CRYPT360/valoStatus)**

# Support
**[Github Profile](https://github.com/D3CRYPT360)**

DM `@D3crypt360` on Twitter