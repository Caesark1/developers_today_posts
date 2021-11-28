### Start project
---
1. Clone this repository into your local maching via https or ssh url
2. You need to create your own `.env` file in envs folder like it was written in `.env_example` file in `envs` folder.
3. Run `docker-compose up -d --build` ```NOTE: make sure that you didn't run another site on port 8000```
4. run `docker-compose exec web python manage.py createsuperuser` create super user 
5. and go to the [127.0.0.1:8000](http://127.0.0.1:8000/) and enjoy

### About doc
---
To see and test all apis. There is already swagger. 
After running server you can visit [127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/) to test and see all apis in this project and how to use them
