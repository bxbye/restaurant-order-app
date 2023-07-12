# Restaurant Order Project

This project manages restaurant's orders process. Users able to order, Order service will track all orders with their status. Restaurant will have a menu that includes several items. OOP principles has been used in this project. After finished infrastructure of this project, I will integrate fastapi or django to manage http requests. Fastapi is able to create api documentation automatically using swagger. I would prefer it because fo that.

# How to test project:
run the commandline code "pytest" in root directory.
this command finds all "test" pattern staring or ending file names and run them.


# for running API and testing it:
1- uvicorn main:app --reload
2- open http://localhost:8000/docs in browser (swagger)
3- docs or redoc endpoints can be used for differen API UI