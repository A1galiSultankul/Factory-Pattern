from abc import ABC, abstractmethod


class BookingSystem(ABC):
    @abstractmethod
    def bookTicket(self, name, date, showTime, tickets):
        pass

    @abstractmethod
    def deleteTicket(self, name, date):
        pass

    @abstractmethod
    def buyTicket(self, name, date, showTime, tickets):
        pass


class concertTicket(BookingSystem):
    def bookTicket(self, name, date, showTime, tickets):
        print(f"Reserved {tickets} tickets for {name} on {date} at {showTime}, let's quickly buy a ticket to the concert")

    def deleteTicket(self, name, date):
        print("Deletion not supported by the concert")

    def buyTicket(self, name, date, showTime, tickets):
        print(f"Congratulations, {name}! Your {tickets} tickets for the show on {date} at {showTime} are booked.")


class footballGameTicket(BookingSystem):
    def bookTicket(self, name, date, showTime, tickets):
        print(f"Reserved {tickets} tickets for {name} for the football game on {date} at {showTime}.")

    def deleteTicket(self, name, date):
        print(f"Deleted the ticket for {name} for the football game on {date}.")

    def buyTicket(self, name, date, showTime, tickets):
        print(f"Congratulations, {name}! Your {tickets} tickets for the football game on {date} at {showTime} are booked.")

class basketballGameTicket(BookingSystem):
    def bookTicket(self, name, date, showTime, tickets):
        print(f"Reserved {tickets} tickets for {name} for the basketball game on {date} at {showTime}.")

    def deleteTicket(self, name, date):
        print(f"Deleted the ticket for {name} for the basketball game on {date}.")

    def buyTicket(self, name, date, showTime, tickets):
        print(f"Congratulations, {name}! Your {tickets} tickets for the basketball game on {date} at {showTime} are booked.")

class museimTicket(BookingSystem):
    def bookTicket(self, name, date, showTime, tickets):
        print(f"You reserved {tickets} tickets for {name} for the museim show on {date} at {showTime}")

    def deleteTicket(self, name, date):
        print(f"You deleted the ticket for {name} for the museim show on {date}")

    def buyTicket(self, name, date, showTime, tickets):
        print(f"Congratulations, {name}! Your {tickets} tickets for the museim show on {date} at {showTime} are booked")

class movieTicket(BookingSystem):
    def bookTicket(self, name, date, showTime, tickets):
        print(f"You reserved {tickets} tickets for {name} for the movie on {date} at {showTime}")

    def deleteTicket(self, name, date):
        print(f"You deleted the ticket for {name} for the movie on {date}")

    def buyTicket(self, name, date, showTime, tickets):
        print(f"Congratulations, {name}! Your {tickets} tickets for the movie on {date} at {showTime} are booked")

class TicketFactory:
    @staticmethod
    def chooseEvent(type):
        if type == "Concert":
            return concertTicket()
        elif type == "Football":
            return footballGameTicket()
        elif type == "Museim":
            return museimTicket()
        elif type == "Basketball":
            return basketballGameTicket()
        elif type == "Movie":
            return movieTicket()
        else:
            raise ValueError("incorrect selection or we do not have such an event, rerun the program dude")

class Configuration:
        showTimes = ["2pm", "4pm", "6pm", "8pm", "10pm", "12pm", ]

class ConcertShowAdapter(BookingSystem):
    def __init__(self, ticket_system):
        self.ticket_system = ticket_system
        self.purchasedTickets = []

    def bookTicket(self, name, date, showTime, tickets):
        self.ticket_system.bookTicket(name, date, showTime, tickets)
        self.purchasedTickets.append((name, date, showTime, tickets))
        print(f"Booking completed for {name} on {date} at {showTime} for {tickets} tickets.")

    def deleteTicket(self, name, date):
        self.ticket_system.deleteTicket(name, date)

    def buyTicket(self, name, date, showTime, tickets):
        self.ticket_system.buyTicket(name, date, showTime, tickets)
        self.purchasedTickets.append((name, date, showTime, tickets))
        print(f"Purchase completed for {name} on {date} at {showTime} for {tickets} tickets.")

    def viewPurchasedTickets(self):
        if self.purchasedTickets:
            print("Purchased Tickets:")
            for ticket in self.purchasedTickets:
                print(f"Name: {ticket[0]}, Date: {ticket[1]}, Show Time: {ticket[2]}, Tickets: {ticket[3]}")
        else:
            print("No purchased tickets.")

if __name__ == '__main__':
    type = input("Enter the event which one do you want to go (Concert, Football, Basketball, Museum, Movie (write exactly)): ")
    try:
        ticketSystem = TicketFactory.chooseEvent(type)
    except ValueError as e:
        print(f"Error: {e}")
    else:
        adapter = ConcertShowAdapter(ticketSystem)

        while True:
            print("\n1. Book a ticket \n2. Delete a ticket \n3. Buy a ticket \n4. View Purchased Tickets\n5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter your name: ")
                showDate = input("Enter the date (YYYY-MM-DD): ")
                print("Available show times:", Configuration.showTimes)
                showTime = input("Choose the show time: ")
                tickets = int(input("Enter the number of tickets: "))
                adapter.bookTicket(name, showDate, showTime, tickets)

            elif choice == '2':
                name = input("Enter your name: ")
                showDate = input("Enter the date to delete (YYYY-MM-DD): ")
                adapter.deleteTicket(name, showDate)

            elif choice == '3':
                name = input("Enter your name: ")
                showDate = input("Enter the date (YYYY-MM-DD): ")
                print("Available show times:", Configuration.showTimes)
                showTime = input("Choose the show time: ")
                tickets = int(input("Enter the number of tickets: "))
                adapter.buyTicket(name, showDate, showTime, tickets)

            elif choice == '4':
                adapter.viewPurchasedTickets()

            elif choice == '5':
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")