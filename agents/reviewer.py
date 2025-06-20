# agents/reviewer.py

def ai_reviewer(rewritten_text: str) -> str:
    """
    Simulates reviewing the AI-written chapter using another LLM agent.
    In real-world, this could apply improvements, suggest edits, or fix grammar.
    """
    review_output = "[AI-REVIEWER FEEDBACK]\n\n" + rewritten_text[:500] + "\n\n... [Suggestions or Improvements Simulated]"
    return review_output
