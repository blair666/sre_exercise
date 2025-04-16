# Fetch Take Home Exercise - SRE 

## ‬Requirements‬
‭‬Code‬
- Must use either the provided Go or Python code as your starting point‬
‭
- Must accept a YAML configuration as command line argument‬
‭
- YAML format must match that in the sample provided‬
‭
- Must accurately determine the availability of all endpoints during every check cycle‬
‭
- Endpoints are only considered available if they meet the following conditions‬
‭
- Status code is between 200 and 299‬
‭
- Endpoint responds in 500ms or less‬
‭
- Must determine availability cumulatively‬
‭
- Must return availability by domain‬
‭
- Must ignore port numbers when determining domain‬
‭
- Check cycles must run and log availability results every 15 seconds regardless of the‬
‭ number of endpoints or their response times‬
‭ Readme‬
‭
- Must outline how to install and run the code‬
‭
- Must include a section that outlines how each of the issues were identified and why each‬
‭ change to the code was made‬
‭

## Files
- main.py
- sample.yaml
- requirements.txt
- README.md


# How to Test the Script Locally
## 1. Install Dependencies
```
pip install -r requirements.txt

```
## 2.  Run the Script
```
python3 main.py sample.yaml

```
## 3. Sample output
```
---
[2025-04-16 13:40:34] dev-sre-take-home-exercise-rubric.us-east-1.recruiting-public.fetchrewards.com has 50% availability percentage
---
[2025-04-16 13:40:52] dev-sre-take-home-exercise-rubric.us-east-1.recruiting-public.fetchrewards.com has 33% availability percentage
---

```
Each new line reflects cumulative availability — calculated as:
```
(total successful checks for domain) / (total checks) * 100

```
Availability is rounded down using int() (as required), and a new log line appears every 15 seconds.