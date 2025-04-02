import random

class SimpleChatbot:
    def __init__(self):
        self.responses = {
            "greeting": [" Welcome to our university.How may i help you"],
            "study": ["what would you like to study"],
            "fee": ["For computer science engineering 3.5lalkhs donation and 1.2lpa college fee "],
            "college departments": ["Eight"],
            " Branches": ["CSE EEE CIVIL MECH CSC CSM AIDS AIML"],
            "admission": ["go through gniindia.org website and apply for admission"],
            "hours": ["opening hours-Describe your opening hours here monday to saturday Morning0 09:10 to 04:10  sunday Morning 10:00 To 06:00"],
            "books": ["you need fill the library form,handover to librarian and collect your books"],
            "library system": ["please write your question or choose one of the options 1 opening hours of library system 2 borrowing book of library system"],
            "semister": ["perhaps semister starts from August onwards"],
            "package": ["our highest package is 24LPA"],
            "documents": ["SSC memo Transfer certificate Rank card Study certificates Caste certificate  Income certificates and your person documents likes Aadhar photo etc "],
            "placements": ["Accenture 4.5lLPA 63memebers selected HCL Tech 4.25LPA 13 selected KIML 2.8LPA 70 memebers selected cogizant 4LPA 12members selected TCS 7LPA 3members selected Deloitee 4LPA 6members selected Amazon 3.5LPA 13members selected "],
            "Events": ["conducting a hackthon once in a month"],
            "campus": ["contact the hostel management"],
            "timings": ["Morning 09:10 To 04:10 "],
            "Address": ["Ibrahimpatnam Ranga Reddy District-501506 Hyderabad Telangana INDIA Ph:08414-202120/21 Helpline:80082 95550/51"],
            "campus hostel": ["junior hostel normal rooms 85000 Ac rooms 1lakh20,000 senior hostel normal rooms 90,000 Ac rooms 1lakh30,000"],
            "default": ["Sorry, I don't understand.", "I'm still learning. Can you try again?", "Hmm, not sure what you mean."]
        }
        self.user_data = {}

    def get_response(self, message):
        # Convert message to lowercase for easier comparison
        message = message.lower()

        if message.startswith("my name is"):
            self.user_data['name'] = message[10:]
            return f"Nice to meet you, {self.user_data['name']}!"
        elif message in['may i know the details of campus hostel','campus hostel fee structure','campus hostel']:
            return random.choice(self.responses["campus hostel"])
        elif 'how many departments in your college' in message:
        
            return random.choice(self.responses["college departments"])
        elif 'borrowing books' in message:
            return random.choice(self.responses["books"])
        elif  message in ['opening hours','what are the library hours']:
            return random.choice(self.responses["hours"])
        elif message in ['how do i get to the campus','campus address','college address']:
            return random.choice(self.responses["Address"])
        elif 'computer science engineering' in message:
            return random.choice(self.responses["fee"])
        elif message in ['may i know the information about college fee structure','fee structure']:
            return random.choice(self.responses["study"])
        elif message in ['may i know the information of library system','about library','library system']:
            return random.choice(self.responses["library system"])
        elif message in ['what events are happening on campus','events in campus','events in college']:
            return random.choice(self.responses["Events"])
        elif message in ['how can apply for campus hostel','application of campus hostel']:
            return random.choice(self.responses["campus"])
        elif message in ['when does the semister start','starting of semister','when does the academic begins']:
            return random.choice(self.responses["semister"])
        elif message in ['placements of this year','how many students are placed this year ']:
            return random.choice(self.responses["placements"])
        elif message == 'what are they':
            return random.choice(self.responses[" Branches"])
        elif message in ['highest package in your college','highest package']:
            return random.choice(self.responses["package"])
        elif message in ['how do i apply for admission','admission process']:
            return random.choice(self.responses["admission"])
        elif message in ['what are the office hours for the registration','working hours']:
            return random.choice(self.responses["timings"])
        elif message in ['what documents are required for the admission','admission documents']:
            return random.choice(self.responses["documents"])
        elif message in ['hi', 'hello', 'hey']:
            return random.choice(self.responses["greeting"])
        else:
            return random.choice(self.responses["default"])

    def chat(self):
        print("Welcome to the college management of GNI.")
        while True:
            user_input = input("You: ")
            response = self.get_response(user_input)
            print("Chatbot:", response)
            if user_input.lower() == 'bye':
                break

if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.chat()