# nalo_solutions


Needs local_settings.py file to be in the same folder as settings.py file

run *docker-compose build* and *docker-compose up* with superuser privileges

- Mock data(MOCK_DATA.csv) is in the data subfolder which has to be uploaded via this url
	localhost:8000/api/contacts_upload/

- Visit this url to show list of (paginated) contacts
	localhost:8000/api/contacts/
	You can also add new contacts via same link.
	

- Visit this url to show detail of specific contact by id
	localhost:8000/api/contacts/id
	You can also edit contact details and delete via same link.
	The id should be an integer.
	

