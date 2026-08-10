from pydantic import BaseModel, Field
from typing import List

class BenefitScheme(BaseModel):
    scheme_name: str = Field(..., description="The official name of the government scheme")
    state: str = Field(..., description="The state providing the scheme, or 'Central' for national schemes")
    sector: str = Field(..., description="The broad sector: Farmers, Business, Medical, Women, Home, Education, Seniors")
    category: str = Field(..., description="A subcategory, e.g., Insurance, Loans, Scholarships")
    description: str = Field(..., description="A brief summary of the scheme's benefits")
    eligibility_criteria: List[str] = Field(default_factory=list, description="List of conditions required to apply")
    required_documents: List[str] = Field(default_factory=list, description="List of documents needed for application")
    application_steps: List[str] = Field(default_factory=list, description="Sequential steps on how to apply")
