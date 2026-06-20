def classify_persona(user_message):

    message = user_message.lower()

    if any(word in message for word in [
        "api",
        "authentication",
        "token",
        "http",
        "error",
        "integration",
        "technical"
    ]):
        return "Technical Expert"

    elif any(word in message for word in [
        "angry",
        "frustrated",
        "upset",
        "terrible",
        "worst",
        "not working"
    ]):
        return "Frustrated User"

    elif any(word in message for word in [
        "business",
        "revenue",
        "executive",
        "manager",
        "cost",
        "roi"
    ]):
        return "Business Executive"

    return "General User"