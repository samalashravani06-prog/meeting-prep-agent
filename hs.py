from memory import load_memory, find_contact


def retain_meeting(name, meeting_date, summary, you_promised, they_promised):
    """
    Hindsight replacement.
    The meeting is already saved locally by capture.py,
    so nothing extra is required here.
    """
    return None


def retain_done(name, promise_text, side):
    """
    Completion status is already stored in memory.json
    by memory.mark_done().
    """
    return None


def retain_preference(text):
    """
    Store brief-style preferences locally.
    """
    data = load_memory()

    # Store preferences in a special local section.
    if "_preferences" not in data:
        data["_preferences"] = []

    data["_preferences"].append(text)

    # Import save_memory here to avoid changing memory.py
    from memory import save_memory
    save_memory(data)


def recall_contact(name):
    """
    Recall previous meetings with this contact from memory.json.
    """
    data = load_memory()

    key = find_contact(name, data)

    if key is None:
        return []

    memories = []

    for meeting in data[key]["meetings"]:
        memories.append(
            f"Meeting with {key} on {meeting['date']}. "
            f"Summary: {meeting['summary']}"
        )

        for promise in meeting.get("you_promised", []):
            memories.append(
                f"The user promised: {promise['text']}"
            )

        for promise in meeting.get("they_promised", []):
            memories.append(
                f"{key} promised: {promise['text']}"
            )

    return memories


def recall_preferences():
    """
    Recall locally stored brief preferences.
    """
    data = load_memory()

    return data.get("_preferences", [])