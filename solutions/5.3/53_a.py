try:
    func()  # noqa F821

except ValueError:
    print("ValueError")

except TypeError:
    print("TypeError")

except SystemError:
    print("SystemError")

else:
    print("No Exceptions")
