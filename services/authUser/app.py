from app import create_service
import sys


auth_service = create_service()
print("Running with Python at:", sys.executable)

if __name__ == '__main__':
    auth_service.run(host="0.0.0.0", debug=True, port=5009)
