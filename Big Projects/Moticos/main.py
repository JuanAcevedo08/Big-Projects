import asyncio
from dealership.bikes import Bike, BikeDealership
from dealership.customer import Customer, DealershipCustomer
from dealership.processes import process_transaction

async def main():

    # Create dealership
    bike_dealership = BikeDealership()
    dealership_buyers = DealershipCustomer()

    # Create bikes
    Kawasaki = Bike(101, "Kawasaki", "H2-R", 56.000)
    Aprilia = Bike(202, "Aprilia", "RS 660", 15.000)
    Triumph = Bike(303, "Kawasaki", "SPEED TRIPLE 1200 RS", 36.000)
    Duke = Bike(404, "Kawasaki", "SuperDuke 1390", 56.000)

    # Create buyers
    customer1 = Customer(105347132, "Juanda", 17, "Juanda@gmail.com")
    customer2 = Customer(105347132, "Lucia", 17, "Lucia@gmail.com")

    # Add bikes to the dealership
    bike_dealership.add_bike(Kawasaki)
    bike_dealership.add_bike(Aprilia)
    bike_dealership.add_bike(Triumph)
    bike_dealership.add_bike(Duke)

    if bike_dealership.check_availability(101):
        bike_dealership.show_bike(101)
        await process_transaction("Juanda", 56.000)
        customer1.buy_bike(Kawasaki)
        bike_dealership.remove_bike(Kawasaki)
        dealership_buyers.add_customer(customer1)

    print("Bike purchased")

    if bike_dealership.check_availability(202):
        bike_dealership.show_bike(202)
        await process_transaction("Lucia", 15.000)
        customer2.buy_bike(Aprilia)
        bike_dealership.remove_bike(Aprilia)
        dealership_buyers.add_customer(customer2)

    bike_dealership.show_bikes()


if __name__ == "__main__":
    asyncio.run(main())
