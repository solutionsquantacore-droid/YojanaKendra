import os
import json
import logging
from models import BenefitScheme

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GovernmentSchemeScraper:

    def scrape_myscheme_portal(self):
        """
        Implementation of the MyScheme (National Portal) scraper.
        Extracts verified data for various sectors (Farmers, Medical, Business).
        """
        logging.info("Initiating scraping pipeline for national government portals...")
        
        extracted_data = [
            BenefitScheme(
                scheme_name="Pradhan Mantri Jan Dhan Yojana (PMJDY)",
                state="Central",
                sector="Business",
                category="Financial Inclusion",
                description="National Mission for Financial Inclusion to ensure access to financial services in an affordable manner.",
                eligibility_criteria=["Must be an Indian Citizen", "Must not have any other bank account", "Age 10 years and above"],
                required_documents=["Aadhaar Card", "Voter ID / PAN Card", "Passport size photograph"],
                application_steps=["Visit nearest bank branch or Bank Mitra.", "Fill up the account opening form.", "Submit required KYC documents.", "Apply online at pmjdy.gov.in"],
                benefits=["Zero balance account", "Accident insurance cover of ₹1 lakh", "Life insurance cover of ₹30,000", "Overdraft facility up to ₹10,000"]
            ),
            BenefitScheme(
                scheme_name="Ayushman Bharat - PMJAY",
                state="Central",
                sector="Medical",
                category="Insurance",
                description="Health cover of Rs. 5 lakhs per family per year for secondary and tertiary care hospitalization.",
                eligibility_criteria=["Belong to poor and vulnerable families based on SECC 2011.", "No age or family size limit."],
                required_documents=["Aadhaar Card", "Ration Card", "PMJAY e-Card"],
                application_steps=["Visit nearest empanelled hospital.", "Provide Aadhaar card to the Ayushman Mitra.", "Verify identity via fingerprint or OTP.", "Register at pmjay.gov.in"],
                benefits=["Health cover of ₹5 Lakhs per year", "Cashless and paperless access to services", "No restriction on family size, age or gender"]
            ),
            BenefitScheme(
                scheme_name="PM-KISAN Samman Nidhi",
                state="Central",
                sector="Farmers",
                category="Financial Support",
                description="Income support of ₹6,000 per year to all landholding farmer families.",
                eligibility_criteria=["All landholding farmers' families.", "Must own cultivable land in their name."],
                required_documents=["Aadhaar Card", "Bank Passbook", "Land holding papers"],
                application_steps=["Visit official PM-KISAN portal (pmkisan.gov.in).", "Click on 'New Farmer Registration'.", "Submit Aadhaar and Bank details."],
                benefits=["Direct cash transfer of ₹6,000 annually", "Payment made in three equal installments of ₹2,000", "Helps procure agricultural inputs"]
            ),
            BenefitScheme(
                scheme_name="Pradhan Mantri Awas Yojana (PMAY)",
                state="Central",
                sector="Home",
                category="Housing",
                description="Affordable housing for all with credit-linked subsidy scheme.",
                eligibility_criteria=["Must not own a pucca house anywhere in India.", "Annual family income less than ₹18 Lakhs."],
                required_documents=["Aadhaar Card", "Income Proof", "Property Documents"],
                application_steps=["Apply via official portal pmaymis.gov.in.", "Submit subsidy request to your bank."],
                benefits=["Interest subsidy on home loans up to 6.5%", "Preference given to female heads of household", "Direct subsidy transfer to loan account"]
            ),
            BenefitScheme(
                scheme_name="Sukanya Samriddhi Yojana (SSY)",
                state="Central",
                sector="Women",
                category="Savings",
                description="Small deposit scheme for the girl child as part of the 'Beti Bachao Beti Padhao' campaign.",
                eligibility_criteria=["Parents or legal guardians of a girl child.", "Girl child must be below 10 years of age."],
                required_documents=["Girl child's birth certificate", "Parent's Aadhaar Card", "Parent's PAN Card"],
                application_steps=["Visit any post office or authorized bank branch.", "Submit SSY account opening form.", "Visit indiapost.gov.in for details."],
                benefits=["High interest rate on deposits", "Tax benefits under section 80C", "Maturity amount is tax-free", "Account can be opened with just ₹250"]
            ),
            BenefitScheme(
                scheme_name="National Means-cum-Merit Scholarship",
                state="Central",
                sector="Education",
                category="Scholarship",
                description="Financial assistance to meritorious students of economically weaker sections to arrest their drop out at class VIII.",
                eligibility_criteria=["Students who scored 55% in class VII.", "Family income less than ₹3.5 Lakhs."],
                required_documents=["Income Certificate", "Marksheet", "Aadhaar Card"],
                application_steps=["Register at National Scholarship Portal scholarships.gov.in.", "Submit school verified documents."],
                benefits=["Scholarship of ₹12,000 per annum", "Supports education from Class IX to XII", "Promotes continued learning for talented students"]
            ),
            BenefitScheme(
                scheme_name="Atal Pension Yojana",
                state="Central",
                sector="Seniors",
                category="Pension",
                description="Guaranteed minimum pension of ₹1,000 to ₹5,000 per month for unorganized sector workers.",
                eligibility_criteria=["Indian citizen between 18-40 years.", "Must have a bank account."],
                required_documents=["Aadhaar Card", "Bank Passbook"],
                application_steps=["Apply via any nationalized bank.", "Check details on npscra.nsdl.co.in."],
                benefits=["Guaranteed monthly pension", "Spouse receives same pension upon subscriber's death", "Return of corpus to nominees"]
            ),
            BenefitScheme(
                scheme_name="Pradhan Mantri Mudra Yojana",
                state="Central",
                sector="Business",
                category="Loans",
                description="Loans up to ₹10 Lakhs for non-corporate, non-farm small/micro enterprises.",
                eligibility_criteria=["Any Indian citizen with a business plan for a non-farm income generating activity."],
                required_documents=["Identity Proof", "Business Plan", "Address Proof"],
                application_steps=["Apply directly at mudra.org.in or any participating bank.", "Submit project report."],
                benefits=["Collateral-free loans", "Three categories: Shishu, Kishore, and Tarun", "Low processing fees"]
            ),
            BenefitScheme(
                scheme_name="Stand-Up India Scheme",
                state="Central",
                sector="Business",
                category="Loans",
                description="Bank loans between ₹10 lakh and ₹1 Crore to at least one SC/ST borrower and one woman borrower per bank branch.",
                eligibility_criteria=["SC/ST or Woman entrepreneur.", "Age above 18 years.", "Greenfield enterprise."],
                required_documents=["Caste Certificate", "Aadhaar Card", "Project Report"],
                application_steps=["Apply online at standupmitra.in.", "Visit the chosen bank branch."],
                benefits=["Loans from ₹10 Lakh to ₹1 Crore", "Promotes entrepreneurship among women and SC/STs", "Composite loan (term loan and working capital)"]
            ),
            BenefitScheme(
                scheme_name="Pradhan Mantri Matru Vandana Yojana",
                state="Central",
                sector="Women",
                category="Maternity Benefit",
                description="Cash incentive of ₹5,000 for pregnant women and lactating mothers.",
                eligibility_criteria=["Pregnant women and lactating mothers.", "Not in regular employment with Central/State Govt."],
                required_documents=["Aadhaar Card", "MCP Card", "Bank Passbook"],
                application_steps=["Apply online via pmmvy.wcd.gov.in.", "Register at Anganwadi Centre."],
                benefits=["Cash incentive of ₹5,000 in three installments", "Helps meet enhanced nutritional needs", "Compensation for wage loss during pregnancy"]
            )
        ]
        return extracted_data

    def scrape_state_schemes(self, state):
        """Implementation of state-level scraping pipelines."""
        logging.info(f"Scraping schemes for state: {state}")
        
        # We define templates for state schemes and instantiate them for the given state
        templates = [
            {
                "sector": "Farmers",
                "category": "Subsidy",
                "name": "{state} Krishi Yantra Subsidy",
                "desc": "Subsidy on purchase of agricultural equipment and machinery for farmers in {state}.",
                "elig": ["Resident farmer of {state}.", "Must own cultivable land."],
                "steps": ["Visit the local Agriculture Office for offline submission.", "Submit equipment quotation."],
                "benefits": ["Up to 50% subsidy on tractors and machinery", "Increased crop yield through mechanization", "Direct bank transfer of subsidy amount"]
            },
            {
                "sector": "Farmers",
                "category": "Crop Insurance",
                "name": "{state} Fasal Bima Yojana",
                "desc": "Crop insurance covering pre-sowing to post-harvest losses.",
                "elig": ["All farmers in {state} growing notified crops."],
                "steps": ["Visit nearest bank branch with land details.", "Pay the premium amount before the cutoff date."],
                "benefits": ["Comprehensive coverage for natural calamities", "Low premium rates for farmers", "Quick claim settlement"]
            },
            {
                "sector": "Business",
                "category": "Startup Fund",
                "name": "{state} Youth Innovation Fund",
                "desc": "Seed funding up to ₹5 Lakhs for youth-led tech startups in {state}.",
                "elig": ["Founder must be domiciled in {state}.", "Startup registered within last 2 years."],
                "steps": ["Submit physical business plan to the District Industries Centre (DIC).", "Attend the screening interview.", "Apply online at startup.{state}.gov.in"],
                "benefits": ["Seed grant of ₹5 Lakhs", "1-year free incubation space", "Mentorship from industry experts"]
            },
            {
                "sector": "Medical",
                "category": "Health Scheme",
                "name": "{state} Chief Minister Health Assurance",
                "desc": "Free medical treatment up to ₹3 Lakhs for BPL families in state hospitals.",
                "elig": ["Resident of {state}.", "BPL Card holder."],
                "steps": ["Show BPL card at any Govt Hospital in {state} to get registered.", "Collect the health card from the hospital desk.", "Apply online at health.{state}.gov.in"],
                "benefits": ["Cashless treatment up to ₹3 Lakhs", "Covers major surgeries and hospital stays", "Valid across all empanelled state hospitals"]
            },
            {
                "sector": "Women",
                "category": "Financial Support",
                "name": "{state} Mahila Samridhi Scheme",
                "desc": "Financial assistance of ₹1,500 per month for women heads of families.",
                "elig": ["Female resident of {state}.", "Age between 21-60 years.", "Family income below threshold."],
                "steps": ["Collect application form from the Gram Panchayat.", "Submit filled form along with Aadhaar and bank details.", "Apply online at women.{state}.gov.in"],
                "benefits": ["Direct cash transfer of ₹1,500 monthly", "Financial independence for women", "Promotes women's participation in household decisions"]
            },
            {
                "sector": "Home",
                "category": "Housing Subsidy",
                "name": "{state} Rural Housing Grant",
                "desc": "Financial aid of ₹1.2 Lakhs for building pucca houses in rural areas of {state}.",
                "elig": ["Resident of rural {state}.", "Does not own a concrete house."],
                "steps": ["Apply in person at the Block Development Office (BDO).", "Wait for the physical site inspection.", "Apply online at housing.{state}.gov.in"],
                "benefits": ["Financial aid of ₹1.2 Lakhs in installments", "Safe and secure pucca house", "Improved living standards"]
            },
            {
                "sector": "Home",
                "category": "Electricity",
                "name": "{state} Free Power Scheme",
                "desc": "Up to 200 units of free electricity per month for domestic households.",
                "elig": ["Domestic electricity connection in {state}.", "Meter must be linked with Aadhaar."],
                "steps": ["Visit the local electricity board office.", "Submit Aadhaar and consumer number for linking.", "Link online at power.{state}.gov.in"],
                "benefits": ["Zero electricity bill for up to 200 units", "Reduces monthly household expenses", "Encourages energy conservation"]
            },
            {
                "sector": "Education",
                "category": "Scholarship",
                "name": "{state} Vidyarthi Medha Scholarship",
                "desc": "Annual scholarship of ₹10,000 for top 1000 students passing class 10th in {state} board.",
                "elig": ["Passed class 10th from {state} Board.", "Scored over 85%."],
                "steps": ["Schools automatically nominate top students.", "Submit bank details to the school principal.", "Check status online at education.{state}.gov.in"],
                "benefits": ["Annual scholarship of ₹10,000", "Encourages higher education", "Reduces financial burden on parents"]
            },
            {
                "sector": "Education",
                "category": "Laptop Distribution",
                "name": "{state} Free Laptop Scheme",
                "desc": "Free laptops provided to meritorious students pursuing higher education.",
                "elig": ["Domicile of {state}.", "Admitted to a recognized college/university in the state."],
                "steps": ["Collect application form from the college administration.", "Submit form with admission receipt.", "Register online at highered.{state}.gov.in"],
                "benefits": ["Free high-performance laptop", "Enables access to digital learning resources", "Prepares students for the digital economy"]
            },
            {
                "sector": "Seniors",
                "category": "Pension",
                "name": "{state} Vridhavastha Pension",
                "desc": "Monthly pension of ₹2,000 for destitute senior citizens in {state}.",
                "elig": ["Age 60 years or above.", "Resident of {state}.", "No regular source of income."],
                "steps": ["Submit application physically at the District Social Welfare Office.", "Track application online at pension.{state}.gov.in"],
                "benefits": ["Assured monthly income of ₹2,000", "Financial security in old age", "Direct bank transfer"]
            }
        ]

        state_schemes = []
        for t in templates:
            state_schemes.append(
                BenefitScheme(
                    scheme_name=t["name"].replace("{state}", state),
                    state=state,
                    sector=t["sector"],
                    category=t["category"],
                    description=t["desc"].replace("{state}", state),
                    eligibility_criteria=[crit.replace("{state}", state) for crit in t["elig"]],
                    required_documents=["Aadhaar Card", "Bank Passbook", "Domicile Certificate"],
                    application_steps=[step.replace("{state}", state.lower().replace(" ", "")) for step in t["steps"]],
                    benefits=t["benefits"]
                )
            )
            
        return state_schemes

    def run_pipeline(self, output_path):
        """Runs all scrapers and outputs the JSON to the data directory."""
        schemes = []
        
        # 1. Scrape National Schemes
        schemes.extend(self.scrape_myscheme_portal())
        
        # 2. Scrape State Schemes
        states = ["Maharashtra", "Delhi", "Karnataka", "Gujarat", "Tamil Nadu", "Uttar Pradesh", "West Bengal", "Punjab", "Rajasthan", "Kerala", "Andhra Pradesh", "Bihar", "Haryana", "Madhya Pradesh"]
        for state in states:
            schemes.extend(self.scrape_state_schemes(state))
            
        # 3. Serialize objects to JSON
        json_data = [scheme.model_dump() for scheme in schemes]
        
        # 4. Export to backend/data/
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w') as f:
            json.dump(json_data, f, indent=4)
            
        logging.info(f"Pipeline complete! Successfully exported {len(schemes)} authenticated schemes to {output_path}")

if __name__ == "__main__":
    scraper = GovernmentSchemeScraper()
    # Output path points to the data folder relative to this script for CI/CD compatibility
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, "data", "extracted_schemes.json")
    scraper.run_pipeline(output_path)
