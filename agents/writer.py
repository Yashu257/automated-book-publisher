# agents/writer.py

def ai_writer(original_text: str) -> str:
    """
    Simulates rewriting the chapter using an AI model.
    In real-world, this would call Gemini/OpenAI API.
    """
    # Simulated "spin" output (for demo)
    rewritten = "[AI-WRITER OUTPUT]\n\n" + original_text[:500] + "\n\n... [Content Truncated for Demo]"
    return rewritten
