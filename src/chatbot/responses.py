class Responses:
    def __init__(self):
        self.responses = {
            "greeting": "Hello! How can I assist you with your insurance underwriting today?",
            "risk_assessment": "To assess your risk, I need some information about your situation. Can you provide details?",
            "policy_personalization": "We can personalize your policy based on your specific needs. What are your preferences?",
            "thank_you": "Thank you for your input! We will get back to you shortly.",
            "fallback": "I'm sorry, I didn't quite understand that. Can you please rephrase?"
        }

    def get_response(self, intent):
        return self.responses.get(intent, self.responses["fallback"])