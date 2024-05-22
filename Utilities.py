import getpass
from pprint import pformat
import MongoLogin
from pymongo.errors import OperationFailure
from mongoengine import *
import io


class Utilities:
    """I have several variations on a theme in this project, and each one will need to start up
    with the same MongoDB database.  So I'm putting any sort of random little utilities in here
    as I need them.

    startup - creates the connection and returns the database client."""

    @staticmethod
    def startup():
        print("Logging in.")
        while True:
            username = MongoLogin.username
            password = MongoLogin.password
            project = MongoLogin.project
            hash_name = MongoLogin.hash_name
            cluster = f"mongodb+srv://{username}:{password}@{project}.{hash_name}.mongodb.net/?retryWrites=true&w=majority"
            database_name = 'term_project'
            client = connect(db=database_name, host=cluster)
            try:
                junk = client.server_info()  # Test the connection
                return client[database_name]
            except OperationFailure as OE:
                print(OE)
                print("Error, invalid password.  Try again.")

    @staticmethod
    def print_exception(thrown_exception: Exception):

        with io.StringIO() as output:
            output.write('***************** Start of Exception print *****************\n')
            output.write(f'The exception is of type: {type(thrown_exception).__name__}\n')
            if isinstance(thrown_exception, NotUniqueError):
                error = thrown_exception.args[0]
                message = error[error.index('index:') + 7:error.index('}')]
                index_name = message[:message.index(' ')]
                field_list = message[message.index('{') + 2:]
                fields = []
                while field_list.find(':') > 0:
                    field_length = field_list.find(':')
                    field = field_list[:field_length]
                    fields.append(field)
                    if (field_list.find(', ')) > 0:
                        field_list = field_list[field_list.find(', ') + 2:]
                    else:
                        field_list = ''
                output.write(f'Uniqueness constraint: {index_name} with fields:\n{fields} violated')
            elif isinstance(thrown_exception, ValidationError):
                output.write(f'{pformat(thrown_exception.message)}\n')
                errors = thrown_exception.errors
                for error in errors.keys():
                    output.write(f'field name: {error} has issue: \n{pformat(errors.get(error))}\n')
            results = output.getvalue().rstrip()
        return results


