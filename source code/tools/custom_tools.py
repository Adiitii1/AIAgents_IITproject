import math
from crewai.tools import tool

@tool("RICE Calculator Tool")
def calculate_rice_score(reach: int, impact: float, confidence: float, effort: int) -> str:
    """
    Calculates the RICE score for feature prioritization.
    - reach: Number of users impacted per quarter (e.g., 5000)
    - impact: 3 = Massive, 2 = High, 1 = Medium, 0.5 = Low, 0.25 = Minimal
    - confidence: 1.0 = High (100%), 0.8 = Medium (80%), 0.5 = Low (50%)
    - effort: Person-weeks required (e.g., 2, 4, 8). Minimum 1.
    """
    try:
        effort_val = max(1, effort)
        rice_score = (reach * impact * confidence) / effort_val
        return f"RICE Score: {round(rice_score, 2)} (Reach: {reach}, Impact: {impact}, Confidence: {confidence}, Effort: {effort_val})"
    except Exception as e:
        return f"Error calculating RICE score: {str(e)}"

@tool("Jira Story Formatter Tool")
def format_jira_story(title: str, as_a: str, i_want: str, so_that: str, acceptance_criteria: str, story_points: int) -> str:
    """
    Formats a feature into an agile user story with acceptance criteria and story points.
    """
    formatted_story = f"""
### Story: {title}
**As a** {as_a}
**I want to** {i_want}
**So that** {so_that}

**Acceptance Criteria:**
{acceptance_criteria}

**Story Points (Fibonacci):** {story_points}
--------------------------------------------------
"""
    return formatted_story
