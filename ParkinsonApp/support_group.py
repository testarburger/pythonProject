class SupportGroup:
    def __init__(self):
        self.members = []

    def join_group(self):
        # Kod do dołączania do grupy wsparcia
        member = input("Enter member name: ")
        self.members.append(member)
        print("Member joined:", member)

    def leave_group(self):
        # Kod do opuszczania grupy wsparcia
        member = input("Enter member name: ")
        if member in self.members:
            self.members.remove(member)
            print("Member left:", member)
        else:
            print("Member not found.")

    def send_message(self):
        # Kod do wysyłania wiadomości do grupy wsparcia
        member = input("Enter member name: ")
        message = input("Enter message: ")
        if member in self.members:
            print("Message sent to", member + ": " + message)
        else:
            print("Member not found.")
