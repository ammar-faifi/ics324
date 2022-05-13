SELECT code, date, destination, source_city
FROM flight_flight
WHERE ACTIVE = 0;

SELECT transaction_id, passenger_id, flight_id, class_type, purchase_date
FROM flight_ticket
WHERE successful = 1;

SELECT COUNT(passenger_id) as numberOfPassaengers , class_type, flight_id
FROM flight_waitinglist
WHERE flight_id = "XY350"
GROUP BY flight_id, class_type;


SELECT id, passenger_id, flight_id, transaction_id
FROM flight_ticket
WHERE successful= 0;


SELECT FLIGHT_DATE, numberOfOccupiedSeates, TOTAL_SEATS
FROM(
    (
        SELECT COUNT(*) as numberOfOccupiedSeates, FLIGHT_DATE
        FROM flight_ticket
        WHERE successful = 1
        GROUP BY date, code 
    ) 
    NATURAL JOIN (
        SELECT code, plane_id, total_seats
        FROM flight_flight JOIN flight_plane ON plane_id=id
    ) 
    );
