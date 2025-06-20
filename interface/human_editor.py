# interface/human_editor.py

def human_review_interface(original_text: str, ai_output: str, feedback: str) -> str:
    print("\n--- AI-Reviewed Text Preview (first 500 chars) ---\n")
    print("[AI-REVIEWER FEEDBACK]\n")
    print(feedback)
    print("\n[AI-WRITER OUTPUT]\n")
    print(ai_output[:500])  # Preview only

    decision = input("\n--- Human Editing Section ---\nDo you want to edit or approve the text? (Type 'edit', 'approve', or 'summary'): ").strip().lower()

    if decision == "approve":
        return ai_output

    elif decision == "summary":
        summary = input("Enter your summary of changes or feedback:\n")
        return ai_output + f"\n\n[HUMAN FEEDBACK]: {summary}"

    elif decision == "edit":
        print("\n📋 Full AI output:\n")
        print(ai_output)
        print("\n Please paste your manually edited version below. End input with a single line: __END__")
        print("-----------------------------------------------------------------------")

        edited_lines = []
        while True:
            line = input()
            if line.strip() == "__END__":
                break
            edited_lines.append(line)

        edited_text = "\n".join(edited_lines)
        return edited_text

    else:
        print("Invalid choice. Defaulting to approved AI version.")
        return ai_output
