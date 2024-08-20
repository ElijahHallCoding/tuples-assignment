def format_itineraries(itineraries):
    # Empty string to store itineraries
    result = ""
    
    # Counter
    itinerary_number = 1
    
    # itinerary Loop
    for itinerary in itineraries:
        
        traveler_name = itinerary[0]
        origin = itinerary[1]
        destination = itinerary[2]
        
        # Format the itinerary 
        result += "Itinerary " + str(itinerary_number) + ": " + traveler_name + " - From " + origin + " to " + destination + "\n"
        
        # Increase the itinerary 
        itinerary_number += 1
    
    # Remove the extra newline character at the end of the string
    result = result.strip()
    
    # Return String
    return result


itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
formatted_itineraries = format_itineraries(itineraries)
print(formatted_itineraries)