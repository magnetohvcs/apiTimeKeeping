docker build -t api_img backend
docker run --rm -d -p 8080:8080 --link db --name api api_img 