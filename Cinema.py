def main_routine ()
    adult_tickets = 0
    student_tickets = 0
    child_tickets = 0
    gift_tickets = 0
    total_sales = 0
    tickets_sold = 0

selling_ticket = input("Would you like to purchase a ticket? (Y/N): ")
while selling_ticket.upper() != "N":
    ticket = sell_ticket()


    amount_tickets = int(input("How many tickets would you like to purchase?: "))
    confirm = input(f"You want {amount_tickets} of {ticket}, is this correct?: ")
    if confirm == "Y":
        price = amount_tickets * float(get_price(ticket))
        total_sales += price
        tickets_sold += amount_tickets
        if ticket == "A":
            adult_tickets += amount_tickets
        elif ticket == "C":
            student_tickets += amount_tickets
        elif ticket == "S":
            child_tickets += amount_tickets
        else:
            gift_tickets += amount_ticket

        selling_ticket = input("\nDo you want to buy "
                               "another ticket? (Y/N): ").upper()

        print("====================================================")
        print(f"The total tickets purchased is {tickets_sold}\n"
              f"This was made up of: \n"
              f"\t{adult_tickets} for adults; and \n"
              f"\t{student_tickets} for students; and \n"
              f"\t {child_tickets} for children; and \n"
              f"\t{gift_tickets} gift vouchers \n")
        print(f"Sales for the day came to ${total_sales:.2f}")
        print("=====================================================")


        def sell_ticket():
            ticket_type_ = input("What kind of ticket do you want: \n"
                                 "\tA for Adult or, \n"
                                 "\tS for Student or, \n"
                                 "\tC for Child or, \n"
                                 "\tG for Gift voucher\n"
                                 ">> ").upper()
            return ticket_type_


        def get_price(type_):
            prices = [["A", 12.5], ["S", 9], ["C", 7], ["G", 0]]
            for price in prices:
                if price[0] == type_:
                    return price[1]


print("********************** Real Ticketing - System ************************\n")
main_routine()

