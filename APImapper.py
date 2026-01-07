status_codes = {
    200: "OK - Request Successful",
    201: "Created - Resource Created",
    400: "Bad Request",
    401: "Unauthorized",
    404: "Not Found",
    500: "Internal Server Error"
}

code = int(input("Enter status code: "))
print(status_codes.get(code, "Unknown Status Code"))
