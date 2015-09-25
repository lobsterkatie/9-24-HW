def main():
    MELON_COST = 1.00

    transaction_list = get_customer_data_from_log()

    for sale in transaction_list:
        name = sale[0]
        num_melons = sale[1]
        payment = sale[2]
        check_customer_payment(name, num_melons, MELON_COST, payment)


def get_customer_data_from_log(log_file_name="customer-orders.txt"):
    """ Creates and returns a list containing customer data, each customer
        being represented as a list itself.

        Expects log file to be in format
            t_id|name|num|payment
        where
            t_id is a transaction ID
            name is the customer's name
            num is the number of melons purchased
            payment is the amount the customer actually paid   .

        All data save transaction ID are passed along as a list in the same
        order as above.
    """

    log_file = open(log_file_name)

    transaction_list = []

    for line in log_file:
        data = line.split("|")
        data[2] = int(data[2]) #number of melons
        data[3] = float(data[3]) #actual payment
        del data[0] #don't need transacton ID
        transaction_list.append(data) #add new transaction to the list

    return transaction_list




def check_customer_payment(name, num_melons, melon_cost, payment):
    """ Computes expected payment and compares it to actual payment. Prints a
        message to the screen if actual != expected. Returns nothing. """

    expected_payment = num_melons * melon_cost
    if payment != expected_payment:
        out_str = "{name} paid ${actual:,.2f}, but should have paid ${expected:,.2f}"
        print out_str.format(name = name, actual = payment, expected = expected_payment)






main()
