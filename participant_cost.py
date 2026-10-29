def participant_cost(attendees, food_per_person, transport_per_person):
    return attendees*(food_per_person + transport_per_person)

#test case 1 for normal attendee
cost=(participant_cost(10,800, 200))
print(cost)
# expected result is 10000 naira

#test case 1 for for zero attendees
cost=(participant_cost(0,800, 200))
print(cost)
# expected result is 0 naira