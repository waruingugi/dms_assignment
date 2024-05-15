
# Document Management System
Assigment to demonstrate proficiency in coding and DMS systems.

View the API (swagger documentation):
[DMS API](https://intellisoft-dms.fly.dev/api/schema/swagger-ui/)


# Key Points
-> [The Backend](https://intellisoft-dms.fly.dev/api/schema/swagger-ui/)
-> [The Frontend](https://dms-frontend.fly.dev/users/)

-> Demo Tutorials:
- [How to create a user, create documents types and upload documents](https://www.loom.com/share/e6ca2073d9e040f692865125593ca090?sid=19b29008-ee15-47b8-83aa-2bb75d6f8307)

- [How to update a document and view different versions of a document](https://www.loom.com/share/9eb28647db534810953f4cae5376dd01?sid=b289a324-6562-45be-a08e-a068525d4729
)

- [Reverting to a specific version of a document](https://www.loom.com/share/673ef988d89e4dc38cbea3e4ebedaa2d?sid=e9b6a369-d7d8-4b68-8f1f-19bb7a3f5d26)

- [Searching using the UI and view previous versions](https://www.loom.com/share/66477dac59a646a28f3d198ae7bb1689?sid=a666b758-9d38-4b6e-8982-42b4061e2cb5
)

## Technology stack
I chose to use Django due to it's scale of scabality over other frameworks when needed to deploy an MVP.

Django contains various packages that abstract security, search, CRUD and model creation.

- PostgreSQL
- Django
- Docker
- Redis (Optional)
- Celery (Optional)

## Concepts covered
### Functionality
The project contains two main modules, `authentication` and `documents`.

You can test the api using the below credentials:
```
Email: demo@example.com
Password: demo@example.com
Token: 3391b58f3960a6765cb6b11d8128b82893a9f9a0
```

When using Token authentication on the API, remember to append the keyword Token so that the value looks like this:
`Token 3391b58f3960a6765cb6b11d8128b82893a9f9a0`

Login into to the api using either a password or token.

#### Authentication
The authentication module contains the `users` models as well as it's  CRUD endpoints.

Permissions has been simplified into the following categories for all users:
- SENIOR DOCTOR: can perform create, read, update, delete on all users.
- Doctor: can perform create, edit and update users. But can not delete users.
- Patient: can only view themselves.

#### Documents
The documents module allows:
- Uploading documents
- Deleting documents
- Updating documents
- Creating documents
- Tracking documents (so that you can revert to a specific version)

### Scalability
Documents are saved on AWS S3 to enable near infinite storage while keeping costs low.

I implemented a lite version of github pre-commit hooks like black to conform the project to PEP standards.

Black and isort came in handy for code re-formatting. The are a necessary tool that allows a programmer to focus on logic.

Ggshield was mainly used to prevent secrets leaking. It pro-actively rejects any commits contain vulnerable keys and passwords.

Asynchronous tasks (such as in uploading documents) and redis caching to improve speed would also have been a good addition but were beyond the scope of this project.

I hosted the project on fly.io due to cost effeciency, speed of deployment and ability to scale horizontally quickly for small projects.

But in most cases AWS is a good option.

Heroku fails here due to issues when deploying docker applications.

### User Interface
I developed a quick user interface to interact with the API using django unicorn.

Django unicorn works well for small open source projects.

However a proper framework like Vue.js or React is recommended.

The interface is available here:
[DMS Frontend](https://dms-frontend.fly.dev/users/)

The DMS frontend authentication is locked to `SENIOR_DOCTOR`, which gives you access to all endpoints.

## Key Functionalities
A picture is worth a thousand words.

Use the below short videos, I demonstrate how to use the key areas of the project:

[How to create a user, create documents types and upload documents](https://www.loom.com/share/e6ca2073d9e040f692865125593ca090?sid=19b29008-ee15-47b8-83aa-2bb75d6f8307)

[How to update a document and view different versions of a document](https://www.loom.com/share/9eb28647db534810953f4cae5376dd01?sid=b289a324-6562-45be-a08e-a068525d4729
)

[Reverting to a specific version of a document](https://www.loom.com/share/673ef988d89e4dc38cbea3e4ebedaa2d?sid=e9b6a369-d7d8-4b68-8f1f-19bb7a3f5d26)

[Searching using the UI and view previous versions](https://www.loom.com/share/66477dac59a646a28f3d198ae7bb1689?sid=a666b758-9d38-4b6e-8982-42b4061e2cb5
)
