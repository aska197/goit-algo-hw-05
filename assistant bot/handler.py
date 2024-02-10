def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, KeyError, IndexError) as e:
            error_messages = {
                KeyError: 'Contact not found.',
                ValueError: 'Invalid command format.',
                IndexError: 'Invalid command format.'
            }
            return error_messages.get(type(e), 'An error occured. Please try again.')
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError # Raise ValurError for invalid command format
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError # Raise ValueError for invalid command format
    name, phone = args
    if name not in contacts:
        raise KeyError # Raise KeyEroor for contact not found
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise ValueError # Raise ValueError for invalid command format
    name = args[0]
    if name in contacts:
        return contacts[name]
    raise KeyError # Raise KeyError for contact not found

@input_error
def show_all(args, contacts):
    if not contacts:
        return 'No contacts available.'
    return '\n'.join([f'{name}: {phone}' for name, phone in contacts.items()])



