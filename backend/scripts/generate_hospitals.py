import json
import random

states = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
    "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu",
    "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Delhi", "Chandigarh"
]

hospital_names = [
    "District Hospital", "Civil Hospital", "Government General Hospital", 
    "Medical College & Hospital", "Institute of Medical Sciences", 
    "Primary Health Centre", "Community Health Centre", "State Hospital", 
    "Ayurvedic Hospital", "Maternity Hospital"
]

specialities = [
    "Cardiology", "Neurology", "Orthopedics", "Pediatrics", "Gynecology", 
    "Oncology", "Dermatology", "ENT", "Ophthalmology", "Urology", 
    "General Surgery", "Internal Medicine", "Dental", "Psychiatry"
]

hospitals = []

# Ensure AIIMS and major institutions exist for specific states
major_hospitals = [
    {
        "name": "AIIMS Delhi", 
        "state": "Delhi", 
        "address": "Sri Aurobindo Marg, Ansari Nagar, New Delhi 110029", 
        "timing": "24x7", 
        "contact_number": "011-26588500", 
        "specialities": ["All Specialities"]
    },
    {
        "name": "Sanjay Gandhi Postgraduate Institute of Medical Sciences (SGPGI)", 
        "state": "Uttar Pradesh", 
        "address": "New PMSSY Rd, Raibareli Rd, Lucknow, Uttar Pradesh 226014", 
        "timing": "OPD: 9:00 AM - 2:00 PM (Mon-Fri)", 
        "contact_number": "0522-2494070", 
        "specialities": ["Cardiology", "Neurology", "Gastroenterology", "Endocrinology"]
    },
    {
        "name": "King Edward Memorial (KEM) Hospital", 
        "state": "Maharashtra", 
        "address": "Acharya Donde Marg, Parel, Mumbai 400012", 
        "timing": "24x7", 
        "contact_number": "022-24107000", 
        "specialities": ["Cardiology", "Neurology", "Orthopedics"]
    },
    {
        "name": "Rajiv Gandhi Government General Hospital", 
        "state": "Tamil Nadu", 
        "address": "EVR Periyar Salai, Park Town, Chennai 600003", 
        "timing": "24x7", 
        "contact_number": "044-25301111", 
        "specialities": ["General Surgery", "Internal Medicine", "Pediatrics"]
    },
    {
        "name": "NIMHANS", 
        "state": "Karnataka", 
        "address": "Hosur Road, Lakkasandra, Bengaluru 560029", 
        "timing": "OPD: 8:00 AM - 4:00 PM", 
        "contact_number": "080-26995000", 
        "specialities": ["Neurology", "Psychiatry", "Neurosurgery"]
    },
]

hospitals.extend(major_hospitals)

def random_phone():
    return "0" + str(random.randint(11, 99)) + "-" + str(random.randint(2000000, 2999999))

for state in states:
    # generate 15 hospitals per state for a comprehensive database
    for i in range(15):
        h_name = f"Government {random.choice(hospital_names)} - {state} Division {i+1}"
        address = f"Main Road, Govt Block, {state} - {random.randint(110000, 899999)}"
        timing = random.choice(["24x7", "OPD: 8:00 AM - 1:00 PM", "OPD: 9:00 AM - 2:00 PM (Mon-Sat)"])
        contact = random_phone()
        
        num_spec = random.randint(2, 6)
        spec = random.sample(specialities, num_spec)
        
        hospitals.append({
            "name": h_name,
            "state": state,
            "address": address,
            "timing": timing,
            "contact_number": contact,
            "specialities": spec
        })

# Write the final JSON to the file
with open('hospitals.json', 'w') as f:
    json.dump(hospitals, f, indent=4)

print(f"Generated {len(hospitals)} hospitals successfully into hospitals.json.")
print("You can now push this hospitals.json file to your GitHub repository!")
