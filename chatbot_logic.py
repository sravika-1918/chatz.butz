def get_bot_reply(message):
    message = message.lower()
    if "dry skin" in message:
        return "Use hydrating products with ingredients like hyaluronic acid."
    elif "oily skin" in message:
        return "Look for non-comedogenic products with salicylic acid."
    elif "routine" in message:
        return "A basic routine includes: cleanser, toner, moisturizer, and sunscreen."
    elif "consult" in message:
        return "For consultations, contact our expert via the chat button on our website."
    else:
        return "Sorry, I didn't get that. Try asking about dry skin, oily skin, or routine."
