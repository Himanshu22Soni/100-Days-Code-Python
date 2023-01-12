# If __name == '__main__'.

# If we are importing test file then without even calling its function can be executed so to prevent this we use __main__ that is implemented in test.py.
import test

print(test.__name__)
test.welcome()
