from app import create_service2

content_service = create_service2()

if __name__ == '__main__':
    content_service.run(debug=True, port=5002)
