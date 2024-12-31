from app.data.db import resume_db
from app.data.utils import convert_oid_to_str

class ResumeService:

  @staticmethod
  async def get_resume() -> dict:
    resume = await resume_db.resume.find_one({})
    return convert_oid_to_str(resume) or {}

  @staticmethod
  async def get_contact() -> dict:
    resume = await resume_db.resume.find_one({})
    return convert_oid_to_str(resume.get("contact", {}))

  @staticmethod
  async def get_projects() -> dict:
    resume = await resume_db.resume.find_one({})
    return convert_oid_to_str(resume.get("projects", []))

  @staticmethod
  async def get_skills() -> dict:
    resume = await resume_db.resume.find_one({})
    return convert_oid_to_str(resume.get("skills", {}))

  @staticmethod
  async def get_professional_experience() -> dict:
    resume = await resume_db.resume.find_one({})
    return convert_oid_to_str(resume.get("professional_experience", []))

  @staticmethod
  async def get_education() -> dict:
    resume = await resume_db.resume.find_one({})
    return convert_oid_to_str(resume.get("education", {}))