def validate_input(data):
    # Validate input data for the chatbot
    if not isinstance(data, dict):
        raise ValueError("Input data must be a dictionary.")
    required_keys = ['user_id', 'message']
    for key in required_keys:
        if key not in data:
            raise ValueError(f"Missing required key: {key}")

def format_response(response):
    # Format the response from the chatbot
    if isinstance(response, dict):
        return response.get('text', 'No response text available.')
    return 'Invalid response format.'

def log_event(event):
    # Log events for debugging or tracking purposes
    with open('event_log.txt', 'a') as log_file:
        log_file.write(f"{event}\n")