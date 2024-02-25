from app import create_service

auth_service = create_service()

if __name__ == '__main__':
    auth_service.run(debug=True, port=5001)
