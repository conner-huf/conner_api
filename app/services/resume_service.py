import json
from pathlib import Path
from app.config import config

class ResumeService:

  @staticmethod
  def load_resume() -> dict:
    """
    Helper method to load the resume JSON data from the file.
    """
    try:
      file_path = Path("app/data/resume.json")
      with file_path.open() as file:
        return json.load(file)
    except FileNotFoundError:
      raise RuntimeError("Resume data file not found")
    except json.JSONDecodeError:
      raise RuntimeError("Error decoding resume data file")
        

  @staticmethod
  async def get_resume() -> dict:
    return ResumeService.load_resume()

  @staticmethod
  async def get_contact() -> dict:
    resume = ResumeService.load_resume()
    return resume.get("contact", [])
    
  @staticmethod
  async def get_projects() -> dict:
    resume = ResumeService.load_resume()
    return resume.get("projects", [])
  
  @staticmethod
  async def get_skills() -> dict:
    resume = ResumeService.load_resume()
    return resume.get("skills", {})

  @staticmethod
  async def get_professional_experience() -> dict:
    resume = ResumeService.load_resume()
    return resume.get("professional_experience", [])
  
  @staticmethod
  async def get_education() -> dict:
    resume = ResumeService.load_resume()
    return resume.get("education", {})